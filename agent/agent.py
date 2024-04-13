from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, AIMessage
from agent.retriver import retrieve_documents
import sqlite3
import os
from uuid import uuid4

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = f"AIE1 - LangGraph - {uuid4().hex[0:8]}"
os.environ["LANGCHAIN_API_KEY"] = "ls__e44d5d7881ca439c9ed14b63c2caae15"
# ------------------ SQlite Database Creation ------------------ #

conn = sqlite3.connect('context_history.db', check_same_thread=False)
cursor = conn.cursor()


#"Creating the table if it doesn't exist."
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_context (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT,
        role TEXT,
        message TEXT)''')

conn.commit()



class LangChatBot:
    def __init__(self, initial_user_info):
        # Initialize LangChain components with a detailed system prompt that includes user details
        model = ChatOpenAI(
            model='gpt-3.5-turbo-1106',
            temperature=0.7
        )
        # Construct the system prompt with the initial user info
        initial_prompt = f"Du bist ein extrem krasser Anwalt. Hier sind einige Informationen über deinen neuen Mandanten: Name: {initial_user_info['name']}, Email: {initial_user_info['email']}, Beschreibung: {initial_user_info['description']}."
        prompt = ChatPromptTemplate.from_messages([
            ("system", initial_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        #search = TavilySearchResults()
        agent = create_openai_functions_agent(
            llm=model,
            prompt=prompt,
            tools=[]
        )
        self.agentExecutor = AgentExecutor(
            agent=agent,
            tools=[retrieve_documents]
        )
        self.chat_history = []


    def chat(self, query, session_id):
        # Insert the user's query into the database
        self.insert_record(session_id, "user", query)

        # Retrieve the chat history which already includes the user's query
        chat_history = self.maintain_history(session_id)

        # Invoke the LangChain agentExecutor with the chat history
        response = self.agentExecutor.invoke({
            "input": query,
            "chat_history": chat_history
        })
        response_content = response["output"]

        # Update the chat history in the database with the new assistant message
        self.insert_record(session_id, "assistant", response_content)

        # Optionally, update the in-memory chat history if needed
        chat_history.append(AIMessage(content=response_content))
        
        return response_content


        
    def insert_record(self, session_id, role, message):
        cursor.execute('INSERT INTO user_context ( session_id, role, message) VALUES (?, ?, ?)', (session_id, role, message))
        conn.commit()

    def maintain_history(self, session_id):
        # Getting history from db
        cursor.execute('SELECT role, message FROM user_context WHERE session_id = ?', (session_id,))
        all_context_data = cursor.fetchall()
        conn.commit()

        history_list = []
        for role, message in all_context_data:
            if role == 'user':
                history_list.append(HumanMessage(content=message))
            elif role == 'assistant':
                history_list.append(AIMessage(content=message))
        
        return history_list




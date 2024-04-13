from langchain_community.vectorstores.elasticsearch import ElasticsearchStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.tools import BaseTool, StructuredTool, tool
from langchain.pydantic_v1 import BaseModel, Field
import streamlit as st
import os
from typing import Optional, Type
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)


def create_elastic_search():
    embedding_function = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")

    ELASTIC_URL = "https://elastic.lightspeedcloud.de/"
    ELASTIC_USER = "elastic"
    ELASTIC_PW = "e9f82c84ecc45f41fa3b5eca851633a4bbb70a3a556fb1da7eb40d3c1b0e78de"
    ELASTIC_INDEX = "urteile"
    elastic_vector_search = ElasticsearchStore(
                es_url=ELASTIC_URL,
                index_name=ELASTIC_INDEX,
                embedding=embedding_function,
                es_user=ELASTIC_USER,
                es_password=ELASTIC_PW
            )
    return elastic_vector_search.as_retriever()


class SearchInput(BaseModel):
    query: str = Field(description="should be a legal search query")


@tool("search-tool", args_schema=SearchInput, return_direct=True)
def retrieve_documents(query: str):
    """Retrieve legal documents from the vector store based on a query."""
    search_results = st.session_state.vector_search.get_relevant_documents(query)
    print(type(search_results))
    return search_results #" ".join(search_results)


class LegalSearchTool(BaseTool):
    name = "legal_search"
    description = "useful for when you need to answer questions about legel matters and court decissions"
    args_schema: Type[BaseModel] = SearchInput

    def _run(
        self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        search_results = st.session_state.vector_search.get_relevant_documents(query)
        """legal stuff."""
        return search_results

    async def _arun(
        self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""

        #search_results = st.session_state.vector_search.get_relevant_documents(query)
        #return search_results
        #raise NotImplementedError("custom_search does not support async")

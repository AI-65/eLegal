from langchain_community.vectorstores.elasticsearch import ElasticsearchStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.tools import BaseTool, StructuredTool, tool
from langchain.pydantic_v1 import BaseModel, Field
import os


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


elastic_vector_search = create_elastic_search()
class SearchInput(BaseModel):
    query: str = Field(description="should be a legal search query")


@tool("search-tool", args_schema=SearchInput, return_direct=True)
def retrieve_documents(query: str):
    """Retrieve legal documents from the vector store based on a query."""
    search_results = elastic_vector_search.get_relevant_documents(query)
    print(type(search_results))
    return " ".join(search_results)


from langchain_community.document_loaders import DataFrameLoader
from langchain_community.vectorstores.elasticsearch import ElasticsearchStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.tools import BaseTool, StructuredTool, tool
import os


def create_elastic_search():
    embedding_function = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")

    elastic_vector_search = ElasticsearchStore(
                es_url=os.getenv("ELASTIC_URL"),
                index_name=os.getenv("ELASTIC_INDEX"),
                embedding=embedding_function,
                es_user=os.getenv("ELASTIC_USER"),
                es_password=os.getenv("ELASTIC_PW")
            )
    return elastic_vector_search.as_retriever()

@tool
def retrieve_documents(query: str, elastic_vector_search) -> list:

    search_results = elastic_vector_search.get_relevant_documents(query)
    return search_results


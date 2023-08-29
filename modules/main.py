__import__('pysqlite3') 
import sys 
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.schema import prompt
from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from .import EMBEDDINGS_BGE_BASE


#loading virtual env
load_dotenv()

# Downloading Embeddings i.e: bge-base-en




class Chatbase:
    def __init__(self, embeddings=EMBEDDINGS_BGE_BASE):
        self.embeddings = embeddings

    def load_text(self, dir):
        loader = TextLoader(dir)
        documents = loader.load()
        return documents

    def split_docs(self,documents, chunk_size=750, chunk_overlap=50):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        splitted_docs = text_splitter.split_documents(documents)
        return splitted_docs

    def embed(self, persist_path, docs):
        try:
            vectordb = Chroma.from_documents(documents=docs,embedding=self.embeddings, persist_directory=persist_path)
            vectordb.persist()
            return True
        except:
            return False

    
    def chat(self, query, vectordb, model_name="gpt-3.5-turbo"):
        matching_docs = vectordb.similarity_search_with_score(query)
        language_model = ChatOpenAI(model_name=model_name)
        retrieval_chain = RetrievalQA.from_chain_type(language_model, chain_type="stuff", retriever=vectordb.as_retriever(search_kwargs={'k':2}))
        response = retrieval_chain.run(query)
        return response


if __name__ == '__main__':
    # docs = chatobj.load_docs('/home/ubuntu/workspace/data')
    # docs_split = chatobj.split_docs(docs)
    # persistDb= chatobj.persist_db('./Database', docs_split)
    chatobj = Chatbase(EMBEDDINGS_BGE_BASE)
    vectordb = Chroma(persist_directory="./Database", embedding_function=EMBEDDINGS_BGE_BASE)
    while(True):
        query = input("Enter the Query: ")
        if query == "exit":
            break
        else:
            with get_openai_callback() as cb:
                resp = chatobj.chat(query, vectordb)
                print(resp,"\n{}".format(cb))

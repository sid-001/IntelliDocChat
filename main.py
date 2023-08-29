import os
from modules.database import KnowledgeBase
from modules.main import Chatbase
from modules import EMBEDDINGS_BGE_BASE
from modules.pdftools import extract_and_clean_pdf_text as cleanPDF
from langchain.vectorstores import Chroma
import streamlit as st
from langchain.callbacks import get_openai_callback
from langchain.document_loaders import TextLoader
import time
from io import StringIO
from pathlib import Path

kb = KnowledgeBase()

home_md = Path("/home/ubuntu/workspace/readme.md").read_text()


def ask(query, persist_dir):
    Query = "Don't justify your answers. Don't give information not mentioned in the CONTEXT INFORMATION " + 'query="{}"'.format(query)
    Chat = Chatbase(EMBEDDINGS_BGE_BASE)
    vectordb = Chroma(persist_directory=persist_dir, embedding_function=EMBEDDINGS_BGE_BASE)
    with get_openai_callback() as cb:
        resp = {
        "response":Chat.chat(Query, vectordb), 
        "prompt":cb.prompt_tokens,
        "completion": cb.completion_tokens,
        "cost": cb.total_cost
        }
        return resp

def embed_text(text_path, persist_path):
    cb = Chatbase()
    docs = cb.load_text(text_path)
    splitted_docs = cb.split_docs(docs)
    embed = cb.embed(persist_path, splitted_docs)
    return True

# Initialize chat history
# if "messages" not in st.session_state:
#     st.title("This the the beggening of Your Chat")
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(name=message["role"], avatar=message['avatar']):
#         st.markdown(message["content"], )

# if prompt := st.chat_input("What's Your Query Today?",):
#     with st.chat_message("user", avatar="https://i.imgur.com/hjaMekQs.png"):
#         st.markdown(prompt)
#     with st.chat_message("ai", avatar="https://i.imgur.com/YbXPMFks.jpeg"):
#         resp = ask(prompt)
#         st.markdown(resp['response'])
#         st.metric(label="Prompt/Completion", value="{}/{} Tokens".format(resp['prompt'], resp['completion']), delta="Total Cost: ${}".format(resp['cost']))
#     st.session_state.messages.append({"role": "User", "content": prompt, "avatar": "https://i.imgur.com/hjaMekQs.png"})
#     st.session_state.messages.append({"role": "Assistant", "content": resp['response'], "avatar":"https://i.imgur.com/YbXPMFks.jpeg"})

sidebar = st.sidebar
sidebar.header('⚡IntelliDocChat', anchor=False, divider='rainbow')
sidebar.caption('Made with :heart: by Siddhartha')
selection = sidebar.selectbox("Select an Option", ['Home','Chat', 'Knowledge Base'])
if selection == 'Home':
    st.header("👋Hey, Welcome to IntelliDocChat", divider=None, anchor=False)
    st.subheader('AI Powered Document Chat Application', anchor=False, help=None, divider='rainbow')
    st.markdown(home_md)

elif selection == "Chat":
    base = []
    for i in kb.get_all_entries():
        base.append(i[0])
    kb_name = sidebar.selectbox("Select a Knowledge Base", base)
    persist_path = kb.get_entry_by_name(kb_name)[1]
    # Initilizing Chat History
    st.header("Welcome to IntelliDocChat👋", divider='rainbow', anchor=False)
    if "messages" not in st.session_state:
        st.session_state.messages = []
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(name=message["role"], avatar=message['avatar']):
            st.markdown(message["content"], )
    # Finally Chat
    if prompt := st.chat_input("What's Your Query Today?",):
        with st.chat_message("user", avatar="https://i.imgur.com/hjaMekQs.png"):
            st.markdown(prompt)
        with st.chat_message("ai", avatar="https://i.imgur.com/YbXPMFks.jpeg"): 
            resp = ask(prompt,persist_path)
            st.markdown(resp['response'])
            st.metric(label="Prompt/Completion", value="{}/{} Tokens".format(resp['prompt'], resp['completion']), delta="Total Cost: ${}".format(resp['cost']))
        st.session_state.messages.append({"role": "User", "content": prompt, "avatar": "https://i.imgur.com/hjaMekQs.png"})
        st.session_state.messages.append({"role": "Assistant", "content": resp['response'], "avatar":"https://i.imgur.com/YbXPMFks.jpeg"})



# KNOWLEDGE BASE
elif selection == "Knowledge Base":
        st.header("📚Knowledge Base", divider=None, help="🚀Upload Your File to Process Further, After a successful upload, the process of converting your text into embeddings will be initiated!", anchor=False)
        name = st.text_input("Name*",placeholder="Enter the Filename", help="Enter the name of this document, so that you can use it later")
        if name != "":
            if kb.entry_exists(name):
                st.error("Knowledge Base with the name {} already exists".format(name))
            else:
                File = st.file_uploader("📄Upload Your Document", type=['pdf',])
                if File is not None:
                    save_folder = '/home/ubuntu/workspace/tmp'
                    save_path = Path(save_folder, File.name)
                    with open(save_path, mode='wb') as w:
                        w.write(File.getvalue())
                    if save_path.exists():
                        with st.status("Processing Your Data...", expanded=True) as status:
                            st.write("Cleaning Your Data...")
                            text = cleanPDF(save_path)
                            st.write("Writing temporary files...")
                            text_path = "{}.txt".format(save_path)
                            with open(text_path, "w") as f:
                                f.write(text)
                            st.write("Generating Embeddings...")
                            persist_path = "/home/ubuntu/workspace/knowledge_base/{}".format(name)
                            embed_text(text_path, persist_path)
                            st.write("Removing temporary Files...")
                            os.remove(save_path)
                            os.remove(text_path)
                            st.write("Indexing Knowledge Base...")
                            kb.insert_entry(name, persist_path)
                            status.update(label="Knowledge base is now indexed and ready to use.", state="complete", expanded=False)


# loader = TextLoader("hello world")
# print(loader.load())
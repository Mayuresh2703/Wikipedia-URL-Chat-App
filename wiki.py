import streamlit as st
import requests
from bs4 import BeautifulSoup
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os 
with st.sidebar:
        st.title('URL Based Chatbot')
        st.markdown("## Conversation History: ")

        if "chat_sessions" not in st.session_state:
            st.session_state.chat_sessions = {}
        
        
        if "active_session" not in st.session_state or st.sidebar.button("New Chat +", use_container_width=True):
            
            chat_id = len(st.session_state.chat_sessions) + 1
            session_key = f"Chat {chat_id}"
            st.session_state.chat_sessions[session_key] = []
            st.session_state.active_session = session_key

        for session in st.session_state.chat_sessions:
            if st.sidebar.button(session, key=session):
                st.session_state.active_session = session
        st.markdown('''
        ## About App:
        This app is an LLM powered chatbot  using:
                    
        - [Streamlit](https://streamlit.io/)
        - [Langchain](https://docs.langchain.com/docs/)
        - [OpenAI](https://openai.com/)

        ## About me:

        - [Github](https://github.com/Mayuresh2703)

        ''')
        st.write("Made by [Mayuresh]")
                    

def get_wikipedia_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    
    return paragraphs


def main():
    # Api Key Input
    api_key = st.text_input("Enter your OpenAI API Key", type="password")
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key

        # Url user input
        st.header("Chat with your URL")
        url = st.text_input("Enter the Wikipedia URL: ")

        if url:
            # extract content from the Wkipedia URL
            wiki_content = get_wikipedia_content(url)

            # split text into chunks
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, length_function=len)
            chunks = text_splitter.split_text('\n'.join(wiki_content))
            
            # Open AI embeddings and vector store 
            embeddings = OpenAIEmbeddings()
            vector_store = FAISS.from_texts(chunks, embedding=embeddings)
            
            # Open AI LLM and initializing a Conversation Chain using langchain
            llm = OpenAI(api_key = api_key, temperature=0)
            qa_chain = ConversationalRetrievalChain.from_llm(llm, vector_store.as_retriever())

            if "active_session" in st.session_state:
                for message in st.session_state.chat_sessions[st.session_state.active_session]:
                    with st.text(message["role"]):
                        st.markdown(message["content"])
            
            # Read user input prompt
            query = st.text_input("Ask your questions from Wkipedia URL ")

            if query:
                # using chat message to initiate User conversation
                st.session_state.chat_sessions[st.session_state.active_session].append({"role": "user", "content": query})
                with st.text("user"):
                    st.markdown(query)

                # Generate response using qa chain with the help of query and previous messages
                result = qa_chain({"question": query, "chat_history": [(message["role"], message["content"]) for message in st.session_state.chat_sessions[st.session_state.active_session]]})
                response = result["answer"]

                # using chat message to initiate Bot conversation
                with st.text("assistant"):
                    st.markdown(response)
                st.session_state.chat_sessions[st.session_state.active_session].append({"role": "assistant", "content": response})

if __name__ == '__main__':
    main()

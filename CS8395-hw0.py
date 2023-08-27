# Step-1 Write all the import statements from the Draft Code.
import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

# Step-2 Write all the function definitions
def summarize_doc(docs):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
    chain = load_summarize_chain(llm, chain_type="stuff")
    return chain.run(docs)

def display_summary(summary):
    if summary:
        st.markdown(f"**Summary:** {summary}")
    else:
        st.markdown("No summary available.")

# Set the title of the application
st.title('Kun Peng_CS8395_hw0')

# Step-3 Get input from the user
text = st.text_input('Enter your text here')

# Step-4 Put a submit button with an appropriate title
if st.button('Summarize'):
    # Step-5 Call functions only if all user inputs are taken and the button is clicked.
    if text:
        #Convert the user's text to a Document object
        doc =  [Document(page_content=text, metadata={'source': 'local'})]
        #Summarize the Document object
        summary = summarize_doc(doc)
        #Display the summary to the user
        display_summary(summary)
    else:
        st.markdown("Please enter some text to summarize.")
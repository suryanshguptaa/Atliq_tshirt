import streamlit as st
from langchain_helper import get_few_shot_db_chain

# Streamlit page config
st.set_page_config(page_title="AtliQ T-Shirts DB Q&A", page_icon="👕", layout="wide")

# Title
st.title("👕 AtliQ T-Shirts Database Q&A")

# Input from user
question = st.text_input("Ask a question about the T-shirts inventory:")

# Load DB chain if not already loaded
if "db_chain" not in st.session_state:
    with st.spinner("Loading local LLaMA model and DB..."):
        st.session_state.db_chain = get_few_shot_db_chain()

# Run query if user asks something
if question:
    try:
        with st.spinner("Generating answer..."):
            response = st.session_state.db_chain.invoke({"query": question})
        st.success("✅ Answer generated!")
        st.write("### Response:")
        st.write(response["result"])
    except Exception as e:
        st.error(f"❌ Error: {e}")

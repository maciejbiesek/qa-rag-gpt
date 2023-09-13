import streamlit as st

from qa_module import AnsweringModel


@st.cache_resource
def load_model():
    return AnsweringModel()


def main():
    with st.spinner("Loading model...."):
        ans_model = load_model()

    st.header("Q&A with polish docs")
    query = st.text_input("Ask a question")

    if query:
        with st.spinner("Searching through the database for the answer..."):
            response, source = ans_model.answer(query)
            st.write(f"Response: {response}")
            st.write(f"Source: {source}")


if __name__ == "__main__":
    main()

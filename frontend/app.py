import streamlit as st
import requests

st.title("AI Repository Assistant")

# -----------------------------
# Process GitHub Repository
# -----------------------------

st.header("GitHub Repository")

github_url = st.text_input(
    "Enter GitHub Repository URL"
)

if st.button("Process Repository", key="process_repo_btn"):

    response = requests.post(
        "http://127.0.0.1:8000/process-repo",
        json={
            "github_url": github_url
        }
    )

    if response.status_code == 200:

        data = response.json()

        st.success(
            data["message"]
        )

        st.write(
            f"Files Loaded: {data['files_loaded']}"
        )

    else:

        st.error(
            f"Error: {response.status_code}"
        )

        st.text(
            response.text
        )

# -----------------------------
# Ask Questions
# -----------------------------

st.header("Ask Questions")

question = st.text_input(
    "Ask a question"
)

if st.button("Submit", key="submit_question_btn"):

    with st.spinner("Thinking..."):

        response = requests.post(
            "http://127.0.0.1:8000/smart-query",
            json={
                "question": question
            }
        )

    if response.status_code == 200:

        data = response.json()

        st.subheader("Route")
        st.write(data["route"])

        st.subheader("Answer")
        st.write(data["answer"])

    else:

        st.error(
            f"Error: {response.status_code}"
        )

        st.text(
            response.text
        )
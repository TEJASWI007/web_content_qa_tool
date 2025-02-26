import streamlit as st
import requests
from bs4 import BeautifulSoup
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Function to scrape webpage content
def scrape_webpage(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            text_content = "\n".join([p.get_text() for p in paragraphs])
            return text_content
        else:
            return f"Error: Unable to fetch {url} (Status Code: {response.status_code})"
    except Exception as e:
        return f"Error: {str(e)}"
# add
# Streamlit UI
st.set_page_config(page_title="Web Content Q&A Tool", layout="wide")
st.title("🔎 Web Content Q&A Tool (Powered by ChatGroq LLaMA)")

# Step 1: Input URLs
st.subheader("Step 1: Enter URLs to Fetch Content")
urls = st.text_area("Enter one or more URLs (one per line):")

if st.button("Ingest Content"):
    url_list = urls.split("\n")
    scraped_data = {}

    for url in url_list:
        url = url.strip()
        if url:
            content = scrape_webpage(url)
            scraped_data[url] = content

    st.session_state["scraped_data"] = scraped_data
    st.success("Content ingested successfully!")

# Step 2: Ask Questions
st.subheader("Step 2: Ask a Question Based on the Content")
question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if "scraped_data" in st.session_state and st.session_state["scraped_data"]:
        combined_content = "\n".join(st.session_state["scraped_data"].values())

        # ChatGroq's LLaMA model (Update API Key)
        llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0, groq_api_key="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")
#  chat = ChatGroq(
#         temperature=0,
#         model="llama-3.1-8b-instant",
#         api_key="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"
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="you are the smart AI who can answer from the context not from the outside of the context.Understand the user query and answer it:\n\n{context}\n\nQuestion: {question}"
        )

        qa_chain = LLMChain(llm=llm, prompt=prompt)
        answer = qa_chain.run(context=combined_content, question=question)

        st.subheader("Answer:")
        st.write(answer)
    else:
        st.warning("No content has been ingested yet. Please enter URLs and ingest content first.")

# Web Content Q&A Tool (Powered by ChatGroq LLaMA)

## Overview
The **Web Content Q&A Tool** is a Streamlit-based application that allows users to scrape web content from given URLs and ask questions based on the retrieved information. It leverages the **ChatGroq LLaMA-3.1-8B-Instant** model to provide context-aware answers.

## Features
- **Web Scraping**: Extracts text content from provided URLs using `BeautifulSoup`.
- **Content Storage**: Saves ingested web content in `st.session_state`.
- **AI-Powered Q&A**: Uses the ChatGroq LLaMA model to generate responses based on the scraped data.
- **User-Friendly UI**: Built with Streamlit for easy interaction.

## Installation
Ensure you have Python installed, then install the required dependencies:

```sh
pip install streamlit requests beautifulsoup4 langchain_groq
```

## How to Use
1. **Run the application**:
   ```sh
   streamlit run app.py
   ```
2. **Enter URLs**: Input one or more URLs (one per line) and click the **Ingest Content** button.
3. **Ask a Question**: Type a question based on the ingested content and click **Get Answer**.
4. **View the Response**: The AI model will generate an answer based on the provided content.

## Code Structure
- `scrape_webpage(url)`: Fetches and extracts text from the given URL.
- `st.session_state["scraped_data"]`: Stores the scraped content.
- `ChatGroq` integration: Uses LLaMA-3.1-8B-Instant for Q&A processing.
- `LLMChain`: Handles the prompt structure and AI-generated responses.

## Example Usage
```
Enter URLs:
https://example.com/article

Enter Question:
What is the main topic of the article?

AI Response:
The article discusses...
```

## Notes
- Ensure the API key for **ChatGroq** is correctly configured before running the script.
- Some websites may block automated scraping. Ensure you comply with their `robots.txt` policies.

## License
This project is open-source and available for modification and distribution.

## Author
Tejaswi Yadav


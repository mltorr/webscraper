import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph
import asyncio
#import platform
import pandas as pd

#https://github.com/ScrapeGraphAI/Scrapegraph-ai

#if platform.system() == "Windows":
#    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

st.title("Scrapes To The Loo")
st.caption("This app allows you to scrape a website using Local AI")

# Set up the configuration for the SmartScraperGraph
graph_config = {
    "llm": {
        "model": "ollama/llama3",
        "temperature": 0,
        "format": "json",  # Ollama needs the format to be specified explicitly
        "base_url": "http://localhost:11434",  
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",
    },
    "verbose": True,
}

# Get the URL of the website to scrape
url = st.text_input("Enter the URL of the website you want to scrape")

# Get the user prompt
user_prompt = st.text_input("What do you want the AI agent to scrape from the website?")

# Create a SmartScraperGraph object
try:
    smart_scraper_graph = SmartScraperGraph(
        prompt=user_prompt,
        source=url,
        config=graph_config
    )

    # Scrape the website
    if st.button("Scrape"):
        result = smart_scraper_graph.run()
        st.write(result)
except NotImplementedError as e:
    st.error(f"An error occurred: {e}")
except AttributeError as e:
    st.error(f"An error occurred: {e}")

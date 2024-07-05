from crewai_tools import EXASearchTool
from crewai_tools import BrowserbaseLoadTool
import streamlit as st

def exa_search_tool():
    exa_search_tool_api = st.input_text("Enter your EXASearch API. Use exa.ai to get one")
    exa_tool = EXASearchTool(exa_search_tool_api)
    return exa_tool


def browserbase_tool():
    browserbase_api = st.input_text("Enter your Browserbase API. Use browserbase.com to get one")
    browserbase_tool = BrowserbaseLoadTool(browserbase_api)
    return browserbase_tool

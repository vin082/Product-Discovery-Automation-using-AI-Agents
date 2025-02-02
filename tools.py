from pydantic import BaseModel, Field
from langchain_community.tools import DuckDuckGoSearchResults

class DuckDuckGoSearchInput(BaseModel):
    query: str = Field(description="Search query")

class DuckDuckGoSearchTool:
    def __init__(self):
        self.name = "DuckDuckGo Search"
        self.description = "A tool for searching the internet using DuckDuckGo"
        self.args_schema = DuckDuckGoSearchInput

    def func(self, query: str) -> str:
        search_tool = DuckDuckGoSearchResults()
        return search_tool.run(query)
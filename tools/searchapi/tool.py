'''搜索工具 Search.api'''
from tools.base import BaseTool
from typing import Any, Dict, Optional
import json

import aiohttp
import requests
import getpass

class Searchapi(BaseTool):
    
    name: str = "searchapi"
    description: str = (
        "Google search API provided by SearchApi.io."
        "This tool is handy when you need to answer questions about current events."
        "Input should be a search query."
    )
    
    def __init__(self,name: str = "searchapi", description: str = 
        "This tool is handy when you need to answer questions about current events,Input should be a search query."
    ,searchapi_api_key=None):
        self.name=name
        self.description=description
        self.searchapi_api_key=searchapi_api_key
    
    def getapi(self,searchapi_api_key=None):
        self.searchapi_api_key=searchapi_api_key
        if self.searchapi_api_key==None:
            self.api=getpass.getpass("请输入你的api-key")
        self.searchapi_api_key=searchapi_api_key
        print("成功")
        return self


    def _prepare_request(self, query: str, **kwargs: Any) -> dict:
        return {
           
            "url": "https://www.searchapi.io/api/v1/search",
            "headers": {
                "Authorization": f"Bearer {self.searchapi_api_key}",
            },
            "params": {
                "engine": "google",
                "q": query,
                **{key: value for key, value in kwargs.items() if value is not None},
            },
        }

    def _search_api_results(self, query: str, **kwargs: Any) -> dict:
        request_details = self._prepare_request(query, **kwargs)
        response = requests.get(
            url=request_details["url"],
            params=request_details["params"],
            headers=request_details["headers"],
        )
        response.raise_for_status()
        return response.json()
    
    def run(self, query: str, **kwargs: Any) -> str:
        results = self._search_api_results(query, **kwargs)
        description=results["knowledge_graph"]["description"]
        return description
        
        

 
    
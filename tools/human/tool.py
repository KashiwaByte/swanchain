"""Tool for asking human input."""
from typing import Callable, Optional
from tools.base import BaseTool



class HumanInputRun(BaseTool):
    def __init__(self, name="human", description="如果你不知道下一步该怎么做或者不知道问题的答案时，你可以求助人类。"):
        super().__init__(name, description)

    def ask(self,text:str) -> None:
      print("\n")
      print(text)
      ans=input()
      return ans

    


    def run(self,query:str):
        self.ask(query)
        return self.input()
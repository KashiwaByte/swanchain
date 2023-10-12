import openai
import json
import getpass

class Agent:
    def __init__(self,model="gpt-3.5-turbo",api=None,tools=None,memory=None,knowledage=None):
        self.api=api
        self.model=model
        self.tools=tools
        self.memory=memory
        self.knowledages=knowledage

    def getapi(self,api=None):
        self.api=api
        if self.api==None:
            self.api=getpass.getpass("请输入你的api-key")
        openai.api_key ="self.api"
        return self
    
    
    
        
    def chat(self,query):
        openai.api_key =self.api
        response = openai.ChatCompletion.create(
        model=self.model,
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query}
    ]
)
        print(response['choices'][0]['message']['content'])
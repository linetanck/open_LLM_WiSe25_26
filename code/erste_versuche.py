# evironment heißt llmsprojekt

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.2:3b', messages=[
  {
    'role': 'user',
    'content': 'What is your name?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)
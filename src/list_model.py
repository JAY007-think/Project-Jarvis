from google import genai
from config import key

client = genai.Client(api_key=key)
for model in client.models.list():
    print(model.name)
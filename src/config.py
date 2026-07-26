from dotenv import load_dotenv
import os
load_dotenv()
NewsApi = os.getenv("NEWS_API_KEY")
OpenAiKey = os.getenv("OPENAI_API_KEY")
key = os.getenv("key")
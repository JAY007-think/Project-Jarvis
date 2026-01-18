from openai import OpenAI
import os

client = OpenAI(
api_key=os.getenv("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role":"system","content":"You are a virtual assistant named jarvis skilled in general task like alexa and google cloud"},
        {"role":"user","content":"what is mango"}
        ]
    )
print(completion.choices[0].message.content)
from openai import OpenAI

client = OpenAI(
api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role":"system","content":"You are a virtual assistant named jarvis skilled in general task like alexa and google cloud"},
        {"role":"user","content":"what is mango"}
        ]
    )
print(completion.choices[0].message.content)
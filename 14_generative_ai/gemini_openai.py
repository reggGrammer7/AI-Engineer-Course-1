from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI(
    api_key ="AIzaSyC5EB9Kmf-N8xDgkenas0gCQn9CRxbBMlM",
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)
response= client.chat.completions.create(
    model="gemini-2.5-flash",
    messages= [
        {"role" : "user", "content": "Hey, I  Regent and nice to meet you "}
    ]
)

print(response.choices[0].message.content)














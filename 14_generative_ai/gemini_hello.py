from google import genai
client = genai.Client(
   # api_key = "AIzaSyC5EB9Kmf-"
)

response = client.models.generate_content(
    model ="gemini-2.5-flash", 
    contents = "Explain how Ai works in few words"
)

print(response.text)

































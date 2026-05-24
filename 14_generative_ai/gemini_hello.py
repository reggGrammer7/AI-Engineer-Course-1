from google import genai
client = genai.Client(
    api_key = "AIzaSyDM0bxIXTkIAEA_hTQ0mi0E4hMO8HKn92o"
)

response = client.models.generate_content(
    model ="gemini-2.5-flash", 
    contents = "Explain how Ai works in few words"
)

print(response.text)

































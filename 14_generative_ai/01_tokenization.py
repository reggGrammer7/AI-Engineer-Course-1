import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")


text = "Hello, welcome to my first LLM application"
tokens = enc.encode(text)
print(tokens)


decoder = enc.decode([13225, 11, 12591, 316, 922, 1577, 451, 19641, 5200])


print(decoder)















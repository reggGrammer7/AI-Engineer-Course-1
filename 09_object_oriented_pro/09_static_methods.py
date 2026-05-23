class chaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    

raw = "water,  milk,     gari, sugar, honey"


word = chaiUtils()
print(word.clean_ingredients(raw))


obj = chaiUtils.clean_ingredients(raw)
print(obj)





from transformers import MarianMTModel, MarianTokenizer

class Translator:
    def __init__(self, model_name="Helsinki-NLP/opus-mt-en-fr"):
        self.model_name = model_name
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)

    def translate(self, text, target_language="fr"):
        if not text:
            raise ValueError("Input text cannot be empty.")
        
        # Prepare the text for translation
        inputs = self.tokenizer.encode(text, return_tensors="pt", padding=True, truncation=True)
        
        # Perform the translation
        with torch.no_grad():
            translated = self.model.generate(inputs, max_length=50, num_beams=4, early_stopping=True)
        
        # Decode the translated text
        translated_text = self.tokenizer.decode(translated[0], skip_special_tokens=True)
        return translated_text

# Example usage
if __name__ == "__main__":
    translator = Translator()
    text_to_translate = "Hello, how are you?"
    translated_text = translator.translate(text_to_translate)
    print(translated_text)
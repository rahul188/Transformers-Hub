from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

class NamedEntityRecognizer:
    def __init__(self, model_name="dbmdz/bert-large-cased-finetuned-conll03-english"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForTokenClassification.from_pretrained(model_name)
        self.ner_pipeline = pipeline("ner", model=self.model, tokenizer=self.tokenizer)

    def recognize_entities(self, text):
        try:
            entities = self.ner_pipeline(text)
            return self.format_entities(entities)
        except Exception as e:
            return {"error": str(e)}

    def format_entities(self, entities):
        formatted_entities = {}
        for entity in entities:
            entity_type = entity['entity']
            entity_text = entity['word']
            if entity_type not in formatted_entities:
                formatted_entities[entity_type] = []
            formatted_entities[entity_type].append(entity_text)
        return formatted_entities

# Example usage
if __name__ == "__main__":
    ner = NamedEntityRecognizer()
    sample_text = "Barack Obama was the 44th President of the United States."
    print(ner.recognize_entities(sample_text))
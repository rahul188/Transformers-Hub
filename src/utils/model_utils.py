from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

def load_model(model_name):
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

def predict(model, tokenizer, text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1)
    return predictions.item()

def load_and_predict(model_name, text):
    model, tokenizer = load_model(model_name)
    prediction = predict(model, tokenizer, text)
    return prediction
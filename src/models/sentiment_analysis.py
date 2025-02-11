from transformers import pipeline

class SentimentAnalysis:
    def __init__(self):
        self.model = pipeline("sentiment-analysis")

    def analyze(self, text):
        try:
            result = self.model(text)
            sentiment = result[0]['label']
            score = result[0]['score']
            return {
                "sentiment": sentiment,
                "score": score
            }
        except Exception as e:
            return {
                "error": str(e),
                "message": "An error occurred while analyzing sentiment."
            }

# Example usage:
# sentiment_analyzer = SentimentAnalysis()
# result = sentiment_analyzer.analyze("I love using Hugging Face Transformers!")
# print(result)
from transformers import pipeline

class TextSummarizer:
    def __init__(self):
        self.model_name = "facebook/bart-large-cnn"
        self.summarizer = pipeline("summarization", model=self.model_name)

    def generate_summary(self, text, max_length=130, min_length=30, do_sample=False):
        try:
            summary = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
            return summary[0]['summary_text']
        except Exception as e:
            return f"Error in summarization: {str(e)}"
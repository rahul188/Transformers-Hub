from transformers import pipeline

class QuestionAnsweringModel:
    def __init__(self):
        self.model = pipeline("question-answering")

    def get_answer(self, question, context):
        try:
            result = self.model(question=question, context=context)
            return result['answer']
        except Exception as e:
            return f"Error occurred: {str(e)}"
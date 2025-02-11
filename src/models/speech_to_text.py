from transformers import pipeline

class SpeechToText:
    def __init__(self):
        self.model = pipeline("automatic-speech-recognition")

    def transcribe(self, audio_file):
        try:
            transcription = self.model(audio_file)
            return transcription['text']
        except Exception as e:
            return f"Error during transcription: {str(e)}"

# Example usage:
# if __name__ == "__main__":
#     stt = SpeechToText()
#     result = stt.transcribe("path_to_audio_file.wav")
#     print(result)
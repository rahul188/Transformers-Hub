from pathlib import Path
import pandas as pd
import json

def load_text_data(file_path):
    if not Path(file_path).exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return pd.read_csv(file_path)

def load_json_data(file_path):
    if not Path(file_path).exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as f:
        return json.load(f)

def preprocess_text_data(data):
    # Implement any necessary preprocessing steps here
    return data.dropna().reset_index(drop=True)

def load_dataset(task_name):
    data_dir = Path(__file__).parent.parent.parent / 'data' / task_name
    if task_name == 'text_summarization':
        return preprocess_text_data(load_text_data(data_dir / 'summarization_data.csv'))
    elif task_name == 'sentiment_analysis':
        return preprocess_text_data(load_text_data(data_dir / 'sentiment_data.csv'))
    elif task_name == 'question_answering':
        return load_json_data(data_dir / 'qa_data.json')
    elif task_name == 'ner':
        return preprocess_text_data(load_text_data(data_dir / 'ner_data.csv'))
    elif task_name == 'translation':
        return preprocess_text_data(load_text_data(data_dir / 'translation_data.csv'))
    elif task_name == 'text_generation':
        return preprocess_text_data(load_text_data(data_dir / 'text_gen_data.csv'))
    elif task_name == 'speech_to_text':
        return load_text_data(data_dir / 'speech_data.csv')
    elif task_name == 'image_captioning':
        return load_text_data(data_dir / 'image_data.csv')
    else:
        raise ValueError(f"Unknown task name: {task_name}")
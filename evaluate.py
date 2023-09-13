import os

import pandas as pd

from qa_module import AnsweringModel
from utils import load_config, save_dataframe


def load_data(data_path: str) -> pd.DataFrame:
    return pd.read_csv(data_path, sep=";", encoding="utf-8")


def predict_answers(model: AnsweringModel, data: pd.DataFrame) -> pd.DataFrame:
    data[['pred_answer', 'pred_source']] = data.apply(lambda x: model.answer(x['query']), axis=1, result_type='expand')
    return data


def evaluate(df_prediction: pd.DataFrame, save_filepath: str):
    df_prediction['correct_answer'] = df_prediction.apply(
        lambda x: x['gold_answer'].lower() in x['pred_answer'].lower(), axis=1)
    df_prediction['correct_source'] = df_prediction['gold_source'] == df_prediction['pred_source']
    save_dataframe(df_prediction, save_filepath)

    print(f"Correct answers: {sum(df_prediction['correct_answer'])}, "
          f"accuracy: {sum(df_prediction['correct_answer']) / len(df_prediction)}")
    print(f"Correct sources: {sum(df_prediction['correct_source'])}, "
          f"accuracy: {sum(df_prediction['correct_source']) / len(df_prediction)}")


def main():
    ans_model = AnsweringModel()
    config_eval = load_config("EVALUATION")
    data = load_data(os.path.join(config_eval.get("DATA_EVAL_PATH"), config_eval.get("DATA_EVAL_FILENAME")))
    pred_data = predict_answers(ans_model, data)
    evaluate(pred_data, os.path.join(config_eval.get("DATA_EVAL_PATH"), config_eval.get("OUTPUT_EVALUATION")))


if __name__ == "__main__":
    main()

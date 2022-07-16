from data.data import *
from evaluate import *
from model.textrank import *
from model.bart import *
from train import build_data_blocks, get_bart_learner, train_bart
import seaborn as sns
import os

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


def test_data():
    test_df = read_orig_data('test', 10)
    print(test_df.head())
    print(add_count_columns(test_df))
    print_selected_articles(test_df, jump=5)

    print_selected_articles_prefix_suffix(test_df, num_samples=2, column_name='article')
    print_selected_articles_prefix_suffix(test_df, num_samples=2, column_name='highlights')


def test_clean_data():
    train_df = read_orig_data('train', 10)
    print(train_df['article'][0])
    clean_train_df = clean_data(train_df)
    print(clean_train_df['article'][0])

    clean_train_df['word_count_text'] = clean_train_df['article'].apply(lambda x: len(nltk.word_tokenize(str(x))))
    sns.displot(clean_train_df["word_count_text"])


def test_textrank():
    test_df = read_orig_data('test', 10)
    summaries = textrank(test_df['article'][0])
    print(summaries[0])


def test_evaluate():
    train_df = read_orig_data('train', num_samples=100)
    pred_sum_corpus = textrank(train_df['article'], ratio=0.3)
    scores = evaluate_avg_rouge(train_df['highlights'], pred_sum_corpus)
    print(scores)


def test_evaluate_textrank_on_clean_test_data():
    test_df = read_clean_data('test_1000', 10)
    pred_sum_corpus = textrank(test_df['article'], ratio=0.3)
    scores = evaluate_avg_rouge(test_df['highlights'], pred_sum_corpus)
    print(scores)


def test_build_pretrained_bart():
    get_pretrained_bart()


def test_bart_data_blocks():
    hf_arch, hf_config, hf_tokenizer, hf_model = get_pretrained_bart()
    train_df = read_orig_data('train', 2)
    dls = build_data_blocks(train_df, hf_arch, hf_config, hf_model, hf_tokenizer, valid_pct=0.5)
    # should be (1, 1) - 1 example for train and 1 for validation
    print(f'{len(dls.train.items)}, {len(dls.valid.items)}')


def test_bart_train():
    hf_arch, hf_config, hf_tokenizer, hf_model = get_pretrained_bart()
    train_df = read_orig_data('train', 10)
    dls = build_data_blocks(train_df, hf_arch, hf_config, hf_model, hf_tokenizer, valid_pct=0.5)
    learn, fit_cbs = get_bart_learner(hf_arch, hf_model, dls)
    train_bart(learn, fit_cbs)


def test_local_bart_summary():
    abs_model_path = "D:/python_projects/NLP_Final_Project/model/ft_cnndm_export_1_EPOCH_75000.pkl"
    assert os.path.exists(abs_model_path), f"model path not exists: {abs_model_path}"

    sample = read_clean_data('test_1000', 1)
    article, summary = sample['article'].array[0], sample['highlights'].array[0]
    inf_learn = load_learner(fname=abs_model_path, cpu=False)
    pred_summary = inf_learn.blurr_summarize(article, early_stopping=True, num_beams=4, num_return_sequences=1)
    print(f"Summary:\n{summary}\n")
    print(f"Predicted summary:\n{pred_summary[0]['summary_texts']}")


def test_bart_summary_from_huggingface():
    sample = read_clean_data('test_1000', 1)
    article = sample['article'].array[0]
    generated_summary = moran_aviv_bart_summary_from_huggingface(article)

    print("\nGenerated Summary:")
    print(generated_summary[0]['generated_texts'])


def main():
    # test_data()
    # test_clean_data()
    # test_textrank()

    # test_evaluate()
    # test_evaluate_textrank_on_clean_test_data()

    # test_build_pretrained_bart()
    # test_bart_data_blocks()
    # test_bart_train()

    # test_local_bart_summary()
    test_bart_summary_from_huggingface()


if __name__ == "__main__":
    main()


import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
import regex as re
import math
import os

# avoiding "up to date" warning message:
# https://stackoverflow.com/questions/23704510/how-do-i-test-whether-an-nltk-resource-is-already-installed-on-the-machine-runni
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

ORIG_DATA_PATH = "./orig_data"
CLEAN_DATA_PATH = "./clean_data"


def read_orig_data(data_type, num_samples=-1):
    """

    :param data_type: 'train'/'val'/'test'
    :param num_samples: num samples to read from csv
    :return: data frame
    """
    data_path = f'{ORIG_DATA_PATH}/{data_type}.csv'
    assert os.path.exists(data_path), f"path not exists: {data_path}"
    if num_samples > 0:
        return pd.read_csv(data_path, nrows=num_samples)
    else:
        return pd.read_csv(data_path)


def read_clean_data(data_type, num_samples=-1):
    """

    :param data_type: 'train'/'val'/'test'
    :param num_samples: num samples to read from csv
    :return: data frame
    """
    data_path = f'{CLEAN_DATA_PATH}/{data_type}.csv'
    assert os.path.exists(data_path), f"path not exists: {data_path}"
    if num_samples > 0:
        return pd.read_csv(data_path, nrows=num_samples)
    else:
        return pd.read_csv(data_path)


def add_count_columns(df_analyzed):
    """

    :param df_analyzed:
    :return: print analysis
    """
    article_words_count = []
    highlights_words_count = []
    article_sentences_count = []
    highlights_sentences_count = []

    for i in range(len(df_analyzed)):
        # words count:
        article_words_count.append(len(df_analyzed['article'].str.lower().str.split()[i]))
        highlights_words_count.append(len(df_analyzed['highlights'].str.lower().str.split()[i]))
        # sentences count:
        article_sentences_count.append(len(sent_tokenize(df_analyzed['article'].str.lower()[i])))
        highlights_sentences_count.append(len(sent_tokenize(df_analyzed['highlights'].str.lower()[i])))

    # add counts columns to df:
    df_analyzed['article_words_count'] = article_words_count
    df_analyzed['highlights_words_count'] = highlights_words_count
    df_analyzed['article_sentences_count'] = article_sentences_count
    df_analyzed['highlights_sentences_count'] = highlights_sentences_count

    return df_analyzed


def print_selected_articles(df, jump=25000):
    """

    :param df: the dataframe
    :param jump: print rows 0, jump, 2*jump...
    :return:
    """
    nrows = df.shape[0]
    selected_articles = [i for i in range(0, nrows, jump)]
    filtered_df = df.iloc[selected_articles]

    for _, values in filtered_df[['article']].iterrows():
        cur_article = values['article']
        print(re.sub("(.{100})", "\\1\n", cur_article, 0, re.DOTALL), end='\n\n')


def print_selected_articles_prefix_suffix(df, num_samples=12, column_name='article', only_prefix=False):
    """

    :param df:
    :param num_samples:
    :param column_name:
    :param only_prefix: if true - no print suffix
    :return:
    """
    nrows = df.shape[0]
    jump = math.floor(nrows / num_samples)
    selected_articles = [i for i in range(0, nrows, jump)]
    filtered_df = df.iloc[selected_articles]

    prefix_list = []
    suffix_list = []
    for _, values in filtered_df[[column_name]].iterrows():
        cur_article = values[column_name]
        prefix_list.append(cur_article[:120])
        suffix_list.append(cur_article[-120:])

    print("Prefix:")
    for pref in prefix_list:
        print(f"{pref}")

    if not only_prefix:
        print("\nSuffix:")
        for suf in suffix_list:
            print(f"{suf}")


def clean_cnn_from_prefix(text):
    """

    :param text:
    :return: the text without "(CNN)" in prefix
    """
    return text[5:] if text[:5] == '(CNN)' else text


def clean_data(df):
    """

    :param df:
    :return: cleaned data frame - specially the prefix
    """
    reg_words = '[\w\\+|\s]*'
    date = f'[0-9]+\:[0-9]+\s+{reg_words},\s+[0-9]+{reg_words}\s+[0-9]+'
    spacer = '\s\.\s'

    # Examples:
    # 'By . Associated Press . PUBLISHED: . 14:11 EST, 25 October 2013 . | . UPDATED: . 15:36 EST, 25 October 2013 . '
    # 'PUBLISHED: . 10:10 EST, 30 June 2013 . | . UPDATED: . 02:30 EST, 1 July 2013 . '
    regex_1 = f'PUBLISHED:{spacer}{date}{spacer}\|{spacer}UPDATED:{spacer}{date}{spacer}'
    # UPDATED: . 03:12 EST, 8 February 2012 .
    regex_2 = f'UPDATED:{spacer}{date}{spacer}'
    # Example: 'By . Eleanor Crooks, Press Association . '
    regex_3 = f'By{spacer}{reg_words},\sPress Association\s\.\s'
    # Example: 'By . Daily Mail Reporter . '
    regex_4 = f'By{spacer}{reg_words}\.\s'
    # Example: 'By SAM TAYLOR FOR THE DAILY MAIL . '
    regex_5 = f'By[\s\w\\+]+{spacer}'
    # Example: 'Canberra, Australia (CNN) -- ', 'London (CNN)  -- ', 'WASHINGTON (CNN)  -- ', '(CNN)  -- ',
    regex_6 = f'[A-Z][a-z]+,\s[A-Z][a-z]+\s+\(CNN\)\s+--\s'
    regex_7 = f'[A-Z]+[a-z]*\s+\(CNN\)\s+--\s'
    regex_8 = f'\(CNN\)\s+--\s'
    # Example: '(CNN) -- '
    regex_9 = f'\([\w\\+|\.|\s]*\)\s--\s'
    # The rest: 'and Michael Zennie . ', 'and Reuters .'
    regex_10 = f'and[\s[A-Za-z]+]*\s.\s'

    print(f"start copy df")
    df_clean = df.copy()

    reg_dict = {'reg_1': regex_1,
                'reg_2': regex_2,
                'reg_3': regex_3,
                'reg_4': regex_4,
                'reg_5': regex_5,
                'reg_6': regex_6,
                'reg_7': regex_7,
                'reg_8': regex_8,
                'reg_9': regex_9,
                'reg_10': regex_10}

    for i in range(1, len(reg_dict) + 1):
        reg_name = f'reg_{i}'
        print(f'start working on {reg_name}')
        cur_reg = reg_dict[reg_name]
        df_clean['article'] = df_clean['article'].str.replace(f'({cur_reg})', '', regex=True)

    # clean '\n'
    df_clean['article'] = df_clean['article'].str.replace(f'(\n)', ' ', regex=True)

    # clean (CNN) in the beginning
    print('Start \'(CNN)\' clean')
    df_clean['article'] = df_clean.apply(lambda x: clean_cnn_from_prefix(x['article']), axis=1)

    # clean the highlights
    df_clean['highlights'] = df_clean['highlights'].str.replace(f'(\n)', ' ', regex=True)

    print('Finish clean')

    return df_clean


def write_clean_data(df, data_type):
    """

    :param df:
    :param data_type: 'train'/'val'/'test'
    :return: save the dataframe
    """
    if 'id' in df.columns:
        df.drop('id', axis=1, inplace=True)
    df.to_csv(f'./clean_data/{data_type}.csv', index=False)

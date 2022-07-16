# For avoiding warning when using gensim from main:
# "UserWarning: detected Windows; aliasing chunkize to chunkize_serial"
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import gensim


def textrank(article_corpus, ratio=0.2):
    """

    :param article_corpus:
    :param ratio: summarization length related to article.
                  Example: if article has 100 sentences and ratio=0.2, so summary will be at most 20 sentences
    :return:
    """
    if type(article_corpus) is str:
        article_corpus = [article_corpus]
    summaries = [gensim.summarization.summarize(txt, ratio=ratio) for txt in article_corpus]
    return summaries

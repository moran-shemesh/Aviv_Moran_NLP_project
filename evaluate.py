from rouge import Rouge


def evaluate_avg_rouge(summary_corpus, pred_summary_corpus):
    """

    :param summary_corpus: array of summarises
    :param pred_summary_corpus: array of generated summarises
    :return:
    """
    assert len(summary_corpus) == len(pred_summary_corpus), f"summary and predicted summary have no same length: {len(summary_corpus)}, {len(pred_summary_corpus)}"
    assert len(summary_corpus) > 0, f"num of summaries is 0!"
    if type(summary_corpus) is str:
        summary_corpus = [summary_corpus]
    if type(pred_summary_corpus) is str:
        pred_summary_corpus = [pred_summary_corpus]

    avg_scores = {'rouge-1': 0, 'rouge-2': 0, 'rouge-L': 0}

    rouge_obj = Rouge()
    for (txt, pred_txt) in zip(summary_corpus, pred_summary_corpus):
        if pred_txt == '':
            score_1 = 0
            score_2 = 0
            score_L = 0
        else:
            scores = rouge_obj.get_scores(refs=txt, hyps=pred_txt, avg=True)
            score_1 = round(scores['rouge-1']['f'], 3)
            score_2 = round(scores['rouge-2']['f'], 3)
            score_L = round(scores['rouge-l']['f'], 3)

        avg_scores['rouge-1'] = avg_scores['rouge-1'] + score_1
        avg_scores['rouge-2'] = avg_scores['rouge-2'] + score_2
        avg_scores['rouge-L'] = avg_scores['rouge-L'] + score_L

    avg_scores['rouge-1'] = round(avg_scores['rouge-1'] / len(summary_corpus), 2)
    avg_scores['rouge-2'] = round(avg_scores['rouge-2'] / len(summary_corpus), 2)
    avg_scores['rouge-L'] = round(avg_scores['rouge-L'] / len(summary_corpus), 2)
    return avg_scores

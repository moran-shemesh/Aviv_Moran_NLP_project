from model.bart import *


MAX_ART_LEN = 256  # 256
MAX_SUM_LEN = 130


def build_data_blocks(df, hf_arch, hf_config, hf_model, hf_tokenizer, valid_pct=0.2):
    """

    :param df: articles ad highlights
    :param hf_arch:
    :param hf_config:
    :param hf_model:
    :param hf_tokenizer:
    :param valid_pct: the part from df which will be in validation set
    :return:
    """
    text_gen_kwargs = default_text_gen_kwargs(
        hf_config, hf_model, task='summarization')

    hf_batch_tfm = Seq2SeqBatchTokenizeTransform(
        hf_arch, hf_config, hf_tokenizer, hf_model,
        max_length=MAX_ART_LEN, max_tgt_length=MAX_SUM_LEN,
        text_gen_kwargs=text_gen_kwargs
    )

    blocks = (Seq2SeqTextBlock(batch_tokenize_tfm=hf_batch_tfm), noop)
    dblock = DataBlock(blocks=blocks, get_x=ColReader('article'),
                       get_y=ColReader('highlights'), splitter=RandomSplitter(valid_pct=valid_pct, seed=42))

    dls = dblock.dataloaders(df, bs=2)

    return dls


def get_bart_learner(hf_arch, hf_model, dls):
    """

    :param hf_arch:
    :param hf_model:
    :param dls: DataBlock
    :return:
    """
    seq2seq_metrics = {
        'rouge': {
            'compute_kwargs': {'rouge_types': ["rouge1", "rouge2", "rougeL"], 'use_stemmer': True},
            'returns': ["rouge1", "rouge2", "rougeL"]
        },
        'bertscore': {
            'compute_kwargs': {'lang': 'en'},
            'returns': ["precision", "recall", "f1"]
        }
    }

    model = BaseModelWrapper(hf_model)
    learn_cbs = [BaseModelCallback]
    fit_cbs = [Seq2SeqMetricsCallback(custom_metrics=seq2seq_metrics)]

    learn = Learner(dls,
                    model,
                    opt_func=ranger,
                    loss_func=CrossEntropyLossFlat(),
                    cbs=learn_cbs,
                    splitter=partial(blurr_seq2seq_splitter, arch=hf_arch)).to_fp16()

    learn.create_opt()
    learn.freeze()

    # learn.lr_find(suggest_funcs=[minimum, steep, valley, slide])

    return learn, fit_cbs


def train_bart(learn, fit_cbs, num_epochs=1):
    """

    :param learn: Learn object
    :param fit_cbs: callbacks
    :param num_epochs: number of epochs
    :return:
    """
    learn.fit_one_cycle(num_epochs, lr_max=3e-5, cbs=fit_cbs)


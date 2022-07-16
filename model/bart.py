from pynvml import *
from fastai.text.all import *
from transformers.models.bart import BartForConditionalGeneration
from blurr.text.modeling.all import *
from blurr.text.data.all import *
from huggingface_hub import from_pretrained_fastai

from blurr.text.utils import get_hf_objects


def print_gpu_utilization():
    """

    :return: print GPU utilization
    """
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)
    info = nvmlDeviceGetMemoryInfo(handle)
    print(f"GPU memory occupied: {info.used//1024**2} MB.")


def get_pretrained_bart():
    """

    :return: blurr objects
    """
    pretrained_model_name = "facebook/bart-large-cnn"
    hf_arch, hf_config, hf_tokenizer, hf_model = get_hf_objects(pretrained_model_name, model_cls=BartForConditionalGeneration)

    return hf_arch, hf_config, hf_tokenizer, hf_model


def upload_model_to_huggingface(learner, tokenizer, repo_id):
    """

    :param learn: Blurr Learn object
    :param tokenizer:
    :param repo_id: example: "Aviv/Moran_Aviv_Bart"
    :return:
    """
    from huggingface_hub import push_to_hub_fastai
    push_to_hub_fastai(learner=learner, repo_id=repo_id)
    tokenizer.save_pretrained("https://huggingface.co/Aviv/Moran_Aviv_Bart/", push_to_hub=True)


def moran_aviv_bart_summary_from_huggingface(corpus):
    """
    Note: the pretrained Moran_Aviv_model is same model: "ft_cnndm_export_1_EPOCH_75000.pkl"
    :param corpus: array of articles (= texts)
    :return: generated summaries
    """
    if type(corpus) is str:
        corpus = [corpus]

    repo_id = "Aviv/Moran_Aviv_Bart"

    print("start get pretrained model from hub")
    inf_learn = from_pretrained_fastai(repo_id)
    print("Finish get pretrained model from hub")

    if torch.cuda.is_available():
        print("Use cuda!")
        inf_learn.to(device="cuda:0")

    print("Start generate text")
    generated_summaries = inf_learn.blurr_generate(corpus)
    return generated_summaries

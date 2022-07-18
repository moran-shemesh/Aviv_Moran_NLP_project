# Text Summarization
NLP final project - Moran Shemesh and Aviv Lazar

## Repo intro
Data Repo:
https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail
TODO: share google drive

Cleaned Data Repo:
https://drive.google.com/drive/folders/1YiL61JCVwMQvRwQWcf0cAIyZfSWtmMJF?usp=sharing

## Installation | Requirements
See requirement file:
https://github.com/moran-shemesh/Aviv_Moran_NLP_project/blob/main/requirements.txt

## Quickstart
Try it on the App:
https://huggingface.co/spaces/Moran/Aviv_Moran_Summarization

You can download our Bart model from HuggingFace:
https://huggingface.co/Aviv/Moran_Aviv_Bart

repo_id = "Aviv/Moran_Aviv_Bart"
inf_learn = from_pretrained_fastai(repo_id)
generated_summaries = inf_learn.blurr_generate(corpus)
You can see an example of using the model here: 
https://github.com/moran-shemesh/Aviv_Moran_NLP_project/blob/main/experiments/Summarization_with_Blurr_notebook_3_Bart_streamlit.ipynb

## Resources


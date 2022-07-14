# https://moran-shemesh-nlp-project-streamlit-app-v9djv3.streamlitapp.com/
# https://www.datacamp.com/tutorial/streamlit
# /home/appuser/venv/bin/python -m pip install --upgrade pip
# pip install --upgrade -r requirements.txt
import streamlit as st
# import time
from huggingface_hub import from_pretrained_fastai
import gensim


# textRank
def textrank(corpus, ratio=0.2):    

  if type(corpus) is str:        

      corpus = [corpus]    

  summaries = [gensim.summarization.summarize(txt, ratio=ratio) for txt in corpus]    

  return summaries

# import numpy as np
# from transformers import *
# from transformers import BartForConditionalGeneration

# from fastai.text.all import *
# from blurr.text.data.all import *
# from blurr.text.modeling.all import *
# import blurr.text

# model = BartForConditionalGeneration.from_pretrained("Moran/Moran_Aviv_Bart",from_tf=True)

# inf_learn = load_learner(fname='Moran/Moran_Aviv_Bart')
# import torch
# from google.colab import drive
# drive.mount('/content/drive')

# url = ' google drive sharing link'
# path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]


# @st.cache(allow_output_mutation=True)
# kaggle_dir = f"/content/drive/MyDrive/HIT/NLP/Final_Project/cnn_daily_mail_dataset/kaggle/cnn_dailymail"
repo_id = "Aviv/Moran_Aviv_Bart"
# inf_learn = from_pretrained_fastai(repo_id)

def start_summarize():
    pass

st.title ("Text Summarization") 
model_type = st.radio('Pick a model',['RankText', 'Bart'])
text = st.text_area('Enter or paste your text')
st.button('Summarize', on_click=start_summarize)





# summary = inf_learn.blurr_summarize(text)
st.title(text)

# st.title(inf_learn.blurr_summarize(text))


grade = st.select_slider(
     'What do you think about the summary?',
     options=['Bad', 'Good', 'Excellent'],
     value=('Good'))


st.header(" © Aviv Lazar & Moran Shemesh")
# url = 'https://drive.google.com/file/d/16XYO5xFM16hXMBshK4orssiTDkhggo98/view?usp=sharing'
# filename = url.split('/')[-1]



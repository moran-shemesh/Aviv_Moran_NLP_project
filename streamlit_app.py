# https://moran-shemesh-nlp-project-streamlit-app-v9djv3.streamlitapp.com/
# https://www.datacamp.com/tutorial/streamlit
# /home/appuser/venv/bin/python -m pip install --upgrade pip
# pip install --upgrade -r requirements.txt
import streamlit as st
# import time
import numpy as np
# from transformers import BartForConditionalGeneration
from huggingface_hub import from_pretrained_fastai
from fastai.text.all import *

# from fastai.blurr.text import *

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
inf_learn = from_pretrained_fastai(repo_id)


st.title ("Text Summarization") 
model_type = st.radio('Pick a model',['RankText', 'Bart'])
text = st.text_area('Enter or paste your text')
st.button('Summarize')

# summary = inf_learn.blurr_summarize(text)
# st.title(summary)

st.title(inf_learn.blurr_summarize(text))


grade = st.select_slider(
     'What do you think about the summary?',
     options=['Bad', 'Good', 'Excellent'],
     value=('Good'))


st.header(" © Aviv Lazar & Moran Shemesh")
# url = 'https://drive.google.com/file/d/16XYO5xFM16hXMBshK4orssiTDkhggo98/view?usp=sharing'
# filename = url.split('/')[-1]



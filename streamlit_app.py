# https://moran-shemesh-nlp-project-streamlit-app-v9djv3.streamlitapp.com/
# https://www.datacamp.com/tutorial/streamlit
import streamlit as st
import time
from huggingface_hub import from_pretrained_fastai
import gensim
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

st.caption(" © Aviv Lazar & Moran Shemesh")

def textrank(corpus, ratio=0.2):    
  if type(corpus) is str:        
      corpus = [corpus]    
  summaries = [gensim.summarization.summarize(txt, ratio=ratio) for txt in corpus][0]
#  st.write(summaries)   
  return summaries
#end textrank

def start_summarize(long_text, model, size):
  num_of_sentences = len(sent_tokenize(long_text))
  if num_of_sentences > 4:
    if model=="RankText":
      summary = textrank(long_text, size/100)
    elif model=="Bart":
      summary = "Sorry, we don't support Bart here. Please try summarize with Bart at the following link: https://huggingface.co/spaces/Moran/Aviv_Moran_Summarization . For more details aboute the model visit the model's card https://huggingface.co/Aviv/Moran_Aviv_Bart"
      # after one time running the next code, streamlit limits arcrossed, so  will mark this code as comments:
      # repo_id = "Aviv/Moran_Aviv_Bart"
      # inf_learn = from_pretrained_fastai(repo_id)  
      # summary = inf_learn.blurr_generate([long_text])[0]['generated_texts']
  else:
    summary = long_text
  st.success(summary)
  st.select_slider('What do you think about the summary?', options=['Bad', 'Good', 'Excellent'], value=('Good'))
#end start_summarize

st.title ("Text Summarization") 
model_type = st.radio('Pick a model',['RankText', 'Bart'])
textrank_summary_size = 0
if model_type=="RankText":
  textrank_summary_size = st.slider('How long would you like the summary to be? (Percentage of full text)', 5,50)
user_text = st.text_area('Enter or paste text to summarize') 
start = st.button('Summarize')#, on_click=start_summarize, args=(user_text, model_type,  ) )

if start:
  start = False
  st.markdown("Summary")
  with st.spinner("We are summarizing your text..."):
    start_summarize(user_text, model_type, textrank_summary_size)



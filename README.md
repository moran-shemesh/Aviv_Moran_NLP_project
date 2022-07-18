# Text Summarization
NLP final project - Moran Shemesh and Aviv Lazar

## Repo intro
There are two options for getting the original data: Kaggle and Google drive. The two options are the same. <br>
Data Repo - Kaggle: <br>
https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail <br>
Data Repo - google drive: <br>
https://drive.google.com/drive/folders/1UJRQbIEEOTwRxaCzbgphNFTjlxykEeSF?usp=sharing

Cleaned Data Repo: <br>
https://drive.google.com/drive/folders/1YiL61JCVwMQvRwQWcf0cAIyZfSWtmMJF?usp=sharing

IMPORTANT NOTE: for running the project locally, there is a need to create in “data” directory 2 new directories: “orig_data” and “clean_data”.
The original data files should be located in "orig_data" directory, and the cleaned data files in "clean_data".


## Installation | Requirements
See requirement file:
https://github.com/moran-shemesh/Aviv_Moran_NLP_project/blob/main/requirements.txt

## Quickstart
Try BART and TextRank on the App: <br>
https://huggingface.co/spaces/Moran/Aviv_Moran_Summarization

### In code: 
Note: Make sure you install first the libraries from requirements file. <br>
--> repo_id = "Aviv/Moran_Aviv_Bart" <br>
--> inf_learn = from_pretrained_fastai(repo_id) <br>
--> generated_summaries = inf_learn.blurr_generate(corpus)

You can also download our Bart model from HuggingFace: <br>
https://huggingface.co/Aviv/Moran_Aviv_Bart

And here you can find an example of using the model: <br>
https://github.com/moran-shemesh/Aviv_Moran_NLP_project/blob/main/experiments/Summarization_with_Blurr_notebook_3_Bart_streamlit.ipynb

## Resources


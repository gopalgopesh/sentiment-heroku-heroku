import streamlit as st
import pandas as pd 
from textblob import TextBlob

'# Twitter sentiment analysis'
text = st.text_input('Input your Tweet here:')

analysis = TextBlob(text)

if analysis.sentiment[0]>0:
	"## Tweet is Positive"
else:
	"## Tweet is Negative"
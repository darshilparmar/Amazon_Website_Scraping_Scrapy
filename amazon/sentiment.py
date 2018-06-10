import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import nltk
from nltk.corpus import stopwords 

amazon = pd.read_csv('amazon.csv')
print(amazon.head())

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

path=r'./data1.csv'
df=pd.read_csv(path)
a=df.iloc[,2:-2]

from os import listdir
from os.path import isfile, join
import pandas as pd

path = "news-topic-data/data/unigram/" 
array = [f for f in listdir(path) if isfile(join(path, f))]
diction = {}
for i in range(len(array)):
    path2 = array[i]
    array[i]= array[i].split(".")[0]
    df = pd.read_csv(f"{path}{path2}", encoding = "ISO-8859-1", header= None)
    diction[array[i]] = df

tokens = 'find your enemies where evil lies thou art heaven grafton'.split()

count_dict = {}
for key in diction.keys():
    count_dict[key] = 0

for token in tokens: 
    for key in diction.keys():
        if token in diction[key].values:
            count_dict[key] +=  diction[key].loc[diction[key][0] == token, 1].iloc[0]

df = pd.DataFrame.from_dict(count_dict, orient='index')
df = df.sort_values(by=0, ascending=False)
print(df.head())


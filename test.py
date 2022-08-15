
filename1 = {"hello": 123456, "abc": 1221}
#print(mydict["message"]['abc'])
values = filename1.values()
total = sum(values)
print(total)


#a = sum(mydict.values())
#print(a)

import os

docs_dict = {}

with os.scandir("txt/") as entries:
    for entry in entries:
        print(entry.name)
        with open("news-topic-data\\data\\unigram"+ entry.name ) as f:
          val = f.read()
          docs_dict[entry.name] = val
          f.close()
print(docs_dict)
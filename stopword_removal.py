# write your code here to remove stopwords from the book review(book11.txt)
from nltk.tokenize import RegexpTokenizer
nltk.download('stopwords')
with open('book1.txt','r') as fp:
  file = fp.read()
words = RegexpTokenizer(file,'\w+')
stop_words = set(stopwords.words('english'))
no_stopwords = [word for word in words if not word in stop_words]
with open('data.csv','w') as fp:
  for i in no_stopwords:
    fp.write(i)

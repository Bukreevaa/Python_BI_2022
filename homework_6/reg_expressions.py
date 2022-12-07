#moduls
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
#first task

ftp_file = open("ftp.txt", "w+")

for i in table:
    s = table[i].astype('str')
    res = s.str.findall(r'^ftp\..+')
    res = list(filter(None, res))
    for j in res:
        ftps = j[0].split(';')
        for k in range(len(ftps) - 1):
            ftp_file.write(ftps[k] + '\n')

ftp_file.close()

#second task

with open('/content/2430AD.txt', 'r') as f:
  all_num = []
  for line in f.readlines():
    num = re.findall(r'\d{1,}', line)
    if len(num) >= 1 :
      all_num.append(num)
print(all_num)

#third task
with open('/content/2430AD.txt', 'r') as f:
  a_words = []
  for line in f.readlines():
    words = re.findall(r'\b\w+?[a]\w+\b', line, flags=re.IGNORECASE)
    if len(words) >= 1:
      for word in words:
        a_words.append(word)

print(a_words)


#fourth task
with open('/content/2430AD.txt', 'r') as f:
  exclamation = []
  for line in f.readlines():
    exc= re.findall(r'[^\."]+!', line)
    if len(exc) >= 1:
       exclamation.append(exc[0])
print(exclamation)
#fifth task

with open('/content/2430AD.txt', 'r') as f:
  unix_word = {}
  for line in f.readlines():
    words = re.findall(r'[a-z]+?\b ', line, flags=re.IGNORECASE)
    for word in words:
      w = word.lower()
      w = w.rstrip()
      if w not in unix_word.keys():
        unix_word[w] = len(w)
table_words = pd.DataFrame(list(unix_word.items()),
                   columns=['word', 'lenght'])


sns.distplot(table_words['lenght'], hist=True, kde=False,
            color = 'blue',
             hist_kws={'edgecolor':'black'})
plt.title('Word length distribution')
plt.xlabel('words lenght')
plt.ylabel('count')


#sixth task

def brick_translator(filepath):
    translated_text = open('translated_text', 'w+')
    dct = {'а': 'ака',
           'о': 'око',
           'и': 'ики',
           "ы": "ыкы",
           "у": "уку",
           "э": "экэ",
           "я": "якя",
           "ю": "юкю",
           "ё": "ёкё",
           "е": "еке"}
    with open(filepath, 'r') as f:
        t_word = ''
        for line in f.readlines():
            words = re.findall(r'[а-я]+?\b', line, flags=re.IGNORECASE)

            for word in words:
                for j in word:
                    if j in dct.keys():
                        t_word += dct[j]
                    else:
                        t_word += j
                t_word += ' '
                translated_text.write(t_word + ' ')
        return t_word
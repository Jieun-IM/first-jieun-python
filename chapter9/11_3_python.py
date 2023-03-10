from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
text = 'python'
s_words = STOPWORDS.union({'one', 'using', 'first', 'two', 'make', 'use'})
wordcloud = WordCloud(width = 2000, height = 1500, stopwords = s_words).generate(text)
plt.figure(figsize=(40,30))
plt.imshow(wordcloud)
plt.show
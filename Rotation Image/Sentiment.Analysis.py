import csv
import matplotlib.pyplot as plt
import pandas as pd
import pprint as pp
import nltk

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
#from wordcloud import WordCloud


#nltk.download()





"""
Your code for part 1.
The idea is to make a list of positive and negative words from the lexicon files, 
and simply count the occurences of positive and negative words in the text. 
So in general, you should have the following steps:
1. Load the text
2. Load the lexicons
3. Count occurences
4. Plot histogram (make a reasonable size for the bins)

The following is a short script of loading the bb_2011_2013.csv file. Note that 
bb_2011_2013.csv and bb_1996_2013.csv is a little different.
	
	with open('data/bb/bb_2011_2013.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"')

"""

###################Text ########################################
# text = open('yelp.txt', encoding='utf-8').read()
# ltext = text.lower()
# text_token = word_tokenize(ltext)
#
# # text_distro = FreqDist()
# # for word in text_token:
# #     if word in neg_words:
# #         text_distro[word] += 1
# #
# # print(text_distro.keys())
#
# print(text_token)
# text_Freqdist = FreqDist()
# #print(text_distro.pformat(maxlen=100))
# # for character, value in text_distro.items():
# #     if character in neg_words:
# for entry in text_token:
#     if entry in neg_words or entry in pos_words:
#         text_Freqdist[entry] += 1
#
# print(text_Freqdist.keys())
# print(len(text_Freqdist))
# print(text_Freqdist.pformat(maxlen=100))
# plt.figure(figsize=(10, 5))
# text_Freqdist.plot(25, cumulative=False)


# for a in Occurance_list:
#     print(a)

# plt.figure(figsize=(10, 5))
# Occurance_list.plot(25, cumulative=False)


################# OCCURANCES #################################

Occurance_list = []

############################# bb file 1 #######################
# with open('bb_1996_2013.csv', 'r') as csvfile:
#     reader = csv.reader((csvfile), delimiter=',', quotechar='"')
#     # words = word_tokenize(reader)
#     # print(len(words))

############################### Negative lexicon words #####################
negative_list_short = []
string_neg_list = ""

with open('lexicon.finance.negative.csv', 'r') as newcsvfile:
    negative = csv.reader((newcsvfile), delimiter=',', quotechar='"')
    for row in negative:
        line = (" ".join(row))
        negative_list_short.append(line)

with open('lexicon.finance.negative.LoughranMcDonald.csv', 'r') as second_neglex:
    sec_neg = csv.reader((second_neglex), delimiter=',', quotechar='"')
    for i in sec_neg:
        line = (" ".join(i))
        negative_list_short.append(line)

with open('lexicon.generic.negative.HuLiu.csv', 'r') as third_neglex:
    third_neg = csv.reader((third_neglex), delimiter=',', quotechar='"')
    for x in third_neg:
        line = (" ".join(x))
        negative_list_short.append(line)


for entry in negative_list_short:
    string_neg_list = string_neg_list + " " + entry

neg_words = word_tokenize(string_neg_list)
#print(neg_words)
print("Length of neg words list: ", len(neg_words))
# neg_distro = FreqDist(neg_words)
# print(neg_distro.pformat(maxlen=1000))
# print(neg_distro.keys())

############################## Positive Lexicons #############################
positive_list_short = []
string_pos_list = ""

with open('lexicon.finance.positive.csv', 'r') as first_poslex:
    first_pos = csv.reader((first_poslex), delimiter=',', quotechar='"')
    for i in first_pos:
        line = (" ".join(i))
        positive_list_short.append(line)

with open('lexicon.finance.positive.LoughranMcDonald.csv', 'r') as second_poslex:
    sec_pos = csv.reader((second_poslex), delimiter=',', quotechar='"')
    for i in sec_pos:
        line = (" ".join(i))
        positive_list_short.append(line)

with open('lexicon.generic.positive.HuLiu.csv', 'r') as third_poslex:
    third_pos = csv.reader((third_poslex), delimiter=',', quotechar='"')
    for i in third_pos:
        line = (" ".join(i))
        positive_list_short.append(line)

for entry in positive_list_short:
    string_pos_list = string_pos_list + " " + entry

pos_words = word_tokenize(string_pos_list)
print("List of Positive words list: ", len(pos_words))

######################### First bb file ###################################

# bb1996_list = []
# with open('bb_1996_2013.csv', 'r', encoding='utf-8') as csvfinanceone:
#     bbreaderone = csv.reader(csvfinanceone)
#     for x in bbreaderone:
#         line = (" ".join(x))
#         bb1996_list.append(line)
#     string_bb1996 = ""
#     for newentry in bb1996_list:
#         string_bb1996 = string_bb1996 + newentry
#     sone = ""
#     sone = sone.join(string_bb1996)
#     lsone = sone.lower()
#
# #print(type(lsone))
# #print(lsone)
# sentences_1 = sent_tokenize(lsone)
# #print(sentences_1)
# #print(len(sentences_1))
# print()
# tok_word_one = word_tokenize(lsone)
# print("Total Number of Words: ", len(tok_word_one))
dist_word_one = FreqDist()
# for word in word_tokenize(lsone):
#     if word in pos_words or word in neg_words:
#         dist_word_one[word] += 1
#
# #print(dist_word_one.pformat(maxlen=100))
# print("Number of Unique Words: ", len(dist_word_one.keys()))
# #print(dist_word_one.keys())
# #plt.figure(figsize=(10, 5))
# #dist_word_one.plot(25, cumulative=False)


######################### Second bb file ################################

bb2011_list = []
with open('bb_2011_2013.csv', 'r') as csvfinance:
    bbreader = csv.reader(csvfinance)
    for a in bbreader:
        line = (" ".join(a))
        bb2011_list.append(line)
    string_bb2011 = ""
    for newentry in bb2011_list:
        string_bb2011 = string_bb2011 + newentry
    s = ""
    s = s.join(string_bb2011)
    ls = s.lower()

#print(type(ls))
#print(ls)
sentences = sent_tokenize(ls)
#print(sentences)
#print(len(sentences))
print()
tok_word = word_tokenize(ls)
print("Total Number of Words in Tokenized list tok_word: ", len(tok_word))
#dist_word = FreqDist()
for word in word_tokenize(ls):
    if word in pos_words or word in neg_words:
        dist_word_one[word] += 1

#print(dist_word_one.pformat(maxlen=100))
print("Number of Unique Words for FreqDist: ", len(dist_word_one.keys()))
#print(dist_word_one.keys())
#plt.figure(figsize=(10, 5))
#dist_word_one.plot(25, cumulative=False)



"""
Your code for part 2
Part 2 requires you to clean the text (remove stopwords/stemming) and make a 
word cloud out of it. Part 2 requires a little more packages to make it work:
	1. WordCloud 
	2. NLTK     (Natural Language Took Kit)  

Note that you can use different packages than those as long as it works, 
and if you do, please note that in your code


"""

print("Length of dist_word_one: ", len(dist_word_one))
for word, frequency in dist_word_one.most_common(50):
    print(u'{} : {}'.format(word,frequency))

stoplist = stopwords.words('english')
print("Length of stoplist", len(stoplist))
k = 50
top_k_list = []
for word, frequency in dist_word_one.most_common(k):
    top_k_list.append((u'{}'.format(word)))

new_stop_list = (set(top_k_list + stoplist))
print("Length of new stoplist", len(new_stop_list))
print()

dist_word_two = FreqDist()
four_or_more = []
four_stoplist = []

print(new_stop_list)
k = len(dist_word_one)
print("Length of dist_word_one length distribution: ", len(dist_word_one))
for word, frequency in dist_word_one.most_common(k):
    if len(word) > 3:
        four_or_more.append((u'{} : {}'.format(word, frequency)))
        four_stoplist.append(word)

print(four_or_more)
print(len(four_or_more))
print("Four_stoplist: ", four_stoplist)
print()
##### STEMMING ######

porter = PorterStemmer()
snowball = SnowballStemmer("english")
stemmed_words_one = [porter.stem(word) for word in four_stoplist]
print("Stemmed word list: ", stemmed_words_one)
print("Length of stemmed word list: ", len(stemmed_words_one))
stemmed_words_two = [snowball.stem(word) for word in four_stoplist]
print("Stemmed Snowball word list: ", stemmed_words_two)
print("Length of Snowball list: ", len(stemmed_words_two))


###### LEMATIZATION ############

wordnet_lem = WordNetLemmatizer()
lemmatized_words = [wordnet_lem.lemmatize(word, "v") for word in four_stoplist]
print("Lematized Words List: ", lemmatized_words)
print("Length of Lemmatized Words list: ", len(lemmatized_words))

########### PART OF SPEECH TAGGING ########





# #read stop words from file
# stopwords = []
#
#
#
#
#
#
# #Ignoring words that does not falls in ASCII code. Then tokenize them
# #You should pass all your text as ONE string to thie function
# unicode_text = nltk.tokenize.word_tokenize(unicode(whole_text, errors='ignore'))
#
# #Load stemmer, note that stemmer works word-by-word
# #so you should feed stemmer like  stemmer.stem(word)
# stemmer = SnowballStemmer("english")
#
#
#
#
# """
# The following code should work fine as long as you feed the stemmed_text variable correctly
# """
# #make wordcloud
# wc = WordCloud(background_color="white", max_words=2000, stopwords=stopwords)
# wc.generate(stemmed_text)
#
# #plot
# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.show()

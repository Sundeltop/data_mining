import csv
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt

with open('sms-spam-corpus.csv') as file:
    reader = csv.reader(file)
    headers = next(reader)
    ps = PorterStemmer()
    en_stops = set(stopwords.words('english'))
    ham_word_list = []
    spam_word_list = []
    ham_messages = []
    spam_messages = []
    for row in reader:
        row[1] = re.sub(r'[^\w\s]+|[\d]+', r'', row[1]).strip().lower()  # get rid of numbers and symbols
        for word in row[1].replace('. ', ' ').split():
            if word in en_stops:
                row[1] = row[1].replace(word, "")  # get rid of stop words
                row[1] = ' '.join(row[1].split())
        if row[0] == "ham":
            ham_messages.append(row[1])
            for word in re.sub(r'[^\w\s]+|[\d]+', r'', row[1]).strip().split():
                ham_word_list.append(word)
        else:
            spam_messages.append(row[1])
            for word in re.sub(r'[^\w\s]+|[\d]+', r'', row[1]).strip().split():
                spam_word_list.append(word)
        words = word_tokenize(row[1])
        for word in words:
            if len(word) <= 1:
                continue
        # print(ps.stem(word))  # stemming

    counter_ham = Counter(ham_word_list)
    counter_spam = Counter(spam_word_list)

    ham_file = open('output/ham_word_count.txt', 'w')
    for key, value in counter_ham.most_common():
        ham_file.write("{} {}\n".format(key, value))
    ham_file.close()

    spam_file = open('output/spam_word_count.txt', 'w')
    for key, value in counter_spam.most_common():
        spam_file.write("{} {}\n".format(key, value))
    spam_file.close()

    x, y = zip(*Counter(ham_word_list).most_common(20))
    plt.subplots(figsize=(15, 8))
    plt.plot(x, y)
    plt.title("ham words/count")
    plt.xlabel("words")
    plt.ylabel("count")
    plt.savefig("output/ham_words_count_plot.png")
    plt.show()

    x, y = zip(*Counter(spam_word_list).most_common(20))
    plt.subplots(figsize=(15, 8))
    plt.plot(x, y)
    plt.title("spam words/count")
    plt.xlabel("words")
    plt.ylabel("count")
    plt.savefig("output/spam_words_count_plot.png")
    plt.show()

    wordcount = {}
    for key in counter_ham.keys():
        length = len(key)
        if length not in wordcount:
            wordcount[length] = 1
        else:
            wordcount[length] += 1
    x, y = zip(*sorted(wordcount.items()))
    plt.subplots(figsize=(15, 8))
    plt.plot(x, y)
    plt.title("ham words quantity/length")
    plt.xlabel("word length\n Average length = " + str(sum(wordcount.keys()) / len(wordcount.keys())))
    plt.ylabel("word count")
    plt.savefig("output/ham_words_length_plot.png")
    plt.show()

    wordcount = {}
    for key in counter_spam.keys():
        length = len(key)
        if length not in wordcount:
            wordcount[length] = 1
        else:
            wordcount[length] += 1
    x, y = zip(*sorted(wordcount.items()))
    plt.subplots(figsize=(15, 8))
    plt.plot(x, y)
    plt.title("spam words quantity/length")
    plt.xlabel("word length\n Average length = " + str(sum(wordcount.keys()) / len(wordcount.keys())))
    plt.ylabel("word count")
    plt.savefig("output/spam_words_length_plot.png")
    plt.show()

    message_count = {}
    for message in ham_messages:
        length = len(message)
        if length not in message_count:
            message_count[length] = 1
        else:
            message_count[length] += 1
    x, y = zip(*sorted(message_count.items()))
    plt.subplots(figsize=(15, 8))
    plt.plot(x, y)
    plt.title("ham messages length/quantity")
    plt.xlabel("message length\n Average length = " + str(sum(message_count.keys()) / len(message_count.keys())))
    plt.ylabel("message count")
    plt.savefig("output/ham_messages_length_plot.png")
    plt.show()

    message_count = {}
    for message in spam_messages:
        length = len(message)
        if length not in message_count:
            message_count[length] = 1
        else:
            message_count[length] += 1
    x, y = zip(*sorted(message_count.items()))
    plt.subplots(figsize=(15, 8))
    plt.plot(x, y)
    plt.title("spam messages length/quantity")
    plt.xlabel("message length\n Average length = " + str(sum(message_count.keys()) / len(message_count.keys())))
    plt.ylabel("message count")
    plt.savefig("output/spam_messages_length_plot.png")
    plt.show()




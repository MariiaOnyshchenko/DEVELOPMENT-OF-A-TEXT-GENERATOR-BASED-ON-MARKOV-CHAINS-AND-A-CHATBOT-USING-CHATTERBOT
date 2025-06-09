import nltk
import chatterbot 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot_corpus
import logging
import re
import random
from collections import defaultdict

# my_file = open('carroll-alice.txt', 'r')
# text = my_file.read()
# print ('Онищенко Марія, 1 група, ЛР5')
# def markov(text):
#     word_list = text.split(' ')
#     word_dict = defaultdict(list)
#     for i in range (len(word_list)):
#         word_dict[word_list[i]].extend(word_list[(i+1):])
#     return word_dict 
# text = re.sub(r"[^a-zA-Zа-яА-ЯіІїЇєЄ0-9\s]", "", text)
# test_dict = markov(text.lower())
# # for word in test_dict:
# #     print (word, test_dict[word])

# def g_sentence(dictionary, count):
#     current = random.choice(list(dictionary.keys()))
#     sentence = current.capitalize()
#     for i in range (count - 1):
#         next_word = random.choice(dictionary[current])
#         sentence += ' ' + next_word
#         current = next_word
#     sentence += '.'
#     return sentence
# print(g_sentence(test_dict, int(input())))
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
german_bot = ChatBot(name ='IdkBot', read_only = True, \
                 logic_adapters =[
                                  'chatterbot.logic.BestMatch'
                            ])

corpus_trainer = ChatterBotCorpusTrainer(german_bot)
corpus_trainer.train('chatterbot.corpus.german')

print('Hallo! Ich bin Chatbot!')
for i in range(10):
    user_input = input()
    print(german_bot.get_response(user_input))    
    
    
    # small_talk = [
# 'Wie sieht es aus?',
# 'Was für ein Zufall!',
# 'Das ist großartig!',
# 'Schön für dich!',
# 'Und wie geht es dir?',
# 'Läuft alles gut?',
# 'Du wirst es nicht glauben!',
# 'Ich bin schließlich auch nur ein Mensch, schiebt die Schuld nicht auf mich.',
# 'Domo arigato mister robato!',
# 'Guten Tag!',
# 'Hallo!',
# 'Seid gegrüßt!',
# 'Was soll das denn?',
# 'Auf Wiedersehen!',
# 'Also dann.',
# 'Schrecklich.',
# 'Alles Gute!',
# 'Hilfe!' 
#     ]
# math_talk_0 = ['ich hasse Mathe', 'Es ist okay, einfach atmen. Chill.']

# math_talk_1 = ['die faktorielle Funktion', 
# '''Die faktorielle Funktion ist eine mathematische Funktion, 
# die durch ein Ausrufezeichen ! dargestellt wird. Die faktorielle Formel impliziert, dass 
# alle ganzen positiven Zahlen, die zwischen der genannten Zahl und 1 liegen, multipliziert 
# werden. Hier ist ein Beispiel: 7! = 1 * 2 * 3 * 4 * 5 * 6 * 7 = 5.040''']

# list_trainer = ListTrainer(my_bot)
# for i in (small_talk, math_talk_0, math_talk_1):
#     list_trainer.train(i)

# print('Hallo! Ich bin Chatbot!')
# for i in range(10):
#     user_input = input()
#     print(my_bot.get_response(user_input))

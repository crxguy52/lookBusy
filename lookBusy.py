from random import randrange, choice
import time

#Prints jibberish to make it look like cool things are happening

runtime = 10     #seconds
linemin = 7      #words
linemax = 10     #words
wordmin = 4      #chars
wordmax = 10     #chars
delaytime = 0.03 #seconds
lines = int(runtime/delaytime)

#only use lowercase letters
letters = 'abcdefghijklmnopqrstuvwxyz'

#print some lines
for i in range(lines):
    #print some words
    line = ''
    for j in range(randrange(wordmin,wordmax)):
        #build a word and print it
        word = ''
        for k in range(randrange(wordmin, wordmax)):
            word += choice(letters)
        line += word + ' '
    print(line)
    #Wait a random time between 0 and 2*delaytime
    dly = randrange(0, int(2*delaytime*10000))/10000.0
    time.sleep(dly)

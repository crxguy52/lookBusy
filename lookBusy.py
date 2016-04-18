from random import randrange, choice
import time

#Prints jibberish to make it look like cool things are happening

runtime = 20     #seconds
linemin = 7      #words
linemax = 10     #words
wordmin = 4      #chars
wordmax = 10     #chars
delaytime = 0.03 #seconds
lines = int(runtime/delaytime)

#only use lowercase letters
letters = 'abcdefghijklmnopqrstuvwxyz'

#generate a bunch of lines
for i in range(lines):
    #generate one line
    line = ''
    
    #generate words for one line
    for j in range(randrange(wordmin,wordmax)):
        word = ''
        
        #build one word and add it to the line        
        for k in range(randrange(wordmin, wordmax)):
            word += choice(letters)
        line += word + ' '
        
    #print the line
    print(line)
    
    #Wait a random time between 0 and 2*delaytime, then loop
    dly = randrange(0, int(2*delaytime*10000))/10000.0
    time.sleep(dly)

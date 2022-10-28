#
#File:
#Author: Dadiso Chitengwa
#
#Created: 10/07/22
#Modified: 10/07/22

infile = open("crosswords.txt", "r")

w = []
e_list= []

for line in infile: 
    word = line[:len(line)-1] # remove the newline character '\n' at the end of each line
    #print(word)
    w.append(word)
infile.close()

def no_e(letter):
    count = 0
    
    for char in w:        
        if 'e' not in char:
            count += 1
            e_list.append(char)
    #print(e_list)

            longest_word =  max(e_list, key=len)
            shortest_word =  min(e_list, key=len)

    print("In the official list of 113,809 crosswords, there are " + str(count) + " words that do not have 'e'.")
    #print(e_list)
    print('The shortest such word is' + shortest_word + ', and the longest such word is ' + longest_word)

no_e(w)    


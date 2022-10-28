#
#File:
#Author: Dadiso Chitengwa
#
#Created: 10/07/22
#Modified: 10/07/22

infile = open("crosswords.txt", "r")

w = []
palin_list =[]

for line in infile: 
    word = line[:len(line)-1] # remove the newline character '\n' at the end of each line
    #print(word)
    w.append(word)
infile.close()

def isPalindrome(pali):
    count = 0
    #max = 0
    #min = 0
    
    for pali in w:
        if pali == pali[::-1]:
            count += 1
            palin_list.append(pali)

            longest_word =  max(palin_list, key=len)
            shortest_word =  min(palin_list, key=len)

    '''for minmax in palin_list:
        len_minmax = int(len(minmax))
        if len_minmax > max:
            max = pali
        elif len_minmax < min:
            min = pali
         '''   
    print('In the official list of 113,809 crosswords, there are ' + str(count)+ ' palindromes')
    #print(pali)
    print('The longest word is ' + longest_word)
    print('The shortest word is ' + shortest_word) 
    #print(type(len(pali)))
    
isPalindrome(w)

   
        
        
    

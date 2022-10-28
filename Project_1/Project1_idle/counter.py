from collections import Counter

infile = open("crosswords.txt", "r")

w = []
e_list= []

for line in infile: 
    word = line[:len(line)-1] # remove the newline character '\n' at the end of each line
    #print(word)
    w.append(word)
infile.close()

x = Counter(w)
print(x)


    
    

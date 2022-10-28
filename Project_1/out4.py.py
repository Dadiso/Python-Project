#
#File:
#Author: Dadiso Chitengwa
#
#Created: 10/07/22
#Modified: 10/07/22

infile = open("crosswords.txt", "r")

w = []
d = {}
max = 0

for line in infile: 
    word = line[:len(line)-1] # remove the newline character '\n' at the end of each line
    #print(word)
    w.append(word)
infile.close()

for i in range(97,123):
    d[chr(i)] = 0


for words in w:
    #for letter in w:
        #d[letter] += 1
    fc = words[0]
    d[fc] += 1
#print(d)

print('In the official list of 113,809 crosswords,')
for l in d:
    print(str(d[l]) + ' words begin with ' + str(l) + ',')
    if int(d[l]) > max:
        max = d[l]
print('and ' + str(max) + ' is the most frequently used first letter.')









    
    

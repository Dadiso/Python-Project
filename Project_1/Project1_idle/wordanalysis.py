#
#File:
#Author: Dadiso Chitengwa
#
#Created: 10/07/22
#Modified: 10/07/22

infile = open("crosswords.txt", "r")

for line in infile: 
    word = line[:len(line)-1] # remove the newline character '\n' at the end of each line
    print(word)

close(infile)

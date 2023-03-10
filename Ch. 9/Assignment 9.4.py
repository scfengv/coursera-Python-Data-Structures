# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# MySolution
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
counts = dict()
for line in fh:
    if line.startswith('From '):
        word = line.split()
        mail = word[1]
        counts[mail] = counts.get(mail,0)+1
    
        
bigcount = None
bigmail = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigmail = word
print(bigmail, bigcount)
# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# MySolution
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
counts = dict()
ti = list()
for line in fh:
    if line.startswith('From '):
        word = line.split()
        time = word[5]
        hrs = time.split(':')
        hr = hrs[0]
        counts[hr] = counts.get(hr,0)+1
    #print(counts)
for (k,v) in counts.items():
    ti.append((k,v))
    ti = sorted(ti)
#print(ti)
for (key, val) in ti:
    print(key, val)
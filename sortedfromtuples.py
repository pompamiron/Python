#Chalakorn Manopirom // read and sorted keyword from file

# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

#   From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008


# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
handle = open(name)
count = dict()

for line in handle:
    if line.startswith('From '): 
        line = line.strip()
        line2 = line.split()
        word = line2[5]

        word2 = word.split(":")
        word3 = word2[0]
        
        count[word3] = count.get(word3,0) + 1
        
tmp = list()        

for a,b in count.items():
    new = (a,b)
    tmp.append(new)
    
tmp = sorted(tmp, reverse=False)

for b,a in tmp:
    print(b,a)

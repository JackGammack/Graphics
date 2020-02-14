import re
bookfile = open("Alice.txt","r")
allwords = open("allwords.txt","w")
unique = open("uniquewords.txt","w")
unique_dict = {}
freqs_dict = {}
pattern = re.compile("[a-z]+")

for line in bookfile:
    line = line.lower().split()
    for word in line:
        if( pattern.fullmatch(word) ):
            allwords.write(word + "\n")
            if( word in unique_dict ):
                unique_dict[word] += 1
            else:
                unique.write(word + "\n")
                unique_dict[word] = 1
        else:
            line.remove(word)
            
for frequency in unique_dict.values():
    if( frequency in freqs_dict ):
        freqs_dict[frequency] += 1
    else:
        freqs_dict[frequency] = 1
        
freqs = open("wordfrequency.txt","w")
max_key = max(freqs_dict.keys())

for key in range(1,max_key+1):
    if( key in freqs_dict ):
        new_line = str(key) + ": " + str(freqs_dict[key]) + "\n"
        freqs.write(new_line)

bookfile.close()
allwords.close()
unique.close()
freqs.close()

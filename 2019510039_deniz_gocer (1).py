import requests
from bs4 import BeautifulSoup

##I asked how many words you want to see.
wordlimit=int(input("Give me a number: "))
##deleted stop words
stopWords = [".", "," ,""," ",";", "'", "-", ":", "/", "!", "+","(", ")", "=", "?", "%", "&", "*", "<", ">" ,"#", "|","{", "}", "$",
                 "ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out",
                 "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into",
                 "of", "most", "itself", "other", "off", "is", "am", "or", "who", "as", "from", "him", "each", "the", "themselves",
                 "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more",
                 "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she",
                 "all", "no", "when", "at", "any", "before", "them", "same", "and", "been","have", "in", "will", "on", "does",
                 "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under",
                 "he", "you", "herself", "has", "jus ", "where", "too", "only", "myself", "which", "those", "i", "after", "few",
                 "whom", "being" , "if", "theirs", "my", "against", "a", "by",  "doing", "it", "how", "further", "was", "here", "than", "the" ,"b"]


##to delete words of one length
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]



def getData1():
    ##I asked book name
    bookName1 = str(input("Please enter a book name: "))
    ##I pulled data as html from the internet
    r = requests.get("https://en.wikibooks.org/wiki/" + bookName1 + "/Print_version")  
    soup = BeautifulSoup(r.content, 'html.parser')
    ##html printing codes
    list_1 = ["h1",'p',"ul","ol","br","dd","dt","b","h2","i","tt","cite","em","strong", "h3", "h4", "h5", "h6", "span", "pre", "code","div"]

    file1 = open("book1.txt", "w")
    ##call the parts on the site according to the codes on the list
    for j in list_1:
        try:
            content = soup.findAll(j)
            for i in content:
                file1.write(i.text)
        except:
            pass

    file1.close()

def countWords1():
    file = open("book1.txt", "r")
    lines = file.readlines()
    file.close()
    
    wordData = {}
    ##We call all the lines one by one, if not in the "word data" dictionary, we start with a value of 1, if there is, we increase the value by 1.
    for line in lines:
        wordsInLine = line.split(" ")
        if (line.strip() == ""):
            continue
        for word in wordsInLine:
            word = cleanWord(word)
            if not (word in stopWords):

                if (word in wordData.keys()):
                    wordCount = wordData[word]
                    wordData[word] = wordCount + 1    
                else:
                    wordData[word] = 1

    return wordData
    
##we list the words in the text from high to low
def sortDictionary(dict):
    values = sorted(dict.values(), reverse=True)

    newDict = {}

    for val in values:
        for key in dict.keys():
            if dict[key] == val:
                newDict[key] = dict[key]
    
    return newDict

##In text, if one of the letters in the alphabet sequence is present, we delete it.
def cleanWord(word):
    newWord = ""
    for char in word.lower():
        if char not in alphabet:
            pass
        else:
            newWord += char
    return newWord


getData1()
result = sortDictionary(countWords1())

count = 1

##sorts as many words as the word limit the user has entered, from high to low
print("No   word         count")
for word in result.keys():
    if (count <= wordlimit):
        print(f"{count}   {word}    {result[word]}")

    count += 1






##for2.book


print()
##deleted stop words
stopWords = [".", "," ,""," ",";", "'", "-", ":", "/", "!", "+","(", ")", "=", "?", "%", "&", "*", "<", ">" ,"#", "|","{", "}", "$",
                 "ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out",
                 "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into",
                 "of", "most", "itself", "other", "off", "is", "am", "or", "who", "as", "from", "him", "each", "the", "themselves",
                 "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more",
                 "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she",
                 "all", "no", "when", "at", "any", "before", "them", "same", "and", "been","have", "in", "will", "on", "does",
                 "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under",
                 "he", "you", "herself", "has", "jus ", "where", "too", "only", "myself", "which", "those", "i", "after", "few",
                 "whom", "being" , "if", "theirs", "my", "against", "a", "by",  "doing", "it", "how", "further", "was", "here", "than", "the","b" ]

##to delete words of one length
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]



def getData2():
    ##I asked book name
    bookName2 = str(input("Please enter a second book name: "))
    ##I pulled data as html from the internet
    r = requests.get("https://en.wikibooks.org/wiki/" + bookName2 + "/Print_version")

    soup = BeautifulSoup(r.content, 'html.parser')
    ##html printing codes
    list_2 = ["h1",'p',"ul","ol","br","dd","dt","b","h2","i","tt","cite","em","strong", "h3", "h4", "h5", "h6", "span", "pre", "code","div"]

    file2 = open("book2.txt", "w")
    ##call the parts on the site according to the codes on the list
    for j in list_2:
        try:
            content = soup.findAll(j)
            for i in content:
                file2.write(i.text)
        except:
            pass

    file2.close()


def countWords2():
    file2 = open("book2.txt", "r")
    lines = file2.readlines()
    file2.close()

    

    wordData = {}

    ## call all the lines one by one, if not in the "word data" dictionary, we start with a value of 1, if there is, we increase the value by 1.
    for line in lines:
        wordsInLine = line.split(" ")
        if (line.strip() == ""):
            continue
        for word in wordsInLine:
            word = cleanWord(word)
            if not (word in stopWords):

                if (word in wordData.keys()):
                    wordCount = wordData[word]
                    wordData[word] = wordCount + 1    
                else:
                    wordData[word] = 1

    return wordData
    
##we list the words in the text from high to low
def sortDictionary(dict):
    values = sorted(dict.values(), reverse=True)

    newDict = {}

    for val in values:
        for key in dict.keys():
            if dict[key] == val:
                newDict[key] = dict[key]
    
    return newDict

##In text, if one of the letters in the alphabet sequence is present, we delete it.
def cleanWord(word):
    newWord = ""
    for char in word.lower():
        if char not in alphabet:
            pass
        else:
            newWord += char
    return newWord


getData2()


result = sortDictionary(countWords2())

count = 1

##sorts as many words as the word limit the user has entered, from high to low
print("No   word         count")
for word in result.keys():
    if (count <= wordlimit):
        print(f"{count}   {word}    {result[word]}")

    count += 1
    

dictbook2=countWords2()
dictbook1=countWords1()
##sorts and prints in descending order according to the sum of the words common to both
dictsame={}
for i in dictbook1:
    if i in dictbook2:
        dictsame[i]=dictbook1[i]+dictbook2[i]
sameword=list(dictsame.values())
sameword.sort()
sameword.reverse()
controller=0
no_repeat=[]
print()
print("NO WORD FREQ_1 FREQ_2 FREQ_SUM")
for i in sameword:
    for j in dictsame:
        if dictsame[j] == i:
            if controller==wordlimit:
                break
            if not j in no_repeat:
                print(controller+1,j,dictbook1[j],dictbook2[j], dictsame[j])
                controller += 1
                no_repeat.append(j)

##finds the words in the first book that are not in the second book, sorts them in ascending order and prints them                
distictword1={}
print()
print("Distict Words")
print("NO WORD FREQ_1")
for i in dictbook1:
    if not i in dictbook2:
        distictword1[i]=dictbook1[i]
disctictbook1=list(distictword1.values())

disctictbook1.sort()
disctictbook1.reverse()
controller=0
no_repeat=[]
for i in disctictbook1:
    for j in distictword1:
        if distictword1[j] == i:
            if controller==wordlimit:
                break
            if not j in no_repeat:
                print(controller+1,j,distictword1[j])
                controller += 1
                no_repeat.append(j)
                
##finds the words in the second book that are not in the first book, sorts them in ascending order and prints them                
distictword2 ={}
print()
print("Distict Words")
print("NO WORD FREQ_2")
for i in dictbook2:
    if not i in dictbook1:
        distictword2[i]=dictbook2[i]
disctictbook2=list(distictword2.values())

disctictbook2.sort()
disctictbook2.reverse()
controller=0
no_repeat=[]
for i in disctictbook2:
    for j in distictword2:
        if distictword2[j] == i:
            if controller==wordlimit:
                break
            if not j in no_repeat:
                print(controller+1,j,distictword2[j])
                controller+=1
                no_repeat.append(j)
print()

       

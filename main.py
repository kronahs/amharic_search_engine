import re
import suffix
import plural
import prefix
import Lexical_analyzer
import Dictionary

def LexicalAnalysis(words):
    wordList=[]
    for word in words:
        if Lexical_analyzer.lexAnalyze(word)  != ' ':
            wordList.append(Lexical_analyzer.lexAnalyze(word))
    return wordList
#table Lookup   =============================================================
def tableLookup(input):
    stemmed,NotStemmed=Dictionary.TableLookUpStemmer(input)
    return stemmed,NotStemmed
#prefix removal =============================================================
def PrefixRemoval(wordList):
    prefixRemoved=[]
    for word in wordList:
        newWord=prefix.prefix(word)
        prefixRemoved.append(newWord)
    return prefixRemoved
#Post fix removal=============================================================    
def postfixRemoval(prefixRemoved):
     postfixRemoved=[]
     for word in prefixRemoved:
        newWord= plural.plural(word)
        postfixRemoved.append(newWord)
     return postfixRemoved
#suffix Removal=================================================================
def suffixremoval(postfixRemoved):
    stem=[]
    for word in postfixRemoved:
        newWord=word = suffix.suffix(word)
        stem.append(newWord)
    return stem    
   
   
    






def stemmer(input):
    words=input.split()
    #comma issue
    wordList=LexicalAnalysis(words)
    print(wordList)
    stemmed,NotStemmed=tableLookup(wordList)
    prefixRemoved=PrefixRemoval(NotStemmed)
    postfixRemoved=postfixRemoval(prefixRemoved)
    laterstem=suffixremoval(postfixRemoved)
    stemmed.extend(laterstem)
    return stemmed


'''stemmer("ዛሬ በጣም ጥሩ ቀን ነው ፣ ስለሆነም እኔ ወደ ጎን ለመጫወት ነው።")'''
'''stemmer('ለረዥም')'''
#print(stemmer('ዛሬ በጣም ጥሩ ቀን ነው ፣ ከወንድሞቼ ጋር ስለምጫወት'))

"ፖሊሶቹ,ፖሊሲዎቻችን,ፍልሚያ,ይፈፅም"
#print(stemmer("በተለያዩ ከፍተኛ ትምህርት ተቋማት ውስጥ የሚገኙና የመውጫ ፈተና የወሰዱ የ \" መካኒካል ምህንድስና \" የትምህርት ዘርፍ ተማሪዎች በተፈተኑት የፈተና ይዘት ላይ ቅሬታ እንዳላቸው ለቲክቫህ ኢትዮጵያ በላኩት መልእክት አሳውቁ።"))
print(stemmer('ቲክቫህ ኢትዮጵያ ባለፉት ቀናት በመቶዎች የሚቆጠሩ ተማሪዎችን ጥያቄ እና ቅሬታ የተቀበለ ሲሆን ተማሪዎቹ ምንም እንኳን የትምህርት ሚኒስቴር ብቁ ዜጋን ከማፍራት አንጻር እና የትት ጥራትን ለማሻሻል እየተገበረ ያለውን የመውጫ ፈተና የሚደግፉት ቢሆን የተፈተኑት የፈተና ይዘት ከተነገራቸው መመዘኛ ነው ተብሎ ከቀረበው ሀሳብ ጋር የማይገጥም መሆኑን ገልጸዋል።'))






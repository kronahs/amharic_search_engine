suffix_set = ["ዎች", 'ውን','ውያን', "ች", "ን", 'ም','ሽ','ህ',"ዎ","ይ","ው","ት"]
letter_set = {"ሁ": "ህ","ሉ": "ል","ሑ": "ሕ","ሙ": "ም","ሡ": "ሥ","ሩ": "ር","ሱ": "ስ","ሹ": "ሽ","ቁ": "ቅ","ቡ": "ብ","ቩ": "ቭ",
              "ቱ": "ት","ቹ": "ች","ኁ": "ኅ","ኑ": "ን","ኙ": "ኝ","ኡ": "እ","ኩ": "ክ","ኹ": "ኽ","ዉ": "ው","ዑ": "ዕ","ዙ": "ዝ","ዡ": "ዥ",
              "ዩ": "ይ","ዱ": "ድ","ጁ": "ጅ","ጉ": "ግ","ጡ": "ጥ","ጩ": "ጭ","ጱ": "ጵ","ጹ": "ጽ","ፁ": "ፅ","ፉ": "ፍ","ፑ": "ፕ"
            }

def suffix(input):
    input = str(input)
    if input.endswith('ን'):
        letter = input[input.__len__() - 2]
        for word in letter_set:
            if word == letter:
                input = input[:-1]
                input = input[:len(input)-1] + letter_set.get(word) + input[len(input)+1:]

    for suffix in suffix_set:
        if input.endswith(suffix) and len(input)>3:
            input = input.removesuffix(suffix)
    
    return input
print(suffix('ተለያዩ'))
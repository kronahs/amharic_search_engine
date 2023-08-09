plural_set = {"ሆ": "ህ","ሎ": "ል","ሖ": "ሕ","ሞ": "ም","ሦ": "ሥ","ሮ": "ር","ሶ": "ስ","ሾ": "ሽ","ቆ": "ቅ","ቦ": "ብ",
              "ቮ": "ቭ","ቶ": "ት","ቾ": "ች","ኆ": "ኅ","ኖ": "ን","ኞ": "ኝ","ኦ": "እ","ኮ": "ክ","ኾ": "ኽ","ዎ": "ው","ዖ": "ዕ","ዞ": "ዝ",
              "ዦ": "ዥ","ዮ": "ይ","ዶ": "ድ","ጆ": "ጅ","ጎ": "ግ","ጦ": "ጥ","ጮ": "ጭ","ጶ": "ጵ","ጾ": "ጽ","ፆ": "ፅ","ፎ": "ፍ",
              "ፖ": "ፕ"}

def plural(input):
    input = str(input)
    if input.endswith("ዎች"):
        input = input[:-2]           
    elif input.endswith("ች"):
        input = input[:-1]
        
        for plural in plural_set:
            if input.endswith(plural) and len(input)>3:
                input = input[:len(input)-1] + plural_set.get(plural) + input[len(input)+1:]
    
    return(input)

print(plural('ተለያዩ'))


'''what should be done here is that according to the number of elements it loops checking the last element for it to not be in this array'''
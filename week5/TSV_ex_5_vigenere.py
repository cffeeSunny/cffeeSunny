import itertools
import string
def vigenere_encrypt (message: str, key:str) -> str:
    message1=list(message.lower())
    key1=list(key.lower())
    diction_vig = {"a" : 0 ,"b" : 1 , "c":2 ,"d": 3 ,  "e" : 4, "f" : 5 ,"g ":6 ," h" :7,"i ": 8,"j ": 9,"k " :10 ,"l " :11,"m ":12 ,"n ":13 ,"o ":14 ,"p "  : 15,"q ": 16,"r " :17,"s " :18,"t " :19,"u " :20,"v " :21,"w " :22,"x " :23,"y ":24, "z ":25}
    dict_vig_2 = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}
    message2 = []
    key2 = []
    for i in message1:
        message2.append(diction_vig.get(i))
    for i in key1:
        key2.append(diction_vig.get(i))
    result1 =[]
    for m, k in  zip(message2,itertools.cycle(key2)):
        result1.append((m+k) % 26)
    result2 = []
    for i in result2:
        result2.append(dict_vig_2.get(i))
    s=""
    return (s.join(result2))


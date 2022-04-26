
dictionary = {
    'teispt_pi' : 10,
    'ptesit1_pi' : 12
    }

dictMsg = {}

for k,v in dictionary.items():
    msgKey = str(k).strip('_pi')
    msgValue = dictionary[k]
    dictMsg[msgKey] = msgValue

print(dictMsg) 



    



    
#print(dictionary)
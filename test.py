from PyDictionary import PyDictionary


dictionary = PyDictionary()

test = dictionary.meaning('time')
print(dictionary.synonym('life'))


for n in  test.items():
    print(n[0] +'->'+ n[1][0])
# def remove_vowel(word):
#     vowel = ['a','e','i','o','u']
#     s = ""
#     for letter in word:
#         if letter not in vowel:
#             s  += letter
#     print(s) 


# def remove_vowel(word):
#     word = [print(s) for s in word if s not in ['a','e','i','o','u']] 
     
remove_vowel = lambda word: [print(s) for s in word if s not in ['a','e','i','o','u']]




word = 'akashoy'
remove_vowel(word)
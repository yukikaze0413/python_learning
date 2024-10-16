def emoji_converter(words):
 words = words.split()
 output = ""
 dictionary = {
    ":)" : "😊",
    ":D" : "😀",
    ":(" : "😔",
     ":|" : "😐",
     ":*" : "😗",
     ";)" : "😉",
 }
 for word in words:
    output += dictionary.get(word, word) + " "
 return output

word = input("Enter a sentence: ")
print(emoji_converter(word))

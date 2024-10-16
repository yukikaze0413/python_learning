words = input("Enter the words: ")
words = words.split()
output = ""
dictionary = {
    ":)" : "😊",
    ":D" : "😀",
    ":(" : "😔",
}
for word in words:
    output += dictionary.get(word, word) + " "
print(output)
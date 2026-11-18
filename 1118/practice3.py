# 실습
word = "NORMAL-WARNING-NORMAL-ERROR-WARNING"

# 1
print("WARNING #:", word.count("WARNING"))

#2
print("NORMAL #:", word.count("NORMAL"))

#3
print("ERROR #:", word.count("ERROR"))

#4
print("first 'WARNING' appearance index:", word.find("WARNING"))

#5
print("second 'WARNING' appearance index:", word.find("WARNING",word.find("WARNING")+1))

#6
print("the words between two 'WARNING's:",word[7+len("WARNING"):28])

#7
print("if the word 'ERROR' is in between:","ERROR"in(word[14:28]))
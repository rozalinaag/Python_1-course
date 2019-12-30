import string
punct=input()
punct="".join(i for i in punct if i not in string.punctuation)
print(punct)

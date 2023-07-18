import string

sentence ="how are you ?"
for i in sentence:
    if i in string.whitespace:
        print("printable a=value is :"+i)
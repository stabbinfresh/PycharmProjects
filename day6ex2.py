file = open('essay.txt', 'r')
text = file.read()
file.close()
print(len(text))
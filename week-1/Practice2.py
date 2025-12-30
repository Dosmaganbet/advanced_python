text = input("Введите текст: ")
words= text.split()
count = 0 

for word in words:
    if word.lower().startswith('е'): 
        count = count + 1    

print(count) 
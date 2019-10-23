word="abcd"

for item in enumerate(word): #it will simply output the elemnts of the index and the index number according to the index
    print(item)

    #or just

    for index,letter in enumerate(word):
        print(index)
        print(letter)
        print('\n')
"""Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово
в этом тексте и через пробел то, сколько раз оно встретилось. 
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк)."""


with open('dataset_3363_3.txt') as inf, open('MostPopularWord.txt','w') as ouf:
    maxc = 0
    s = inf.read().lower().strip().split() #strip() - удаляет все знаки припинания, включая \n 
    s.sort()
    for word in s:
        counter = s.count(word)
        if counter > maxc:
            maxc = counter
            result_word = word
    ouf.write(result_word +' ' + str(maxc))

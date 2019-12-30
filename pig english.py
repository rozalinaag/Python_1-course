def pigify(word):
    upp=0
    if word[0]==(word[0]).upper():
        upp=1
    
    const=['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    vowel=['e','y','u','i','o','a']
    vhodinconst=0
    vhodinvowel=0
    firstconst=''
    firstlowel=''
    indx=0
    for i in range(len(word)):
        letter=word[i]
        
        if letter.lower() in const:
            vhodinconst=1
            if vhodinvowel==0:
                firstconst+=letter.lower()
                indx+=1
            else:
                break
        elif letter.lower() in vowel:
            vhodinvowel=1
            if vhodinconst==0:
                firstlowel+=letter.lower()
                indx+=1
            else:
                break
    thnak=''
    newsreth=''
    newword=''
    if word[-1]==',' or word[-1]=='.' or word[-1]=='!' or word[-1]=='?':
        thnak=word[-1]
    if firstconst!='' and firstlowel=='':
        if thnak=='':
            newsreth=word[indx:len(word)]
        else:
            newsreth=word[indx:len(word)-1]
        if upp==1:
            newword=newsreth[0].upper()+newsreth[1:len(newsreth)]+firstconst+'ay'+thnak
        else:
            newword=newsreth+firstconst+'ay'+thnak
    elif firstlowel!='':
        if thnak=='':
            newsreth=word
        else:
            newsreth=word[0:len(word)-1]
        newword=newsreth+'way'+thnak
    if newword=='':
        newword=word
            
    print(newword)
  


pigify("in!")

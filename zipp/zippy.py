def dictionary_crack_zip(file,dicty):
    from zipfile import ZipFile
    
    def passw(dicty):
        for parol in dicty:
            passwd=(parol.replace('\n','')).lower()
            archiv.setpassword(passwd.encode())
            try:
                archiv.extractall()
            except:
                p=1
            else:
                yield passwd 
    with open(dicty,errors='ignore') as dicty:
        with ZipFile(file) as archiv:
            for password in passw(dicty):
                return password
 
    
lob=dictionary_crack_zip("foopl.zip", "dic.txt")
print(lob)

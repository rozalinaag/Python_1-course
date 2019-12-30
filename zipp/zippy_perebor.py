from itertools import product
def brute_crack_zip(file):
    from zipfile import ZipFile
    def passw(chars):
        k=0
        for i in range(1,9):
            pwds=product(chars,repeat=i)
            for parol in pwds:
                klop=''
                for j in range(i):
                    klop+=parol[j]
                passwd=(klop.replace('\n','')).lower()
                archiv.setpassword(passwd.encode())
                try:
                    archiv.extractall()
                except:
                    p=1
                else:
                    yield passwd
                k+=1
                if k%1000000==0:
                    print(passwd)
    chars="qwertyuiopasdfghjklzxcvbnm0123456789"
    with ZipFile(file) as archiv:
        for password in passw(chars):
            return password
print('parol=',brute_crack_zip("breakme2.zip"))


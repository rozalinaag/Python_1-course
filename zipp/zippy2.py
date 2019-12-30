from itertools import product
import threading
import time
patrik='1'
def brute_crack_zip(file):
    
    from zipfile import ZipFile
    def passw(chars):
        def tread(times,k,i,chars):
            global patrik
            pwds=product(chars,repeat=i)
            time.sleep(times)
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
                    
                    patrik = passwd
                    return passwd
                    #yield passwd; return
            
            archiv.setpassword(patrik.encode())
            try:
                archiv.extractall()
            except:
                p=1
            else:
                return patrik
        k=1000
        liss=[]
        t=threading.Thread(target=tread, name='loli{}'.format(1), args=(0,k,1,chars))
        t.start()
        liss.append(t)
        t=threading.Thread(target=tread, name='loli{}'.format(2), args=(0,k,2,chars))
        t.start()
        liss.append(t)

        t=threading.Thread(target=tread, name='loli{}'.format(3), args=(0,k,3,chars))
        t.start()
        liss.append(t)
        #t=threading.Thread(target=tread, name='loli{}'.format(4), args=(0,k,4,chars))
        #t.start()
        #liss.append(t)
        #t=threading.Thread(target=tread, name='loli{}'.format(5), args=(0,k,5,chars))
        #t.start()
        #liss.append(t)
        #t=threading.Thread(target=tread, name='loli{}'.format(6), args=(0,k,6,chars))
        #t.start()
        #liss.append(t)
        #t=threading.Thread(target=tread, name='loli{}'.format(7), args=(0,k,7,chars))
        #t.start()
        #liss.append(t)
        #t=threading.Thread(target=tread, name='loli{}'.format(8), args=(0,k,8,chars))
        #t.start()
        #liss.append(t)
    
        for t in liss:
            t.join()
    chars="qwertyuiopasdfghjklzxcvbnm0123456789"
    with ZipFile(file) as archiv:
        r=passw(chars)
    if patrik=='1':
        return 'not found'
    else:
        return patrik
print('parol=',brute_crack_zip("foope.zip"))






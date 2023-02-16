file = input('Masukkan lokasi dan nama file : ')
try : 
    xfile = open (file)
    for new in xfile :
        new = new.rstrip()
        if not new.startswith('from'):
            continue
        wfile = open('EmailFrom.txt','w')
        wfile.write(new)
        wfile.close()

except :
    print('File ' +file+ ' tidak ada di directory!! \ntry again!!')
    
    
'''
xfile = open (file)
for x in xfile :
    x = x.rstrip()
    if not x.startswith('from'):
        continue
    print(x)
'''  
'''
xfile = open (file)
readfile = xfile.read()
saring = readfile[0:966]

wfile = open ('EmailFrom.txt', 'w')
wfile.write(saring)
wfile.close()
'''
    
    
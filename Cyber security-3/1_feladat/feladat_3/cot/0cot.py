checkFileBin=['A'] #Ebbe a tömbbe tesszük be, hogy milyen sorrendbe olvassa a bin fájlokat
BadChecksum=''
for binName in checkFileBin:
    binName+=".bin"
    print(binName,end='\t')
    file=open(f'D:\Projects\VI_OITM-Cyber_Security\Cyber security-3\\1_feladat\\feladat_3\cot\{binName}',"rb")
    content=list(file.read())
    contentBytes=bytes(content)
    file.close()#fájlt 
    fileLength=len(content)
    checksum=0
    for x in range(fileLength-1):#utolsó elem (checksum) előttiig
        checksum=checksum+content[x]
    checksum=checksum&255
    if checksum ==content[fileLength-1]: #!=
        BadChecksum+=binName[0]+" "
    if content[0]:#első elem (pointer)
        checkFileBin.append(chr(content[0]))#Számból ASCII kóddá válik, majd a listához adja
print("\nHelytelen BIN: \n\t"+BadChecksum)
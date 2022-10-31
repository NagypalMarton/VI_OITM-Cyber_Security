checkFileBin=['A'] #Ebbe a tömbbe tesszük be, hogy milyen sorrendbe olvassa a bin fájlokat
BadChecksum=''
for binName in checkFileBin:
    binName+=".bin"
    print(binName,end='\t')
    bin=open(binName,"rb")
    number=list(bin.read())
    numberBytes=bytes(number)
    bin.close()#fájlt 
    binLength=len(number)
    binSUM=0
    for x in range(binLength-1):#utolsó elem (checksum) előttiig
        binSUM=binSUM+number[x]
    newChecksum=binSUM&255
    if newChecksum !=number[binLength-1]:
        BadChecksum+=binName+" "
    if number[0]:#első elem (pointer)
        checkFileBin.append(chr(number[0]))#Sámból ASCII kóddá válik, majd a listához adja
print("\nHelytelen BIN: \n\t"+BadChecksum)
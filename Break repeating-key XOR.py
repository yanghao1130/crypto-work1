import base64
def hamming(a, b):
    a1=''.join([bin(ord(i)).replace('0b', '').zfill(8) for i in a])
    b1=''.join([bin(ord(i)).replace('0b', '').zfill(8) for i in b])
    dis=0
    for i in range(len(a1)):
        if a1[i]!=b1[i]:
            dis+=1
    return dis

def grouping(arr,keylen,index):#分组
    listi=[]
    i=0
    while(1):
        if index+i*keylen <= len(arr)-1:
            listi.append(arr[index+i*keylen])
            i+=1
        else:
            break
    return listi

def keydecrypt(templist):
    visiable_chars=[]#字母+空格
    for x in range(65,91):
        visiable_chars.append(chr(x))
    for x in range(67,123):
        visiable_chars.append(chr(x))
    visiable_chars.append(' ')
    
    bestkey=0
    dismax=0
    for key in range(32,128):
        dis=0
        for i in range(len(templist)):
            if chr(key^ord(templist[i])) in visiable_chars:
                dis+=1
        if dis>dismax:
            dismax=dis
            bestkey=key
    return chr(bestkey)

def decrypt(arr,key,keysize):
    plaintext=[]
    key1=[]
    for i in range(len(key)):
        key1.append(ord(key[i]))
        
    for i in range(len(arr)):
        plaintext.append(chr(ord(arr[i])^int(key1[i%keysize])))
    return ''.join(plaintext)

#读取密文文本
f = open('decodetext.txt', 'r')
decstr=''
for line in f:
    line=line.replace('\n','')
    decstr=decstr+line
f.close()
decstr=str(base64.b64decode(decstr),"utf-8")

#根据题目计算可能的keysize大小
normalized_distances=[]
for keysize in range(2,41):
    str1=''
    str2=''
    str1=decstr[0:keysize]
    str2=decstr[keysize:2*keysize]
    str3=decstr[2*keysize:3*keysize]
    str4=decstr[3*keysize:4*keysize]
    disham=(hamming(str1,str2)+hamming(str1,str3)+hamming(str1,str4)+hamming(str2,str3)+hamming(str2,str4)+hamming(str3,str4))/6
    disham=disham/keysize
    normalized_distances.append((keysize,disham))
normalized_distances = sorted(normalized_distances,key=lambda x:x[1])
print(normalized_distances)

#解密密钥
keysize=normalized_distances[0][0]
key=''
for i in range(keysize):
    strlist=grouping(decstr,keysize,i)
    key=key+keydecrypt(strlist)
print("密钥为：" +key)
print("\n")

#用密钥解密密文
print(decrypt(decstr,key,keysize))

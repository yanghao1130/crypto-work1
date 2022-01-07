import string
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

def findkey(arr):#检测每位可能的密钥
    visiable_chars=[]#可见字符
    for x in range(32,47):
        visiable_chars.append(chr(x))
    for x in range(58,122):
        visiable_chars.append(chr(x))

     
    targetlist=[]
    templist=[]
    for key in range(0x00,0xFF):
        templist.append(key)
        for i in range(0,len(arr)):
            if chr(key^arr[i]) not in visiable_chars:
                templist.remove(key)
                break
    targetlist=templist
    return targetlist
        
def decrypt(arr,key):
    plaintext=[]
    key1=''
    for i in range(len(key)):
        key1=key1+chr(key[i])
    print(key1)
    for i in range(len(arr)):
        plaintext.append(chr(arr[i]^key[i%7]))
    return ''.join(plaintext)
decstr='F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923C\
AB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF\
5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84C\
C931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D96\
3FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47E\
FD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5\
923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA\
36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63C\
ED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A8\
5A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250\
C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794'
arr=[]
for x in range(0,len(decstr),2):
    arr.append(int(decstr[x:2+x],16))

for keylen in range(1,11):
    keylist=[]
    for key in range(0,keylen):
        templist=grouping(arr,keylen,key)
        keylist.append(findkey(templist))
    print(keylist)
keylist=[[186], [31], [144, 145], [176, 178, 179, 180, 181, 182, 183], [82, 83], [204, 205], [62, 63]]
for i0 in keylist[0]:
    for i1 in keylist[1]:
        for i2 in keylist[2]:
            for i3 in keylist[3]:
                for i4 in keylist[4]:
                    for i5 in keylist[5]:
                        for i6 in keylist[6]:
                            tempkey=[]
                            tempkey.append(i0)
                            tempkey.append(i1)
                            tempkey.append(i2)
                            tempkey.append(i3)
                            tempkey.append(i4)
                            tempkey.append(i5)
                            tempkey.append(i6)
                            print(decrypt(arr,tempkey))


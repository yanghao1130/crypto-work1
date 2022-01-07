import hashlib
import itertools
import time

start=time.time()
def sha1(res):
    sha = hashlib.sha1(res.encode('utf-8'))
    encrypts = sha.hexdigest()
    return encrypts

target='67ae1a64661ac8b4494666f58c4822408dd0a3e4'
str1="QqWw%58(=0Ii*+nN"
list1=[['Q', 'q'],[ 'W', 'w'],[ '%', '5'], ['8', '('],[ '=', '0'], ['I', 'i'], ['*', '+'], ['n', 'N']]
for keysize in range(8,9):
   str1=['','','','','','','','','','']
   for a in range(2):
       str1[0]=list1[0][a]
       for b in range(2):
           str1[1]=list1[1][b]
           for c in range(2):
               str1[2]=list1[2][c]
               for d in range(2):
                   str1[3]=list1[3][d]
                   for e in range(2):
                       str1[4]=list1[4][e]
                       for f in range(2):
                           str1[5]=list1[5][f]
                           for g in range(2):
                               str1[6]=list1[6][g]
                               for h in range(2):
                                   str1[7]=list1[7][h]
                                   str2=''.join(str1)
                                   for i in itertools.permutations(str2, 8):
                                        tempstr=''.join(i)
                                        if sha1(tempstr)==target:
                                            print(tempstr)
                                            
end=time.time()
print('Running time: %s Seconds'%(end-start))
        

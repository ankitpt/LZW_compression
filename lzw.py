import numpy as np
from PIL import Image


#mat= np.matrix('39 39 126 126;39 39 126 126;39 39 126 126;39 39 126 126 ')

im = Image.open('jaime.tiff')
shp=list(im.size)
#amat = np.asarray(mat).ravel()
amat = np.asarray(im).ravel()
dic={}
out=[]
k=0
tmp=256

for i in range(0,256):
    dic[str(i)]=i
    

p=str(amat[0])
amatn=amat[1:]

for i in amatn:
    
    c=str(i)
    new=p+'-'+c
    
    if new in dic:
        
        p=new
        
    else:
        
        out.append(dic[p])
        dic[new]=tmp
        tmp=tmp+1
    
        p=c
        
if p in dic:
    out.append(dic[p])

dic = {v: k for k, v in dic.iteritems()}

fin=list()
for i in out:
    
    tem=map(int,dic[i].split('-'))
    fin.extend(tem)

nfin=np.asarray(fin)
nfin.resize(shp[0],shp[1],4)

    



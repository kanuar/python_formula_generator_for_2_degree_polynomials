from numpy import linalg,matrix
print('input should be of the format "n tn"')
print('enter 0 0 to end input')
op,ip=[],[]
a,b=input().split()
a,b=int(a),int(b)
while ((a!=0) and (b!=0)):
    op+=[b]
    ip+=[[1,a,a*a]]
    a,b=input().split()
    a,b=int(a),int(b)
s=''
for i in op:
    s+=str(i)+' ;';
s=s[:-1]
op=matrix(s)
s=''
for i in ip:
    s+=str(i)+' ;';
s=s[:-1]
ip=matrix(s)
t=ip.getT()
th=linalg.pinv((t*ip))*t*op
h='n^2*'+str(th[2][0])+'+n*'+str(th[1][0])+'+'+str(th[0][0])
print(h)

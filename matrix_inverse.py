def occ2():
    mat = [0,0],[0,0]
    print(mat)
    for i in range (0,2):
      mat[i][0]=float(input("x"))
      mat[i][1]=float(input("y"))
    print(mat)
    return mat

def occ3():
    mat = [0,0,0],[0,0,0],[0,0,0]
    for i in range (0,3):
     mat[i][0]=float(input("x"))
     mat[i][1]=float(input("y"))
     mat[i][2]=float(input("z"))
    print(mat)
    return mat

def det2(mat):
    det2 = (mat[0][0]*mat[1][1])-(mat[0][1]*mat[1][0])
    return det2

def det3(mat):
    d=[0,0,0]
    for i in range (0,3):
            temp = mat
            mat = numpy.delete(mat,(0),axis = 0)
            mat = numpy.delete(mat,(i),axis = 1)
            detm = det2(mat)
            mat = temp
            d[i]=mat[0][i]*detm
    l=d[0]
    n=d[1]
    m=d[2]
    det3 = l-n+m
    if det3 == 0:
        print("singular")
    else:
        print(det3)
    return det3

def inv2(mat,det2):
    mat1 = [0,0],[0,0]
    mat1[0][0]=mat[1][1]
    mat1[1][1]=mat[0][0]
    mat1[0][1]=-1*mat[0][1]
    mat1[1][0]=-1*mat[1][0]
    for i in range (0,2):
        for ii in range (0,2):
          mat1[i][ii]=mat1[i][ii]*(1/det2)
    print(mat1)
    return mat1

def inv3(mat,det3):
    mat2 = [0,0,0],[0,0,0],[0,0,0]
    for i in range (0,3):
        for ii in range (0,3):
            temp = mat
            mat = numpy.delete(mat,(i),axis = 0)
            mat = numpy.delete(mat,(ii),axis = 1)
            detm = det2(mat)
            mat2[i][ii] = detm
            mat = temp
    for i in range (0,3):
        for ii in range (0,3):
             if (i + ii)%2 == 1:
                 mat2[i][ii]=mat2[i][ii] * -1
    mat3 = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range (0,3):
        for ii in range (0,3):
            mat3[i][ii]=float(mat2[ii][i])
    return mat3
    
def cc():
    c = [0,0]
    c[0] = float(input("c1"))
    c[1]= float(input("c"))
    return c

def ccc():
    c=[0,0,0]
    c[0]= float(input("c1"))
    c[1]= float(input("c2"))
    c[2]= float(input("c3"))
    return c

def multinvccc(mat4,c,det3):
    invdet = 1/det3
    l = [0,0,0]
    xyz = [0,0,0]
    for i in range (0,3):
        for ii in range (0,3):
            l[ii] = mat4[i][ii]*c[ii]
            print(l)
        xyz[i]=(l[0]+l[1]+l[2])*invdet
    print(xyz)
def multinvcc(mat1,c,det2):
    l = [0,0]
    xy=[0,0]
    for i in range (0,2):
        for ii in range (0,2):
            l[ii] = mat1[i][ii]*c[ii]
        xy[i]=l[0]+l[1]
    print(xy)
    
    
        
            
    
            
import numpy
n = input("dimensions?")
if n == "3x3":
       mat = occ3()
       det3 = det3(mat)
       mat4=inv3(mat,det3)
       c = ccc()
       multinvccc(mat4,c,det3)
elif n == "2x2":
       mat = occ2()
       det2 = det2(mat)
       mat1=inv2(mat,det2)
       c = cc()
       multinvcc(mat1,c,det2)
else:
       print("error")



k=input("press enter to exit")




















        
      
    

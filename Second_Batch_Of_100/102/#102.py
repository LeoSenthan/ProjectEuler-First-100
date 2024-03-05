with open("BONUS/102/#102.txt","r") as f:
    triangles=f.readlines()
count=0
def CheckTriangle(triangle):
    ax,ay,bx,by,cx,cy=map(int,triangle.split(","))
    #barycentric coordinates of origin to 3 points
    a=True if ax*by-ay*bx>0 else False
    b=True if bx*cy-by*cx>0 else False
    c=True if cx*ay-cy*ax>0 else False
    if a and b and c:
        return True
    elif a==False and b==False and c==False:
        return True
    return False
for triangle in triangles:
    if CheckTriangle(triangle):
        count+=1
print(count)

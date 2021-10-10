def operation_1(a,b,c):
    return (a+b*c)
def operation_2(a,b,c):
    return (a*2+b)
def operation_3(a,b,c):
    return (c*3-b)
i=5
j=1
k=2
resultat_1=operation_1(i,j,k)+operation_3(k,i,j)
if i!=resultat_1:
    resultat_2=resultat_1+operation_2(k,j,i)
else:
    resultat_2=resultat_1+operation_2(k,i,j)
print(resultat_2)

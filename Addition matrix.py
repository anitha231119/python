X=[[12,7,3],
   [4,3,1],
   [2,3,5]]
Y=[[10,4,5],
   [5,4,3],
   [1,2,3]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][y]+y[i][j]
for r in result:
    print(r)

mat = [[2,3,4,5,6,2,4,3],
      [2,3,4,7,6,7,6,2],
      [2,3,5,5,5,5,2,5],
      [2,3,1,1,0,1,3,6],
      [1,1,0,2,9,0,3,5],
      [2,3,1,1,5,1,0,7]]

ans = []
for i in range(len(mat)-2):
  for j in range(len(mat[0])-2):
    if(mat[i][j] == mat[i][j+1]==mat[i][j+2]):
      ans.append(mat[i][j])
    elif(mat[i][j] == mat[i+1][j] == mat[i+2][j]):
      ans.append(mat[i][j])
    elif(mat[i][j]==mat[i+1][j+1]==mat[i+2][j+2]):
      ans.append(mat[i][j])
      
for i in range(len(mat)-2):
  for j in range(len(mat)-2, len(mat[i])):
    if(mat[i][j]==mat[i+1][j]==mat[i+2][j]):
      ans.append(mat[i][j])

for i in range(len(mat)-2, len(mat)):
  for j in range(len(mat[i])-2):
    if(mat[i][j]==mat[i][j+1]==mat[i][j+2]):
      ans.append(mat[i][j])

      
print(ans)
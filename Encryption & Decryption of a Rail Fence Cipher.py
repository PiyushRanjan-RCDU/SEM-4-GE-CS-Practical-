# Rail Fence cipher encryption
plaintext=input("enter the plain text : ")
key=int(input("enter the key value : "))
text=plaintext.upper()
matrix=[[" " for x in range(len(plaintext))] for y in range(key)]
flag=0
row=0
for i in range(len(text)):
  matrix[row][i]=text[i]
  if row==0:
    flag=0
  elif row==key-1:
    flag=1
  if flag==0:
    row+=1
  else:
    row-=1
for i in range(key):
    "".join(matrix[i])
ciphertext=[]
for i in range(key):
    for j in range(len(text)):
        if matrix[i][j]!=' ':
            ciphertext.append(matrix[i][j])
cipher="".join(ciphertext)
print("Cipher Text: ",cipher)

#rail fence cipher decryption
def decryptRailFence(cipher, key):
 
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix to
    # distinguish filled spaces
    # from blank ones
    rail = [[' ' for i in range(len(cipher))]
                  for j in range(key)]
     
    # to find the direction
    dir_down = None
    row, col = 0, 0
     
    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        # place the marker
        rail[row][col] = '*'
        col += 1
         
        # find the next row
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
             
    # now we can construct the
    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
         
    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
         
        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))
 
# Driver code
if __name__ == "__main__":
    # Now decryption of the
    # same cipher-text
    cipher=input("enter the cipher text : ")
    key=int(input("enter the key value : "))
    print(decryptRailFence(cipher, key))
def spiral_creator(n):
    top = 0
    bottom = n-1
    left =0
    right = n-1
    num = 1
    mat = [[0]*n for i in range(n)]

    while top<=bottom and left<=right:
        # We'll go right first
        for i in range(left, right+1):
            mat[top][i]=num
            num+=1
        top+=1
        #We'll go down now
        for i in range(top, bottom+1):
            mat[i][right] = num
            num+=1
        right-=1
        #We'll go left now
        if right>=left:
            for i in range(right, left-1,-1):
                mat[bottom][i] = num
                num+=1
            bottom-=1
        #We'll go up now
        if bottom>=top:
            for i in range(bottom, top-1,-1):
                mat[i][left] = num
                num+=1
            left+=1
    ans = []
    for i in mat:
        for j in i:
            ans.append(j)
    
    lst = []
    brk = n-1
    for i in range(len(ans)):
        if i==brk:
            brk+=n
            lst.append(ans[i])
            print(lst)
            lst = []
        else:
            lst.append(ans[i])

    return ans

print(spiral_creator(4))

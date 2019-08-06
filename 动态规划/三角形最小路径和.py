def minimumTotal(triangle):
    for i in range(len(triangle)-1, -1, -1):
        print(i)
        if i == len(triangle)-1:
            print(triangle)
            continue
        else:
            for j in range(len(triangle[i])):
                print(i,j)
                print(triangle[i + 1][j])
                print(triangle[i + 1][j + 1])
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
            print(triangle)
    return triangle[0][0]
minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
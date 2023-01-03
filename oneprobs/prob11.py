grid = open('prob11text.txt', 'r')

gridlist = []

for line in grid:
    linestrlist = line.split(" ")
    lineintlist = [int(i) for i in linestrlist]
    gridlist.append(lineintlist)

#print(gridlist)

greatestproduct = 0

def productList(nums):
    product = 1
    for i in nums:
        product *= i
    return product

#left-right
for i in range(20):
    for j in range(17):
        if productList(gridlist[i][j:(j+3)]) > greatestproduct:
            greatestproduct = productList(gridlist[i][j:(j+3)])

#up-down
for k in range(17):
    for l in range(20):
        if (gridlist[k][l]*gridlist[k+1][l]*gridlist[k+2][l]*gridlist[k+3][l]) > greatestproduct:
            greatestproduct = gridlist[k][l]*gridlist[k+1][l]*gridlist[k+2][l]*gridlist[k+3][l]

#top-left to bottom-right
for m in range(17):
    for n in range(17):
        if (gridlist[m][n]*gridlist[m+1][n+1]*gridlist[m+2][n+2]*gridlist[m+3][n+3]) > greatestproduct:
            greatestproduct = gridlist[m][n]*gridlist[m+1][n+1]*gridlist[m+2][n+2]*gridlist[m+3][n+3]

#top-right to bottom-left

for p in range(17):
    for q in range(3,20):
        if (gridlist[p][q]*gridlist[p+1][q-1]*gridlist[p+2][q-2]*gridlist[p+3][q-3]) > greatestproduct:
            print(p)
            print(q)
            greatestproduct = gridlist[p][q]*gridlist[p+1][q-1]*gridlist[p+2][q-2]*gridlist[p+3][q-3]

print(greatestproduct)
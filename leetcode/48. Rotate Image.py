class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we take the 00 element and put it in a temp variable then move the 02 variable to 00 position, 22 variable to 02 location and so on. This is done so we don't have to put the variables in temp again and again for each transfer, which is why we go in the backward direction. Then we have just solvd the outer square and reduced values of our boundaries to create subproblems of the same

        l = 0
        r = len(mat) - 1
        top = 0
        bottom = len(mat) - 1
        while (l < r):
            for i in range(r - l):

                temp = mat[top][l + i]
                mat[top][l + i] = mat[bottom - i][l]
                mat[bottom - i][l] = mat[bottom][r - i]
                mat[bottom][r - i] = mat[top + i][r]
                mat[top + i][r] = temp

            l += 1
            r -= 1
            top += 1
            bottom -= 1

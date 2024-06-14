# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 00:56:22 by inazaria          #+#    #+#              #
#    Updated: 2024/06/14 03:26:39 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List

class Solution:
    def checkNumInSquare(self, board, val: str, i: int , j: int) -> bool :
        remainder_i: int = i % 3
        list_i_rows: List[int] = []

        if (remainder_i == 0) :
            list_i_rows = [i, i + 1, i + 2]
        if (remainder_i == 1) :
            list_i_rows = [i - 1, i, i + 1]
        if (remainder_i == 2) :
            list_i_rows = [i - 2, i - 1, i]
        
        remainder_j: int = j % 3
        list_j_rows: List[int] = []
        
        if (remainder_j == 0) :
            list_j_rows = [j, j + 1, j + 2]
        if (remainder_j == 1) :
            list_j_rows = [j - 1, j, j + 1]
        if (remainder_j == 2) :
            list_j_rows = [j - 2, j - 1, j]

        if list_j_rows[2] == 9 :
            print(j)
        square = [board[x][y] for x in list_i_rows for y in list_j_rows]
        if val in square :
            return False

        return True

    def isValidNum(self, board, val: str, i: int , j: int) -> bool :

        for x in range(0, 9) :
            if board[x][j] == val and i != x :
                return False
            
            if board[i][x] == val and j != x :
                return False

        if not self.checkNumInSquare(board, val, i, j) :
            return False
        
        return True

    def sudokuBacktracking(self, board, row, col) -> bool:
        
        # if we're at the end of the graph
        if row == 8 and col == 9 :
            return True
        
        # if we're at the end of a row
        if col == 9 :
            row += 1
            col = 0
        
        if board[row][col] != "." :
            return self.sudokuBacktracking(board, row, col + 1)

        for val in range(1, 10) :
            if (self.isValidNum(board, str(val), row, col)) :
                board[row][col] = str(val)
                if (self.sudokuBacktracking(board, row, col + 1)) :
                    return True
            board[row][col] = "."

        return False

            

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.sudokuBacktracking(board, 0, 0) 

        


if __name__ == "__main__" : 
    if (len(sys.argv) != 2) :
        print("Usage : python Solution.py <\"[[...], [...], ...]\">")
        sys.exit(1)

    try :
        matrix = eval(sys.argv[1])
    except :
        print("Error : Invalid input")
        sys.exit(1)

    if (len(matrix) != 9) :
        print("Error : Invalid input")
        sys.exit(1)

    for row in matrix :
        if (len(row) != 9) :
            print("Error : Invalid input")
            sys.exit(1)
        for cell in row :
            if (cell != '.' and (cell < '1' or cell > '9')) :
                print("Error : Invalid input")
                sys.exit(1)

    print("Before Solving : ")
    for row in matrix :
        print(row)
    print("\n")
    Solution().solveSudoku(matrix)
    print("After Solving : ")
    for row in matrix :
        print(row)
    sys.exit(0)
    

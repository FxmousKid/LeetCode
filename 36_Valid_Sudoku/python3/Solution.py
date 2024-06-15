# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/15 02:15:54 by inazaria          #+#    #+#              #
#    Updated: 2024/06/15 03:22:22 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List


class Solution:
    def isValidRow(self, board, i, j, val) -> bool :
        for x in range(0, 9) :
            if board[i][x] == val and x != j :
                return False
        
        return True    

    def isValidColumn(self, board, i, j, val) -> bool :
        for y in range(0, 9) :
            if board[y][j] == val and y != i :
                return False

        return True

    def isValidSquare(self, board, i, j, val) -> bool :
        remainder_i = i % 3
        remainder_j = j % 3

        list_i_rows = []
        if (remainder_i == 0) : list_i_rows = [i, i + 1, i + 2]
        if (remainder_i == 1) : list_i_rows = [i - 1, i, i + 1]
        if (remainder_i == 2) : list_i_rows = [i - 2, i - 1, i]

        list_j_rows = []
        if (remainder_j == 0) : list_j_rows = [j, j + 1, j + 2]
        if (remainder_j == 1) : list_j_rows = [j - 1, j, j + 1]
        if (remainder_j == 2) : list_j_rows = [j - 2, j - 1, j]

        sqaure = [board[x][y] for x in list_i_rows for y in list_j_rows if (i, j) != (x, y)]
        if val in sqaure: 
            return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9) :
            for j in range(0, 9) :
                cell = board[i][j]
                if cell == "." :
                    continue
                
                if not(self.isValidRow(board, i, j, cell)) :
                    print(f"1) i = {i}, j = {j}, val = {cell}")
                    return False

                if not (self.isValidColumn(board, i, j, cell)) :
                    print(f"2) i = {i}, j = {j}, val = {cell}")
                    return False

                if not (self.isValidSquare(board, i, j, cell)) :
                    print(f"3) i = {i}, j = {j}, val = {cell}")
                    return False

        return True



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

    print("\nSudoku : \n")
    isSolvable: bool = Solution().isValidSudoku(matrix)
    for row in matrix :
        print(row)
    print(f"\nIs this solvable ? : {isSolvable}")
    sys.exit(0)
 

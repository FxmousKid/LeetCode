# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/15 20:19:14 by inazaria          #+#    #+#              #
#    Updated: 2024/06/15 22:01:06 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Solution:
    def concatDoubleList(self, lst: list[list[str]]) -> str :
        result: str = ""
        for sub_list in lst :
            result += "".join(sub_list)

        return result


    def convert(self, s: str, numRows: int) -> str:
        
        numCols: int = len(s) // numRows
        lst_2d = [[""] * (numRows * (numCols + 1)) for _ in range(numRows)]

        i = j = 0
        isDescending = False
        for n in range(len(s)) :
            lst_2d[i][j] = s[n]

            if i == numRows - 1:
                i -= 1
                j += 1
                isDescending = True

            elif i == 0 :
                i += 1
                isDescending = False

            elif isDescending == True :
                i -= 1
                j += 1

            else :
                i += 1

        return self.concatDoubleList(lst_2d)



if __name__ == "__main__" :
    if (len(sys.argv) != 3) :
        print("Usage : python Solution.py <stringToConvert> <numberOfRows")
        sys.exit(1)
    
    string = sys.argv[1]
    numRows = int(sys.argv[2])
    if numRows < 1 :
        print("Number of rows must be greater than 0")
        sys.exit(1)

    zigzagString = Solution().convert(string, numRows)
    print(f"string = {string}, numRows =  {numRows}, converted String = {zigzagString}")
    sys.exit(0)

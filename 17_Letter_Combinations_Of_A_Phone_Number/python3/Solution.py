# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/22 17:32:26 by inazaria          #+#    #+#              #
#    Updated: 2024/06/22 20:01:21 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List

class Solution:    

    def letterCombinations(self, digits: str) -> List[str]:
        
        digit_to_letters : dict[str, str] = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def backtrack(idx: int, comb: str) -> None :
            if idx == len(digits) :
                res.append(comb)
                return None

            for letter in digit_to_letters[digits[idx]] :
                backtrack(idx + 1, comb + letter)        

        res = []
        backtrack(0, "")
        res = [] if res == [""] else res

        return res




if __name__ == "__main__" : 
    if (len(sys.argv) != 2):
        print("Usage: python3 Solution.py <digits>")
        sys.exit(1)

    digits = sys.argv[1]
    for digit in digits :
        if not digit.isdigit():
            print("Error: digits must be a number")
            sys.exit(1)

    answer: List[str] = Solution().letterCombinations(digits)
    print(f"digits = {digits}, answer = {answer}")
    sys.exit(0)

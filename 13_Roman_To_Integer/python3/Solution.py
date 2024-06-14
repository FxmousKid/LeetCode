# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 03:38:04 by inazaria          #+#    #+#              #
#    Updated: 2024/06/14 03:40:12 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num : dict[str, int] = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        if len(s) == 1 :
            return roman_num[s]
        
        res : int = 0
        to_substract : int = 0

        for idx in range(1, len(s)):
            if s[idx - 1] == 'I' :
                if s[idx] == 'X' or s[idx] == 'V' : 
                    to_substract += 1
                    continue
            elif s[idx - 1] == 'X' :
                if s[idx] == 'L' or s[idx] == 'C' :
                    to_substract += 10
                    continue
            elif s[idx - 1] == 'C' :
                if s[idx] == 'D' or s[idx] == 'M' : 
                    to_substract += 100
                    continue
            res += roman_num[s[idx - 1]]
        
        res += roman_num[s[-1]]
        return res - to_substract

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Usage: python3 Solution.py <romanString>")
        sys.exit(1)

    for c in sys.argv[1]:
        if c not in "IVXLCDM":
            print("Invalid roman number")
            sys.exit(1)

    roman_val:int = Solution().romanToInt(sys.argv[1])
    print(f"{sys.argv[1]} = {roman_val}")
    sys.exit(0)

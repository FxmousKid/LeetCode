# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 05:07:50 by inazaria          #+#    #+#              #
#    Updated: 2024/06/12 14:13:15 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Solution :
    def isValid(self, s: str) -> bool:
        opening_char : str = "{[("
        total_char : dict[str, int] = {'{' : 1, '}' : -1, '[' : 2, ']' : -2, '(' : 3, ')' : -3}
        opened_char : list[str] = []
        for char in s :
            if (char in opening_char) :
                opened_char.append(char)
                continue 
            if (len(opened_char) == 0) :
                return False
            if (total_char[char] != -total_char[opened_char[-1]]) :
                return False
            opened_char.pop(-1)
        return (len(opened_char) == 0)

if __name__ == "__main__" :
    if (len(sys.argv) != 2) :
        print("Usage : python3 Solution.py <string>")
        sys.exit(1)
    for s in sys.argv[1] :
        if s not in "(){}[]" : 
            print("Not a valid parentheses input !")
            sys.exit(1)
    res : bool = Solution().isValid(sys.argv[1])
    print(f"{sys.argv[1]} is ", end = "")
    print("a valid ", end = "") if res else print("not a valid ", end = "")
    print("parentheses string !")
    

    sys.exit(0)



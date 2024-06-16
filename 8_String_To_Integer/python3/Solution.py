# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/16 21:29:02 by inazaria          #+#    #+#              #
#    Updated: 2024/06/16 21:54:49 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Solution:
    def myAtoi(self, s: str) -> int:
        sign: int = 1
        res : int = 0
        idx : int = 0 
        len_s: int = len(s)

        while idx < len_s and s[idx] == " " :
            idx += 1
                
        if 0 <= idx < len_s and s[idx] == "+" :
            idx += 1

        elif 0 <= idx < len_s and s[idx] == "-" :
            sign *= -1
            idx += 1        

        while idx < len(s) and ord(s[idx]) >= 48 and ord(s[idx]) <= 57 :
            res = 10 * res + ord(s[idx]) - 48
            idx += 1 

        res = res * sign
        res =  2 ** 31 - 1 if res >  2 ** 31 - 1 else res
        res = -2 ** 31     if res < -2 ** 31 else res

        return res
        


if __name__ == "__main__" : 
    if (len(sys.argv) != 2) :
        print("Usage: python3 Solution.py <string>")
        print("Example: python3 Solution.py \"42\"")
        sys.exit(1)

    try :
        num = str(sys.argv[1])
 
    except Exception as e:
        print("Error: ", e)
        print("Usage: python3 Solution.py <string>")
        print("Example: python3 Solution.py \"42\"")
        sys.exit(1)
    
    answer = Solution().myAtoi(num)
    print(f"atoi({num}) = {answer}")

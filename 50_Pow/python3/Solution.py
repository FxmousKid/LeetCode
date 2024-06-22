# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/22 20:57:42 by inazaria          #+#    #+#              #
#    Updated: 2024/06/22 21:09:14 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


class Solution:
    def myPow(self, x: float, n: int) -> float:
        og_x = x

        if n <= 2**31 - 1 and n >= -2**31:
            return x ** n


        if n == 0:
            return 1.0

        if n < 0 :
            n = -n
            while (n > 1) :
                x *= og_x
                n -= 1
            return 1 / x
        
        while (n > 1) :
            x *= og_x
            n -= 1
        return x






if __name__ == "__main__" :
    if (len(sys.argv) != 3) :
        print("Usage: python operations.py <x> <n>")
        print("Example: python3 Solution.py 10 3")
        sys.exit(1)
    
    try:
        x = float(sys.argv[1])
        n = int(sys.argv[2])
    except ValueError:
        print("ValueError: only number\n")
        print("Usage: python operations.py <x> <n>")
        print("Example: python3 Solution.py 10 3")
        sys.exit(1)

    answer: float = Solution().myPow(x, n)
    print(f"{x}^{n} = {answer}")
    sys.exit(0)

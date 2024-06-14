# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 03:25:56 by inazaria          #+#    #+#              #
#    Updated: 2024/06/13 16:53:02 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Solution:
    def ClosentTenPower(self, num: int) -> int :
        powerOfTen: int = 1
        while (powerOfTen * 10 <= num) :
            powerOfTen *= 10
        return (powerOfTen)
    
    def reverse(self, x: int) -> int:
        if x == 0 : 
            return 0
        

        sign = 1
        if x < 0 :
            sign = -1
            x = -x
        res: int = 0
        while x != 0 :
            powerOfTen: int = self.ClosentTenPower(x)
            res += (x % 10) * powerOfTen
            if res > 2**31 - 1 or res < -2**31 :
                return 0
            x -= (x % 10)
            x = int(x / 10)

        return res * sign

if __name__ == "__main__" :
    if (len(sys.argv) != 2):
        print("Usage: python Solution.py <number>")
        sys.exit(1)
    try :
        number = int(sys.argv[1])
    except ValueError:
        print("Invalid number / not a number")
        sys.exit(1)
    reverse_number = Solution().reverse(number)
    print(f"the reverse of {number} is {reverse_number}")
    sys.exit(0)

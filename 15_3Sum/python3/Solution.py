# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/22 17:18:34 by inazaria          #+#    #+#              #
#    Updated: 2024/06/22 17:30:41 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List

class Solution:
    def twoSum(self, nums: List[int]) -> list[int] :
        return []
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return []




if __name__ == "__main__" : 
    if (len(sys.argv) != 3) :
        print("Usage: python operations.py <list> <Target>")
        print("Example: python3 Solution.py '[1,2,3,4,5]' 5")
        sys.exit(1)

    try : 
        lst = eval(sys.argv[1])
        lst: List[int] = [int(i) for i in lst]
        target = int(sys.argv[2])
    except Exception as e:
        print(f"Error: {e}\n")
        print("Usage: python operations.py <list> <Target>")
        print("Example: python3 Solution.py \"[1,2,3,4,5]\" 5")
        sys.exit(1)

    answer: List[List[int]] = Solution().threeSum(lst)
    
    print(f"list = {lst}, target = {target}, answer = {answer}")
    sys.exit(0)

 

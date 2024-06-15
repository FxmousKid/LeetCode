# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/15 23:36:53 by inazaria          #+#    #+#              #
#    Updated: 2024/06/15 23:55:51 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map: dict[int, int] = {target - val : idx  for idx, val in enumerate(nums)}

        answer: List[int] = []
        for i in range(len(nums)) :
            try : 
                answer = [i, hash_map[nums[i]]]
                if answer[0] == answer[1] :
                    answer = []
                    continue
                return answer
            except :
                continue

        return answer            



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

    answer: List[int] = Solution().twoSum(lst, target)
    print(f"list = {lst}, target = {target}, answer = {answer}")
    sys.exit(0)

     

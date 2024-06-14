# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 19:21:11 by inazaria          #+#    #+#              #
#    Updated: 2024/06/14 19:27:30 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
       return 1 

if __name__ == "__main__" :
    if (len(sys.argv) != 2) :
        print("Usage : python3 Solution.py <\"[...]\">")
        sys.exit(1)

    lst_str: List[str] = eval(sys.argv[1])
    lst: List[int] = [int(i) for i in lst_str]
    answer: int = Solution().firstMissingPositive(lst)
    print(f"list = {lst}, answer = {answer}")
    sys.exit(0)


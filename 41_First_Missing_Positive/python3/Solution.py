# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 19:21:11 by inazaria          #+#    #+#              #
#    Updated: 2024/06/15 01:28:22 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List, Union

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int :
        positive_list: List[Union[int, str]]

        first_missing_positive: int = 1
        for num in nums :
            
            if num > 0 and 


        return first_missing_positive

if __name__ == "__main__" :
    if (len(sys.argv) != 2) :
        print("Usage : python3 Solution.py <\"[...]\">")
        sys.exit(1)

    lst_str: List[str] = eval(sys.argv[1])
    lst: List[int] = [int(i) for i in lst_str]
    answer: int = Solution().firstMissingPositive(lst)
    print(f"list = {lst}, answer = {answer}")
    sys.exit(0)


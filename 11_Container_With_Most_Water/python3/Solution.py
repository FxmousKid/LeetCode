# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/16 22:36:09 by inazaria          #+#    #+#              #
#    Updated: 2024/06/16 23:15:14 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List

class Solution():
    def maxArea(self, height : List[int]) -> int:
        maxArea: int = 0
        h: List[int] = height
        n: int = len(height)
        i: int = 0
        j: int = n - 1

        while (i < j) :
            maxArea = max(maxArea, (j - i) * min(h[i], h[j]))
            if h[i] > h[j] :
                j -= 1
            else :
                i += 1

        return maxArea


if __name__ == "__main__" : 
    if (len(sys.argv) != 2) :
        print("Usage: python Solution.py <\"list\">")
        print("Example: python Solution.py \"[1, 2, 3, 4, 5]\"")
        sys.exit(1)

    try:
        height = eval(sys.argv[1])
        if (type(height) != list) :
            raise Exception

    except Exception as e:
        print("Error: Invalid list")
        sys.exit(1)

    maxArea: int = Solution().maxArea(height)
    print(f"MaxArea for {height} : {maxArea}")

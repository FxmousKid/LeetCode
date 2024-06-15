# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/15 03:22:59 by inazaria          #+#    #+#              #
#    Updated: 2024/06/15 03:42:23 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_set: set = set()
        max_len: int = 0
        left: int = 0

        for right in range(len(s)) :
            while s[right] in substring_set :
                substring_set.remove(s[left])
                left += 1

            substring_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__" : 
    if (len(sys.argv) != 2) :
        print("Usage : python3 Solution.py <string>")
        sys.exit(1)

    answer: int = Solution().lengthOfLongestSubstring(sys.argv[1])
    print(f"Length of Longest substring in {sys.argv[1]} = {answer}")
    sys.exit(0)

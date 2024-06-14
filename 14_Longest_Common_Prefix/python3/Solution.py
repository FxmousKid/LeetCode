# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 04:10:39 by inazaria          #+#    #+#              #
#    Updated: 2024/06/12 05:06:33 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Solution :
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        prefix = ""
        index : int = 0

        while (index < len(strs[0])) :
            temp = strs[0][index]
            for string in strs :
                if string[index] != temp :
                    return (prefix)
            prefix += temp
            index += 1
        return (prefix)


if __name__ == "__main__" :
    if (len(sys.argv) == 1) :
        print("Usage : python3 Solution.py <str1> <str2> <str3> ...")
        sys.exit(1)
    prefix : str = Solution().longestCommonPrefix(sys.argv[1:])
    print(f"Longest Common Prefix = \"{prefix}\" !")
    sys.exit(0)


# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 02:57:15 by inazaria          #+#    #+#              #
#    Updated: 2024/06/13 03:24:51 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index : int = 0
        while (index + len(needle) <= len(haystack)) :
            #reducedHaystack : str = "".join([haystack[i + index] for i in range(len(needle))])
            reducedHaystack : str = haystack[index : index + len(needle)]
            if (needle == reducedHaystack) :
                return (index)

            index += 1

        return (-1)

if __name__ == "__main__" :
    if (len(sys.argv) != 3) :
        print("Usage: python Solution.py <haystackString> <needleString>")
        sys.exit(1)
    haystack : str = sys.argv[1]
    needle : str = sys.argv[2]
    needleIndex : int = Solution().strStr(haystack, needle)
    print(f"1st Index of {needle} in {haystack}: {needleIndex}")
    sys.exit(0)

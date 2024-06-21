# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/17 01:43:05 by inazaria          #+#    #+#              #
#    Updated: 2024/06/18 19:35:54 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        



if __name__ == "__main__" :
    if (len(sys.argv) != 3) :
        print("Usage : python3 Solution.py <string> <wordDict>")
        print("Example : python3 Solution \"catsandog\" \"[\"cats\",\"dog\",\"sand\",\"and\",\"cat\"]")
        sys.exit(1)

    wordDict = []
    string = ""
    try : 
        string: str = str(sys.argv[1])
        wordDict: list[str] = eval(sys.argv[2])
    except :
        print("Error : Bad Formatting")
        print("Usage : python3 Solution.py <string> <wordDict>")
        print("Example : python3 Solution \"catsandog\" \"[\"cats\",\"dog\",\"sand\",\"and\",\"cat\"]")
    
    answer: bool = Solution().wordBreak(string, wordDict)
    print(f"string = {string}, wordDict = {wordDict}, answer = {answer}")

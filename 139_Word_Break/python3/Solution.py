# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/17 01:43:05 by inazaria          #+#    #+#              #
#    Updated: 2024/06/21 22:46:39 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List

class Solution:

    def isValidWord(self, s, index_s, word) -> bool :
        len_word = len(word)
        return s[index_s:index_s + len_word] == word


    def backtrack(self, s: str, index_s: int, wordDict: List[str], dp: dict[int, bool]) -> bool :
        
        if index_s in dp :
            return dp[index_s]

        if index_s >= len(s) :
            return True

        for word in wordDict :
            if self.isValidWord(s, index_s, word) :
                dp[index_s] = True
                if self.backtrack(s, index_s + len(word), wordDict, dp) :
                    return True
                
        dp[index_s] = False

        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict : 
            return True

        dp: dict[int, bool] = {}
        return self.backtrack(s, 0, wordDict, dp)


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

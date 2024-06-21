# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/21 19:55:06 by inazaria          #+#    #+#              #
#    Updated: 2024/06/21 22:46:34 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List

class Solution:

    def isValidWord(self, s, index_s, word) -> bool :
        return s[index_s:index_s + len(word)] == word

    def backtracking(self, s, index_s, wordDict, memo, perms) -> list[list[str]]:

        print(f"index_s = {index_s}, perms = {perms}")
        
        if index_s >= len(s) and perms[-1] == [] :
            print("the follow call was from line 26")
            return perms

        if index_s >= len(s) and perms[-1] not in perms[:-1] :
            if sum([len(lst) for lst in perms[-1]]) == len(s) :
                perms.append([])
                print("the follow call was from line 32")
                return (self.backtracking(s, 0, wordDict, {}, perms))    

#        if index_s in memo :
#            if memo[index_s] == True :
#                perms[-1].append()
  
        for word in wordDict :
            if index_s not in memo :
                if (self.isValidWord(s, index_s, word)) :
                    memo[index_s] = True
                    perms[-1].append(word)

            if index_s in memo and memo[index_s] == True :
                print("the follow call was from line 46")
                return (self.backtracking(s, index_s + len(word), wordDict, memo, perms))
                     
    
        if len(perms[-1]) > 0 :
            memo[index_s] = False
            wrongWord = perms[-1].pop(-1)
            print("the follow call was from line 53")
            return (self.backtracking(s, index_s - len(wrongWord), wordDict, memo, perms))


    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        memo: dict[int, str] = {}
        perms: list[list[str]] = [[]]

        answer_list : list[list[str]] = self.backtracking(s, 0, wordDict, memo, perms)
        answer : list[str] = [" ".join(lst) for lst in answer_list if lst != []]
        
        if answer[0] == '' :
            return []

        return answer


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
    
    answer: list[str] = Solution().wordBreak(string, wordDict)
    print(f"string = {string}\nwordDict = {wordDict}\nanswer = {answer}")

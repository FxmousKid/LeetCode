# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 16:56:50 by inazaria          #+#    #+#              #
#    Updated: 2024/06/13 22:36:12 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Solution:
    def handleStarMatch(self, s: str, index_s: int, p: str, index_p: int) -> int :
        '''will iterate in s while s[i++] = prev_char, can be 0 times, can be all of s.
        We will match at most until the remaining chars in s == the remaining chars in c'''
 
        while self.isRegexCharMatch(s[index_s], p[index_p]):
            if len(s) - index_s - 1 == len(p) - index_p : 
                break
            index_s += 1
            if index_s >= len(s) :
                break

        return index_s
        

    def isRegexCharMatch(self, s_0: str, val_p: str) -> bool :
        if (val_p == '.') :
            return True

        return (val_p == s_0)


    def isMatch(self, s: str, p: str) -> bool:

        index_p: int = 0
        index_s: int = 0
        while (index_p < len(p) and index_s < len(s)) :

            if (index_p < len(p) - 1 and p[index_p + 1] == "*") :
                print(f"before * handling : s_index = {index_s}, p_index = {index_p}")
                index_s = self.handleStarMatch(s, index_s, p, index_p)
                index_p += 1
                print(f"After * handling  : s_index = {index_s}, p_index = {index_p + 1}")
                print("\n")


                
            elif (self.isRegexCharMatch(s[index_s], p[index_p])) :
                index_s += 1

            #print(f"s_index = {index_s}, p_index = {index_p}")
            
            index_p += 1
        
        
        print(f"index_s = {index_s}, index_p = {index_p}")

        len_s: int = len(s)
        len_p: int = len(p)

        

        if (index_p < len_p or index_s < len_s) :
            return False
     
        return True


if __name__ == '__main__' :
    if (len(sys.argv) != 3) :
        print("Usage: python Solution.py <stringToMatch> <pattern>")
        sys.exit(1)
    
    string: str = sys.argv[1]
    pattern: str = sys.argv[2]
    match_val: bool = Solution().isMatch(string, pattern)
    print(f"{pattern} matched in {string} : {match_val}")
    sys.exit(0)

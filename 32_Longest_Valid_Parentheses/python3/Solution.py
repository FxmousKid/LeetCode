# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 22:37:58 by inazaria          #+#    #+#              #
#    Updated: 2024/06/13 23:53:54 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Solution:
    def isNotValid(self, s1: str, s2: str) -> bool :
        '''Retursn 1 if s1 and s2 are not valid Parentheses'''
        if (s1 == '(' and s2 == '(') :
            return True

        if (s1 == ')' and s2 == ')') :
            return True

        if (s1 == ')' and s2 == '(') :
            return True

        return False

    def loop_from_idx(self, s, index) -> int :
        current_valid: int = 0
        longest_valid: int  = 0
        
        for idx in range(1 + index, len(s), 2) :
            val = s[idx]

            #print(f"(idx, val) = ({idx}, {val} )")
            #print(f"s[idx - 1] = {s[idx]}, val = {val}, idx = {idx}")
            if (idx >= len(s)) : 
                break

            if self.isNotValid(s[idx - 1], val) :
            #    print(f"self.isNotValid({s[idx - 1]}, {val})")
                current_valid = 0

            if s[idx - 1] == "(" and val == ")" :
             #   print(f"current_valid = {current_valid}")
                current_valid += 1

            if current_valid > longest_valid :
                longest_valid = current_valid
            
        
        return (longest_valid * 2)


    def longestValidParentheses(self, s: str) -> int:
       
        if (len(s) <= 1) :
            return 0

        if len(s) == 2 :
            if not(self.isNotValid(s[0], s[1])) :
                return 2
            return 0

        longest_start_0: int = self.loop_from_idx(s, 0)
        longest_start_1: int = self.loop_from_idx(s, 1)
            
        return (max(longest_start_0, longest_start_1))


if __name__ == "__main__" : 
    if (len(sys.argv) != 2) :
        print("Usage : python Solution.py <String>")
        sys.exit(1)
    
    for s in sys.argv[1] :
        if (s != '(' and s != ')') :
            print("Usage : python Solution.py <String>")
            sys.exit(1)

    sol = Solution().longestValidParentheses(sys.argv[1])
    print(f"Longest Valid Parentheses in {sys.argv[1]} : {sol}")

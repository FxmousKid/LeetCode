# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/15 17:38:19 by inazaria          #+#    #+#              #
#    Updated: 2024/06/16 05:20:40 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

# Time to Implement Manacher's Algorithm !
# Nevermind it's tough, if anyone expects it in a interview, i might as well
# expect CEO position from them hahaha
# we're implementing expand around center method, O(n^2) time, but O(1) space

class Solution:
    def expandAroundCenter(self, s, left, right) -> str :

        while (left >= 0 and right < len(s) and s[right] == s[left]) :
            left -= 1
            right += 1

        return (s[left + 1 : right])
        

    def longestPalindrome(self, s: str) -> str:
        
        if (len(s) <= 1) :
            return s
    
        longest: str = ""
        for i in range(len(s)) :

            odd_palindrome_substr: str = self.expandAroundCenter(s, i, i) 
            even_palindrome_substr: str = self.expandAroundCenter(s, i, i + 1)
       
            if len(odd_palindrome_substr) > len(longest) :
                longest = odd_palindrome_substr

            if len(even_palindrome_substr) > len(longest) :
                longest = even_palindrome_substr

        return longest


if __name__ == "__main__" :
    if (len(sys.argv) != 2) :
        print("Usage : python Solution.py <string>")
        sys.exit(1)
 
    string: str = sys.argv[1]
    answer: str = Solution().longestPalindrome(string)
    print(f"Longest Palindrome in {string} : {answer}")
    sys.exit(0)

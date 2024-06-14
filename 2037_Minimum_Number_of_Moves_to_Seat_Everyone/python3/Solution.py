# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 18:54:25 by inazaria          #+#    #+#              #
#    Updated: 2024/06/14 19:13:24 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
    
        moves = 0
        for i in range(len(seats)) :
            seats_i = seats[i]
            students_i = students[i]
            maximum = max(seats_i, students_i)
            minimum = min(seats_i, students_i)
            
            while (minimum < maximum) :
                moves += 1
                minimum += 1

        return moves

if __name__ == "__main__" :
    if (len(sys.argv) != 3) :
        print("Usage : python3 Solution.py <seatsList> <studentList>" )
        sys.exit(1)

    seats = eval(sys.argv[1])
    students = eval(sys.argv[2])

    seats = [int(i) for i in seats]
    students = [int(i) for i in students]

    answer = Solution().minMovesToSeat(seats, students)
    print(f"Seats : {seats}")
    print(f"Students : {students}")
    print(f"Answer : {answer}")
    sys.exit(0)

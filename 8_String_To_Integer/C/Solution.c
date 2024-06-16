/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Solution.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/16 21:55:01 by inazaria          #+#    #+#             */
/*   Updated: 2024/06/16 22:35:25 by inazaria         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

# include <stdio.h>
# include <limits.h>

int myAtoi(char* s) {
	int		sign = 1;
	int		idx = 0;
	long	res = 0;

	while (s[idx] && s[idx] == ' ') {
		idx++;
	}

	if (s[idx] && s[idx] == '+') {
		idx++;
	}

	else if (s[idx] && s[idx] == '-') {
		sign = -sign;
		idx++;
	}

	while (s[idx] && s[idx] >= '0' && s[idx] <= '9') {
		
		res = 10 * res + s[idx] - '0';
		if (res * sign > INT_MAX) {
			res = INT_MAX;
			return res;
		}
		if (res * sign < INT_MIN) {
			res = INT_MIN;
			return res;
		}	
		idx++;
	}

	res *= sign;
	return (res);	
}

int	main(int argc, char *argv[]) {
	if (argc != 2) {
		fprintf(stdout, "Usage : ./a.out \"num\"");
		return (1);
	}
	int	answer;
	answer = myAtoi(argv[1]);
	printf("myAtoi(%s) = %d", argv[1], answer);
	return (0);
}

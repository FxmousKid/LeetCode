/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Solution.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/21 10:36:45 by inazaria          #+#    #+#             */
/*   Updated: 2024/06/21 17:11:51 by inazaria         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

bool	isValidWord(char *s, size_t index_s, char *word) {
	if (strncmp(s + index_s, word, strlen(word)) == 0)
		return true;

	return false;
}

// dp[x] == 0 -> not visited
// dp[x] == 1 -> visited and true
// dp[x] == 2 -> visited and false

bool	backtracking(char *s, size_t index_s, char **wordDict, int wordDictSize, int *dp, size_t size_dp) {
	if (index_s >= strlen(s))
		return true;

	if (dp[index_s] > 0)
		return (dp[index_s] == 1) ? true : false;

	for (int i = 0; i < wordDictSize; i++) {
		if (isValidWord(s, index_s, wordDict[i]) == true) {
			if (backtracking(s, index_s + strlen(wordDict[i]), wordDict, wordDictSize, dp, size_dp) == true) {
				dp[index_s] = 1;
				return true;
			}
		}
	}

	dp[index_s] = 2;
	return false;
}

bool	wordBreak(char* s, char** wordDict, int wordDictSize) {	

	int dp[strlen(s)];
	bzero(dp, strlen(s) * sizeof(int));

	return backtracking(s, 0, wordDict, wordDictSize, dp, 0);
}


int main(int argc, char *argv[]) {

	if (argc < 2) {
		return (1);
	}

	int	wordDictSize = argc - 2;
	char *wordDict[wordDictSize];

	for (int i = 2; i < argc; i++)
		wordDict[i - 2] = argv[i];


	bool answer = wordBreak(argv[1], wordDict, wordDictSize);
	(answer) ? printf("answer is True\n") : printf("Asnwer is False\n");
	return (0);
}

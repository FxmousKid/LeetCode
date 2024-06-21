/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Solution.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/21 17:23:24 by inazaria          #+#    #+#             */
/*   Updated: 2024/06/21 19:54:37 by inazaria         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>



typedef struct Trie {
	struct	Trie* childs[26];
	bool	wordEnd;
}			Trie;


Trie* trieCreate() {
	Trie *trie = (Trie *) calloc(sizeof(Trie), 1);
	//bzero(trie->childs, sizeof(Trie*) * 26);
	return (trie);
}

void trieInsert(Trie* obj, char* word) {
	
	if (word == NULL || *word == '\0')
		return ;
	
	Trie	*tmp = obj;
	int		charIndex;
	
	for (size_t idx = 0; idx < strlen(word); idx++) {
		charIndex = word[idx] - 'a';
		
		if (tmp->childs[charIndex] == NULL)
			tmp->childs[charIndex] = trieCreate();
		
		tmp = tmp->childs[charIndex];
	}
	tmp->wordEnd = true;
}

bool trieSearch(Trie* obj, char* word) {
	if (word == NULL)
		return (false);

	if (*word == '\0')
		return true;
	
	Trie	*tmp = obj;
	int		charIndex;

	for (size_t idx = 0; idx < strlen(word) - 1; idx++) {
		charIndex = word[idx] - 'a';
		if (tmp->childs[charIndex] == NULL)
			return false;

		tmp = tmp->childs[charIndex];
	}

	Trie *lastChar = tmp->childs[word[strlen(word) - 1] - 'a'];
	
	if (lastChar == NULL)
		return false;

	return (lastChar->wordEnd);
}

bool trieStartsWith(Trie* obj, char* prefix) {
	if (prefix == NULL)
		return (false);

	if (*prefix == '\0')
		return true;
	
	Trie	*tmp = obj;
	int		charIndex;

	for (size_t idx = 0; idx < strlen(prefix) - 1; idx++) {
		charIndex = prefix[idx] - 'a';
		
		if (tmp->childs[charIndex] == NULL)
			return false;

		tmp = tmp->childs[charIndex];
	}

	tmp = tmp->childs[prefix[strlen(prefix) - 1] - 'a'];
	if (tmp == NULL)
		return false;

	return true;
}

void trieFree(Trie* obj) {

	for (size_t i = 0; i < 26; i++) {
		if (obj->childs[i] != NULL)
			trieFree(obj->childs[i]);
	}
	free(obj);
}



int main(void) {
	Trie *t = trieCreate();
	trieInsert(t, "hello");
	printf(" \"Hello\" in t : ");
	trieSearch(t, "helloo") == true ? printf("yes !\n") : printf("no !\n");

	trieFree(t);
	return (0);	
}

/**
 * Your Trie struct will be instantiated and called as such:
 * Trie* obj = trieCreate();
 * trieInsert(obj, word);
 
 * bool param_2 = trieSearch(obj, word);
 
 * bool param_3 = trieStartsWith(obj, prefix);
 
 * trieFree(obj);
*/

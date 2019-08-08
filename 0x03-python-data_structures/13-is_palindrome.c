#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks palindrome
 * @head: listint_t
 * Return: int
 */

int is_palindrome(listint_t **head)
{

	int count;
	listint_t *h = *head;

	int *s;
	int *beg;
	int *end;
	int x;
	int y = 0;

	for (count = 0; h; count++)
		h = h->next;

	s = malloc(sizeof(char) * count + 1);
	for (x = 0; x < count; x++)
	{
		s[x] = (*head)->n;
		(*head) = (*head)->next;
	}
	s[x] = '\0';
	end = s;
	beg = s;
	while (*end)
		end++;
	end--;
	while (y < (count / 2))
	{

		if (*beg != *end)
		{
			return (0);
		}
		beg++;
		end--;
		y++;
	}
	return (1);
}

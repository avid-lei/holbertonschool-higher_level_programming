#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - insert node in sorted list
 * @head: listint_t **
 * @number: int
 * Return: listint_t
 */


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *checker = *head;
	listint_t *node = malloc(sizeof(listint_t));

	if (!node)
		return (NULL);

	if (!head)
		return (NULL);

	node->n = number;
	node->next = NULL;

	if (!(*head))
		return (node);

	while (checker->next->n < number && checker->next->next)
	{
		checker = checker->next;
	}

	if (checker->next->next)
	{
		node->next = checker->next;
		checker->next = node;
	}
	else
		checker->next->next = node;

	return (node);

}

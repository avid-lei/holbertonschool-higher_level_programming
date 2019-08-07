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

	if (!head || !(*head))
		return (NULL);


	if (!node)
		return (NULL);

	node->n = number;
	node->next = NULL;

	while (checker->next->n < number)
	{
		checker = checker->next;
	}

	node->next = checker->next;
	checker->next = node;


	return (node);

}

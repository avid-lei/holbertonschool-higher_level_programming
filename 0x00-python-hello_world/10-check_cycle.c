#include "lists.h"

/**
 * check_cycle - check if there is a cycle in linked list
 * @list: listint_t
 * Return: 1 if founs, 0 if not)
 */

int check_cycle(listint_t *list)
{

	listint_t *tor = list;
	listint_t *har = list;


while (tor->next && har->next->next)
{
	tor = tor->next;
	har = har->next->next;

	if (tor == har)
		return (1);

}

return (0);


}

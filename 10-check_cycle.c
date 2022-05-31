#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: the list to check for the cycle
 *
 * Return: If there is no cycle - 0 or 1;
 */

int check_cycle(listint_t *list)
{
	listint_t *node = NULL;
	listint_t *node2 = NULL;

	if (list == NULL || list->next == NULL)
		return (0);

	node = list->next;
	node2 = list->next->next;

	while ((node && node2) && node2->next != NULL)
	{
		if (node == node2)
			return (1);

		node = node->next;
		node2 = node2->next->next;
	}
	return (0);
}

#include "lists.h"
/**
 * is_palindrome - checks if the linked list value is palindrome
 * @head: first node
 *
 * Return: 1 if the list is palindrome or 0 if it is not
 */

int is_palindrome(listint_t **head)
{
	listint_t *head2 = *head, *head3 = *head;
	int *pA;
	int i = 0, j = 0;

	if (head == NULL)
		return (1);
	while (head2 != NULL)
	{
		i++;
		head2 = head2->next;
	}
	pA = malloc(sizeof(int) * i);
	while (head3 != NULL)
	{
		*(pA + j) = head3->n;
		j++;
		head3 = head3->next;
	}
	for (j = 0; j < i / 2; j++)
	{
		if (pA[i - 1 - j] == pA[j])
			continue;
		else
		{
			free(pA);
			return (0);
		}
	}
	free(pA);
	return (1);
}

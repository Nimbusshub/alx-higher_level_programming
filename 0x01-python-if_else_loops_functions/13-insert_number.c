#include "lists.h"
/**
 * insert_node - inserts a new node in a sorted singly linked list
 *
 * @head: the head of the sorted singly linked list
 * @number: the number to fix into the sorted singly linked list
 *
 * Return: the address of the inserted new node (Success) or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *head2 = *head;
	listint_t *head3;

	if (!head)
		return (NULL);

	while (head2 != NULL)
	{
		if (head2->n > number)
			break;
		head3 = head2;
		head2 = head2->next;
	}

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = head2;
	head3->next = new_node;

	return (new_node);
}


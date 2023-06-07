#include "lists.h"

/**
  * insert_node - inserts a number into a sorted singly linked list.
  * @head: head of the struct
  * @number: the new node value
  * Return: the address of the new node, or NULL if it failed
  */



listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *tmp, *tmp2;

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	if ((*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	tmp = *head;
	tmp2 = (*head)->next;
	while (tmp2)
	{
		if (tmp2->n > number)
		{
			new_node->next = tmp2;
			tmp->next = new_node;
			return (new_node);
		}
		tmp = tmp2;
		tmp2 = tmp2->next;
	}
	if (tmp2 == NULL)
	{
		tmp2->next = new_node;
		return (new_node);
	}
	return (NULL);
}

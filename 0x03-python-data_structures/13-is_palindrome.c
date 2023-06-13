#include "lists.h"
#include <stdio.h>

/**
  * is_palindrome - check if list is palindrome
  * @head: list head
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */

int is_palindrome(listint_t **head)
{
	int i = 0, j, k, size = 0;
	listint_t *temp;

	temp = *head;
	if (!(*head) || !(*head)->next)
		return (1);

	while (temp)
	{
		size++;
		temp = temp->next;
	}

	int array[size];

	temp = *head;
	while (temp)
	{
		array[i] = temp->n;
		temp = temp->next;
		i++;
	}
	i -= 1;
	k = i;
	for (j = 0; j <= k / 2 && i >= 0; j++)
	{
		if (array[i] != array[j])
			return (0);
		i -= 1;
	}
	return (1);
}

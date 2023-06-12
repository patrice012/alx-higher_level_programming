#include "lists.h"
#include <stdio.h>

/**
  * is_palindrome - check if list is palindrome
  * @head: list head
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */

int is_palindrome(listint_t **head)
{
	int i = 0, j, **array, flag = 1, size = 0;
	listint_t *temp = *head;

	if (!(*head))
		return (flag);
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	array = (int **)malloc(sizeof(int) * size);
	if (!array)
		return (-1);
	while (temp)
	{
		array[i] = (int *)malloc(sizeof(int));
		*array[i] = temp->n;
		temp = temp->next, i++;
	}
	array[i] = NULL;
	i -= 1;
	for (j = 0; array[j] && i >= 0; j++)
	{
		if (*array[j] != *array[i])
			flag = 0;
		free(array[j]), free(array[i]);
		i -= 1;
	}
	while (array[j])
	{
		free(array[j]);
		j++;
	}
	free(array);
	return (flag);
}

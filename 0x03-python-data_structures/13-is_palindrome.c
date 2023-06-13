#include "lists.h"
#include <stdio.h>

/**
  * is_palindrome - check if list is palindrome
  * @head: list head
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */

int is_palindrome(listint_t **head)
{
	int i = 0, j, **array, flag = 1;
	listint_t *temp;

	if (!(*head) || !(*head)->next)
		return (flag);
	array = (int **)malloc(sizeof(int) * 1024);
	if (!array)
		return (-1);
	temp = *head;
	while (temp)
	{
		array[i] = (int *)malloc(sizeof(int));
		*array[i] = temp->n;
		temp = temp->next, i++;
	}
	array[i] = NULL;
	i -= 1;
	for (j = 0; j <= (i / 2) && i >= 0; j++)
	{
		if (*array[j] != *array[i])
		{
			flag = 0;
			break;
		}
		i -= 1;
	}
	i = 0;
	while (array[i])
	{
		free(array[i]);
		i++;
	}
	free(array);
	return (flag);
}

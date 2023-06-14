#include "lists.h"
#include <stdio.h>

void free_arr(int **arr, int size);

/**
  * is_palindrome - check if list is palindrome
  * @head: list head
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */

int is_palindrome(listint_t **head)
{
	int i = 0, j, k, size = 0, **array;
	listint_t *temp = *head;

	if (!(*head) || !(*head)->next)
		return (1);
	while (temp)
	{
		size++;
		temp = temp->next;
	}
	array = (int **)malloc(sizeof(int *) * (size + 1));
	if (!array)
		return (0);
	temp = *head;
	while (temp)
	{
		array[i] = (int *)malloc(sizeof(int));
		if (!array[i])
		{
			free_arr(array, i);
			return (0);
		}
		*(array[i]) = temp->n;
		temp = temp->next;
		i++;
	}
	array[i] = NULL;
	k = i, i -= 1;
	for (j = 0; j <= k / 2 && i >= 0; j++, i--)
	{
		if (*(array[j]) != *(array[i]))
		{
			free_arr(array, k);
			return (0);
		}
	}
	free_arr(array, k);
	return (1);
}


/**
  * free_arr - free an array
  * @array: array
  * @k: index
  */

void free_arr(int **array, int k)
{
	int j = 0;

	for (j = 0; j < k; j++)
		free(array[j]);
	free(array);
}


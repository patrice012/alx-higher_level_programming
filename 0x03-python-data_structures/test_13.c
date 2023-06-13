#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * test_1 - test
  */

void test_1(void)
{
	listint_t *head;

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 42);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 1);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	free_listint(head);
}



/**
  * test_2 - test
  */

void test_2(void)
{
	listint_t *head;

	head = NULL;
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 0);
	add_nodeint_end(&head, 42);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 727);
	add_nodeint_end(&head, 0);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 98);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	free_listint(head);
}




/**
 * test_3 - test
 */

void test_3(void)
{
	listint_t *head;

	head = NULL;
	add_nodeint_end(&head, 8);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 0);
	add_nodeint_end(&head, 72);
	add_nodeint_end(&head, 72);
	add_nodeint_end(&head, 0);
	add_nodeint_end(&head, 8);
	add_nodeint_end(&head, 50);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	free_listint(head);
}

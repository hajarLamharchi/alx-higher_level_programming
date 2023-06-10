#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse - reverse a listint_t list
 * @head: point to head of the list to reverse
 * Return: the reversed listint_t list
 */
listint_t *reverse(listint_t *head)
{
	listint_t *p1 = NULL;
	listint_t *p2 = NULL;

	while (head != NULL)
	{
		p2 = head->next;
		head->next = p1;
		p1 = head;
		head = p2;
	}
	head = p1;
	return (head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head of listint_t list
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *second_list = NULL;
	int status = 1;
	listint_t *node1 = NULL, *node2 = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		if (fast == NULL)
		{
			second_list = slow->next;
			break;
		}
		if (fast->next == NULL)
		{
			second_list = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	slow->next = NULL;
	second_list = reverse(second_list);
	node1 = *head;
	node2 = second_list;
	while (node1 != NULL && node2 != NULL)
	{
		if (node1->n != node2->n)
		{
			status = 0;
			break;
		}
		node1 = node1->next;
		node2 = node2->next;
	}
	return (status);
}

/*
 * File: 13-is_palindrome.c
 * Author: Chidiadi E. Nwosu
 */
#include <stdlib.h>
#include <stdio.h>
#include "lists.h"


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head node of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *fast, *slow, *prev;

	if (!head || !(*head) || !(*head)->next)
		return (1);

	fast = *head;
	slow = *head;
	tmp = slow;
	prev = NULL;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		tmp->next = prev;
		prev = tmp;
		tmp = slow;
	}

	if (fast != NULL)
		slow = slow->next;

	while (prev && slow)
	{
		if (prev->n != slow->n)
			return (0);

		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}

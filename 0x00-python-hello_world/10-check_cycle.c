/*
 * File: 10-check_cycle.c
 * Author: Chidiadi E. Nwosu
 */

#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *fast, *slow;

	fast = list;
	slow = list;

	while (slow && fast && fast->next)
	{
		if (i++ != 0 && slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}

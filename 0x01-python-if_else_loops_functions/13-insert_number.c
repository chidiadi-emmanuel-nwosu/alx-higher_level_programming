/*
 * File: 13-insert_number.c
 * Author: Chidiadi E. Nwosu
 */

#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number in a sorted singly linked list
 * @head: pointer to the start of the list
 * @number: number to be inserted
 *
 * Return: the address of the new node, NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev, *tmp; 

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;

	if (!(*head) || ((*head)->n > number))
	{
		*head = new;
		new->next = *head;
		return (new);
	}

	tmp = *head;

	for (; tmp; tmp = tmp->next)
	{
		if (tmp->n > number)
			break;
		prev = tmp;
	}

	new->next = tmp;
	prev->next = new;

	return (new);
}

/*
 * File: 13-is_palindrome.c
 * Author: Chidiadi E. Nwosu
 */
#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

int check_pal(int *arr, int i, int j);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head node of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int i = 0, *arr;

	arr = malloc(sizeof(*arr) * 1);
	if (!head || !(*head))
		return (1);
	while (tmp)
	{
		arr = realloc(arr, sizeof(*arr) * (i + 1));
		if (!arr)
			return (0);
		arr[i++] = tmp->n;
		tmp = tmp->next;
	}
	return (check_pal(arr, 0, i - 1));
}



/**
 * check_pal - checks if a string is palindrome
 * @arr: input integer array
 * @i: start arr index
 * @j: end arr index
 *
 * Return: 1 is s is palindrome, 0 otherwise
 */

int check_pal(int *arr, int i, int j)
{
	if (arr[i] != arr[j])
		return (0);
	if (i >= j)
		return (1);
	return (check_pal(arr, ++i, --j));
}

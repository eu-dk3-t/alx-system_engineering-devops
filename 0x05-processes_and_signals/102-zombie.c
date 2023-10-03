#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int infinite_while(void);

/**
 * infinite_while - Infinite loop.
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * Function name:
 * 	main 
 * Description:
 * 	The main function that will create zombie processes..
 * Return:
 * 	 EXIT_SUCCESS.
 */
int main(void)
{
	char i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %i\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}
	infinite_while();
	return (EXIT_SUCCESS);
}

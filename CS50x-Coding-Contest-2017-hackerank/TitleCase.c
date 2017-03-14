#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(int argc, char const *argv[])
{
	char input[100];
	gets(input);
	strcat(input,"\n");
	char* word = strtok(input," ");
	while(word != NULL)
	{
		//process first word
		if(isalpha(word[0]))
		{
			if (strcmp(word,"the") != 0 && strcmp(word, "of") != 0 && strcmp(word, "and") != 0 && strcmp(word, "but") != 0)
			{
				word[0] = toupper(word[0]);
			}
		}
		printf("%s ", word);
		//next word
		word = strtok(NULL, " ");
	}
	return 0;
}
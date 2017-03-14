	#include <stdio.h>
	#include <stdlib.h>
	int main(int argc, char const *argv[])
	{
		//inputs
		int floors, rooms_per_floor, demand;
		scanf("%d", &floors);
		scanf("%d", &rooms_per_floor);
		char *input = NULL;
		char* hotel[floors];
		for (int i = 0; i < floors; i++)
		{
			input = (char *) malloc(sizeof(char) * rooms_per_floor+1);
			scanf("%s", input);
			hotel[i] = input;
		}
		scanf("%d", &demand);
		int vacant = 0;
		if (demand > rooms_per_floor)
		{
			printf("0\n");
			return 0;
		}
		else
		{
			for (int i = 0; i < floors; i++)
			{
				vacant = 0;
				for (int j = 0; j < rooms_per_floor; j++)
				{
					if (hotel[i][j] == '0')
					{
						vacant++;
					}
					else
					{
						if (vacant >= demand)
						{
							printf("1\n");
							return 0;
						}
						vacant = 0;
					}
				}
				if (vacant >= demand)
				{
					printf("1\n");
					return 0;
				}
			}
			printf("0\n");
		}
		return 0;
	}

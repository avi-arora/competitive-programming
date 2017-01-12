#include <stdio.h>
int main(int argc, char const *argv[])
{
	int no_of_fish, no_of_days;
	scanf("%d", no_of_fish);
	scanf("%d", no_of_days);
	int days[no_of_days];
	for (int i = 0; i < no_of_days; ++i)
	{
		scanf("%d", days[i]);
	}
	for (int i = 0; i < no_of_days; ++i)
	{
		no_of_fish = no_of_fish - days[i];
		if (no_of_fish < 0)
		{
			printf("%d\n", i);
			return 0;
		}
	}
	printf("Happy Cat!\n");
	return 0;
}
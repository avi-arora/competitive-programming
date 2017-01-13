#include <stdio.h>
#include <string.h>
int getValue(const char num)
{
	int val;
	switch(num)
	{
		case 'I': val = 1;		break;
		case 'V': val = 5;		break;
		case 'X': val = 10;	 	break;
		case 'L': val = 50;	 	break;
		case 'C': val = 100;	break;
		case 'D': val = 500;	break;
		case 'M': val = 1000; 	break;
		default:  val = -1;
	}
	return val;
}

int evaluate(const char *roman)
{
	int input_length = strlen(roman);
	int value_a = 0, value_b = 0, temp_sum = 0, sum = 0;
	if (input_length == 1)
	{
		sum = getValue(roman[0]);
	}
	else
	{

		if(input_length % 2 == 0)
		{
			for (int i = 0; roman[i] != '\0'; i += 2)
			{
				value_a = getValue(roman[i]);
				value_b = getValue(roman[i+1]);
				if (value_b  > value_a)
				{
					temp_sum = value_b - value_a;
				}
				else
				{
					temp_sum = value_a + value_b;
				}
				sum += temp_sum;
			}
		}
		else
		{
			//if length is odd move two character at a time, untill one left.
			int i = 0;
			for (; roman[i] != '\0';)
			{
				value_a = getValue(roman[i]);
				value_b = getValue(roman[i+1]);
				if (value_b > value_a)
				{
					temp_sum = value_b - value_a;
				}
				else
				{
					temp_sum = value_a + value_b;
				}
				sum += temp_sum;
				i += 2;
				if (roman[i+1] == '\0')
				{
					break;
				}
			}
			sum += getValue(roman[i]);
		}
	}
	return sum;
}
int main(int argc, char const *argv[])
{
	char input[100];
	gets(input);
	printf("%d\n", evaluate(input));
	return 0;
}
#include <stdio.h>
int main(int argc, char const *argv[])
{
	float a_x, a_y, a_w, a_h;
	float b_x, b_y, b_w, b_h;
	float area = 0.0;
	scanf("%f%f%f%f", &a_x, &a_y, &a_w, &a_h);
	scanf("%f%f%f%f", &b_x, &b_y, &b_w, &b_h);
	float a_xx = a_x + a_w;
	float a_yy = a_y + a_h;
	float b_xx = b_x + b_w;
	float b_yy = b_y + b_h;
	if (a_x <= b_xx && b_x <= a_xx && a_y <= b_yy && b_y <= a_yy)
	{
	
		if (a_xx < b_xx)
		{
			area = (a_xx - b_x) * (a_yy - b_y);
		}
		else 
		{
			area = (b_xx - a_x) * (b_yy - a_y);
		}
	}
	else
	{
		area = 0.00;
	}
	printf("%.2f\n", area);
	return 0;
}
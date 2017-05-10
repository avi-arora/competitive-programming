#include<cs50.h>
#include<stdio.h>
int main (void)
{
   int height;
   do 
   { 
      printf("welcome to mario, please Enter the height : ");
      height = GetInt();
   }
   while ( height > 23 || height < 0 );
   int column, space, row;
   for ( column = 1 ; column <= height ; column++ )
   {
      for ( space = 1 ; space <= height - column ; space++ )
      {
         printf(" ");
      }
      printf("#");
      for ( row = 1 ; row <= column ; row++ )
      {
         printf("#");
      }
      printf("\n");
   }
}

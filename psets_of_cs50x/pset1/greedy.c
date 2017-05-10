#include<cs50.h>
#include<math.h>
#include<stdio.h>
int main (void)
{
   double money;
  do 
   {
      printf("enter the ammount of money you owe: ");
      money = GetDouble();
   }
   while ( money <= 0 );
   money = money * 100;
   int rounded = round(money);
   int quatr = 25 , dime = 10 , nickl = 5 , penni = 1 , coins = 0;
   while ( rounded >= quatr )
   {
      rounded = rounded - quatr;
      coins = coins + 1;
   }
   while ( rounded >= dime )
   {
      rounded = rounded - dime;
      coins = coins + 1;
   }
   while ( rounded >= nickl )
   { 
      rounded = rounded - nickl;
      coins = coins + 1;
   }
   while ( rounded >= penni )
   {
      rounded = rounded - penni;
      coins = coins + 1;
   }
   printf("%d\n", coins);  
}

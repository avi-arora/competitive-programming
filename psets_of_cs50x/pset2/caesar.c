/*
 **********************************************************************************************************************************************
 * This is cs50.
 * 
 * problem set - 2.
 * crypto
 *
 * caesar.c
 * By - Avishek arora
 * Created on 22-7-2014.
 *
 **********************************************************************************************************************************************
 */
#include<cs50.h>
#include<ctype.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main ( int argc , string argv [] )
{
   if ( argc != 2 )
   {
      printf("correct usage ./caesar <key>\n");
      return 1; //Quit the program.
   }
   string ptext = GetString();
   int key = atoi ( argv [1] ); //Converts the string\char into an integer value.
   int ctext;
   for ( int text = 0 , l = strlen ( ptext ) ; text < l ; text++ )
   {
      if ( isalpha (ptext[text]) ) // Checks weather entered string is alphabetical or not.
      {
         if ( isupper( ptext[ text ] ) ) // For all upper case alphabets.
         {
            ctext = ( ( ptext[ text ] - 'A' ) + key ) % 26;
            printf("%c", ctext + 'A' );
         }
         else if ( islower( ptext[ text ] ) ) // For all lower case alphabets.
         {
            ctext = ( ( ptext[text] - 'a' ) + key ) % 26;
            printf("%c", ctext + 'a' );
         }
      }
      else // For numbers, special symbol and others.
      printf("%c", ptext[text] );
   }
   printf("\n");
}        

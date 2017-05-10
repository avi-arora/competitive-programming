/*
 **********************************************************************************************************************************************
 * This is cs50.
 * 
 * Problem set - 2.
 * crypto
 * 
 * vigenere.c 
 * by Avishek Arora
 * Created on - 27-07-2014
 * 
 **********************************************************************************************************************************************
*/
 
#include<cs50.h>
#include<ctype.h>
#include<stdio.h>
#include<string.h>
int main ( int argc , string argv [] )
{
   if ( argc != 2 )
   {
      printf("correct usage ./vigenere <key>\n");
      return 1;  //Quit the program.
   }
   string key = argv[1];
   int size = strlen( key );
   for ( int i = 0 ; i < size ; i++ )
   {
      if ( ! isalpha( key[i] ) ) // If not alphabetical.
      {
         printf("Keyword must only be letters A-Z and a-z\n");
         return 1; 
      }
   }
   string ptext = GetString(); // Get plaintext from the user.
   int ctext;  // Cipher text.
   for ( int text = 0 , k = 0 , length = strlen( ptext ) ; text < length && k < length ; text++ ) // Keep track of plaintext and key.
   {
      if ( ! isalpha( ptext[text] ) ) 
      {
         printf("%c", ptext[text] );
      }
      else 
      {
         if ( isupper( key[ k % size ] ) ) 
         {
            if ( isupper( ptext[ text ] ) )
            {
               ctext = ( ( ptext[ text ] + key[ k % size ] ) - 130 ) % 26; // If key and plaintext is UPPER CASE.
               printf("%c", ctext + 'A' );
            }
            else 
            {
               ctext = ( ( ( ptext[ text ] + key[ k % size ] ) + 32 ) - 194 ) % 26; // If key is UPPER but plaintext is lower case.
               printf("%c", ctext + 'a' );
            }
            k++;  // Increment index of key.
         }
         else
         {
            if ( islower( ptext[ text ] ) ) 
            {
               ctext = ( ( ptext[ text ] + key[ k % size ] ) - 194 ) % 26;  // If key and plaintext is lower case.
               printf("%c", ctext + 'a' );
            }
            else
            {
               ctext = ( ( ( ptext[ text ] + key[ k % size ] ) - 32 ) - 130 ) % 26;  // If key is lower but plaintext is UPPER CASE.    
               printf("%c", ctext + 'A' );
            }
            k++;
         }
      }
   }
   printf("\n");
}

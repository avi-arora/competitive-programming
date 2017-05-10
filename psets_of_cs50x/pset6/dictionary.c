/****************************************************************************
 * dictionary.c
 *
 * Computer Science 50
 * Problem Set 6
 *
 * Implements a dictionary's functionality.
 ***************************************************************************/

#include <stdbool.h>
// ading standard libraries 
#include<ctype.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>


#include "dictionary.h"

int count = 0 ;

// creating a node for saving words
typedef struct node
{
   char word [ LENGTH + 1 ] ;
   struct node* next ;
} node ;

int hshfunc ( node* temp ) ;
// creating globally accessable table
node* wrdtble [ 25 ] ;

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char* word)
{
    // Check the spelling of any word in the text file 
      // obtain the hash value
      int key = 0 ;
      if ( islower ( word [ 0 ] ) ) 
      {
         key = word [ 0 ] - 'a' ;
      }
      else if ( isupper ( word [ 0 ] ) ) 
      {
         key = word [ 0 ] - 'A' ;
      } 
       char wrd [ LENGTH + 1 ] ;
       strcpy ( wrd , word );
       int size = strlen ( wrd ) ;
       for ( int i = 0 ; i <= size ; i++ ) 
       {
          if ( isupper ( wrd [ i ] ) )
          {
             wrd [ i ] = tolower ( wrd [ i ] ) ;
          }
       }
     // search for that value in the table 
                     // condition for word not in table and not matched
       if ( wrdtble [ key ] == NULL ) 
       {
          return false ;
       }
                     node* temp = wrdtble [ key ] ;
                     while ( temp -> next != NULL && strcmp ( temp -> word , wrd  ) != 0 )
                     {
                        temp = temp -> next ;
                     }
                     if ( strcmp ( temp -> word , wrd  ) == 0 ) 
                     {
                        return true ;
                     }
                     else
                     {
                        return false ;
                     }
        return false ;
        free ( temp ) ;
}

/**
 * Loads dictionary into memory.  Returns true if successful else false.
 */
bool load(const char* dictionary)
{
    // Load the dictionary into the memory
    if ( dictionary == NULL ) 
    {
       return false ;
    }
    FILE* words = fopen ( dictionary , "r" ) ;
    if ( words == NULL )
    {  
       free ( words );
       return false;
    }
    for ( int i = 0 ; i < 26 ; i++ ) 
         wrdtble [ i ] = NULL ;
    
    // storing word 
      while ( 1 ) 
      {
         node* temp = malloc ( sizeof ( node ) ) ;
         if ( fscanf ( words , "%s" , temp -> word ) == EOF ) 
         {  free ( temp ) ; 
            fclose(words);
            return true ;
         }
         int key = hshfunc ( temp ) ;
         if ( wrdtble [ key ] == NULL ) 
         {
            temp -> next = NULL ;
            wrdtble [ key ] = temp ;
         }
         else
         {
            temp -> next = wrdtble [ key ] ;
            wrdtble [ key ] = temp ;
         }
         temp = NULL ;
         free ( temp ) ;
         count++;

      }
      free ( words ) ;
      return false;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
   if ( count > 0 ) 
       return count ;
    else
       return 0;
}

/**
 * Unloads dictionary from memory.  Returns true if successful else false.
 */
bool unload(void)
{
    // clears the memory from the ram , using by the program while executing
    for ( int key = 0 ; key < 26 ; key++ )
    {
    
       if ( wrdtble [ key ] == NULL ) 
       {
          continue;
       } 
       else
       {  
          // assign to the linked list head
          node* move = wrdtble [ key ] ;
          // removing the memory
          while ( move != NULL ) 
          {
             node* temp = move ;
           /*  if ( move -> next == NULL ) 
             {
                free ( temp ) ;
             }
             else
             { */
                move = move -> next ;
                free ( temp ) ;
           // } 
          }
         free ( move ) ;
       }
    }
      return true; 
}
/**
 * hashing the key and gives the value
 */

int hshfunc ( node* temp ) 
{
    int key ;
    if ( isupper( temp -> word[ 0 ]  ) ) 
    {
         key = temp -> word [ 0 ] - 'A' ; 
    }
    else
    {
        key = temp -> word [ 0 ] - 'a' ;
    }
   return key ;
}

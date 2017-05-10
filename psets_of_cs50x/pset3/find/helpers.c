/**
 * helpers.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Helper functions for Problem Set 3.
 */
       
#include <cs50.h>

#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    // Binary search.
    int max = n;
    int min = 0;
    for ( int i = 0 ; i < n ; i++ )
    {
       int middle = ( ( max + min )/ 2 ); // go to the middle of the array. 
       if ( values[ middle ] == value ) // found the value in middle .  
       {
          return true;
          break;
       }
       else if ( values[ middle ] < value )
       {
          min = middle + 1;
       }
       else if ( values[ middle ] > value )
       {
          max = middle - 1;
       }
    }
    return false;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    // selection sort.
    for ( int i = 0 ; i < ( n - 1 ) ; i++ ) 
    {
       int min = i;
       for ( int j = ( i + 1 ) ; j < n ; j++ )
       {
          if ( values[j] < values[ min ] )
          {
             min = j;
          }
       }
       if ( min != i ) // if number is not equals i. swap numbers.
       {
           int temp = values[min];
           values[min] = values[i];
           values[i] = temp;
       }
    }
}

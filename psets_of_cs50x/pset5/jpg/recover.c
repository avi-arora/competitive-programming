/* Source file name - recover.c
 * Executable file name - recover 
 * Created by - Avishek Arora
 * on - 02 - oct - 2014 
 * Email - Avi.Arora25@gmail.com
 * Submitted to - David j malan , Harvard University 
 * 
 * Programs that recover's jpeg or jpg file from a memory portion or foriensic image of compact flash memory card
 *
 *
 *
*/

// including standard libraries 
#include<stdio.h>
#include<stdint.h>
#include<stdlib.h>

typedef uint8_t BYTE ;

// defining jpg section according to FAT system 
#define BLOCKSIZE 512 

int main ( void ) 

{
   // opens the memory card file or say the forensic image of the card 
   FILE* cfcard = fopen ( "card.raw" , "r" ) ;

   // check that the file is open correctly 
   if ( cfcard == NULL ) 
   {
      printf("memory card does'nt open correctly\ninsufficient memory\n");
      return 1 ;
   } 

   // create a buffer 
   BYTE buffer [ BLOCKSIZE ] ;

   //counter for the no: of images
   int images = -1 ;

   // file name array
   char title [ 8 ] ;

   // declaring the file 
   FILE* photo = NULL ;
           
           // reading raw from the card
   while ( fread ( &buffer , sizeof ( BYTE ) , BLOCKSIZE , cfcard ) == BLOCKSIZE ) 
   {

      // ensure the signature's 
      if ( ( buffer [ 0 ] == 0xff && buffer [ 1 ] == 0xd8 && buffer [ 2 ] == 0xff ) && ( buffer [ 3 ] == 0xe0 || buffer [ 3 ] == 0xel ) )
      {
         
         // update's the images bcuz found a jpeg
         images++ ;

         if ( photo != NULL ) 
         {
            // closing any previously opened file 
            fclose ( photo ) ;

            // creates a new file 
            sprintf( title , "%.3d.jpg" , images ) ;
         }
         else
         sprintf( title , "%.3d.jpg" , images ) ;

         // opens the images 
         photo = fopen ( title , "a" ) ;


      }
      if ( images >= 0 ) 
      {  
        fwrite ( &buffer , sizeof ( BYTE ) , BLOCKSIZE , photo ) ;
      }
   }

    // close any onened file
    fclose ( photo ) ;
   
   // that's all 
   return 0 ;
}

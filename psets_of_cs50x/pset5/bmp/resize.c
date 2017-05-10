/**
 * resize
 *
 * resize.c
 *
 * Computer Science 50
 * Problem Set 5
 *
 * stretch the BMP picture by a factor of n 
 */
       
#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char* argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        printf("Usage: ./resize n infile outfile\n");
        return 1;
    }

    int size = atoi ( argv [ 1 ] ) ;

    if ( size < 1 || size > 100 ) 
    {
       printf("invalid size\n");
       return 2;
    }

    // remember filenames
    char* infile = argv[2];
    char* outfile = argv[3];

    // open input file 
    FILE* inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 3;
    }

    // open output file
    FILE* outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 4;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf ;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // file new headers 
    BITMAPFILEHEADER bf_new = bf ;

    BITMAPINFOHEADER bi_new = bi ;

    // updating new headers 
    bi_new.biSize = bi.biSize;
    bi_new.biWidth = size * bi.biWidth ;
    bi_new.biHeight = size * bi.biHeight ;
    
    int padding_new = ( 4 - ( ( bi_new.biWidth * sizeof ( RGBTRIPLE ) ) % 4 ) ) % 4;
    int padding_old = ( 4 - ( bi.biWidth * sizeof ( RGBTRIPLE ) ) % 4 ) % 4 ; 


    // totol size of image in bytes including the pixels and padding 

    bi_new.biSizeImage = ( sizeof ( RGBTRIPLE )  *  bi_new.biWidth * bi_new.biWidth ) + ( padding_new * bi_new.biWidth ) ; 



    // updating file headers
    // new size fileheader 
    bf_new.bfSize =  sizeof ( bf ) + sizeof ( bi ) + ( ( sizeof ( RGBTRIPLE ) * bi_new.biWidth + padding_new ) * bi_new.biWidth ) ; 




    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || 
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }
      // write the bitmap file header 
      fwrite ( &bf_new , sizeof ( BITMAPFILEHEADER ) , 1 , outptr ) ;
      
      // write the bitmap info header
      fwrite ( &bi_new , sizeof ( BITMAPINFOHEADER ) , 1 , outptr ) ;

      for ( int i = 0 , biHeight = abs ( bi.biHeight )  ; i < biHeight ; i++ ) 
      {

         for ( int j = 0 ; j < size  ; j++ ) 
         {
            for ( int k = 0 ; k < bi.biWidth ; k++ ) 
            {
               // temp storage 
               RGBTRIPLE triple ;

               //read pixels for the infile 
               fread ( &triple , sizeof ( RGBTRIPLE ) , 1 , inptr ) ;
               for ( int l = 0 ; l < size ; l++ ) 
               {
                  fwrite ( &triple , sizeof ( RGBTRIPLE ) , 1 , outptr ) ;
               }

            }
               // skip over padding 
               fseek ( inptr , padding_old , SEEK_CUR ) ;
            
               // add padding 
               for ( int m = 0 ; m < padding_new ; m++ ) 
               {
                  fputc ( 0x00 , outptr ) ;
               }

               fseek ( inptr , - ( bi.biWidth * 3 + padding_old ) , SEEK_CUR ) ;
         }
         fseek ( inptr , bi.biWidth * 3 + padding_old , SEEK_CUR ) ;
    }
    
    //closing both files 
    fclose ( inptr ) ;
    fclose ( outptr ) ;

    return 0 ;
}



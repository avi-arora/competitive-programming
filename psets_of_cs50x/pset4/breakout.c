//
// breakout.c
//
// Computer Science 50
// Problem Set 4
//

// standard libraries
#define _XOPEN_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Stanford Portable Library
#include "gevents.h"
#include "gobjects.h"
#include "gwindow.h"

// height and width of game's window in pixels
#define HEIGHT 600
#define WIDTH 400

// paddle height and width of game in pixels
#define paddle_height 10
#define paddle_width  60

// number of rows of bricks
#define ROWS 5

// number of columns of bricks
#define COLS 10

// radius of ball in pixels
#define RADIUS 10

// lives
#define LIVES 3

// prototypes
void initBricks(GWindow window);
GOval initBall(GWindow window);
GRect initPaddle(GWindow window);
GLabel initScoreboard(GWindow window);
void updateScoreboard(GWindow window, GLabel label, int points);
GObject detectCollision(GWindow window, GOval ball);

int main(void)
{
    // seed pseudorandom number generator
    srand48(time(NULL));

    // instantiate window
    GWindow window = newGWindow(WIDTH, HEIGHT);

    // instantiate bricks
    initBricks(window);

    // instantiate ball, centered in middle of window 
    // avi-- function gonna return the drawing part of the ball. -- return a drawn shape of oval ball. -- remove
    GOval ball = initBall(window);

    // instantiate paddle, centered at bottom of window
    // return a drawn paddle of retangular shape. --remove return a graphical paddle.
    GRect paddle = initPaddle(window);

    // instantiate scoreboard, centered in middle of window, just above ball
    // it initiates Glabel it shows game score in graphical way( Glabel== graphical label ). -- remove
    GLabel label = initScoreboard(window);

    // number of bricks initially
    int bricks = COLS * ROWS;

    // number of lives initially
    int lives = LIVES;

    // number of points initially
    int points = 0;
   
   // move the ball at certain angles in x and y directions
    double x_direction = drand48( ) + 2 ;
    double y_direction = 1.0 + 2;
    
    waitForClick();
    // keep playing until game over
   while (lives > 0 && bricks > 0)  // this block contains all the mouse movement of paddle.
    {

         //handles the movement of the ball  
       move ( ball ,x_direction , y_direction ); 

        if ( getX ( ball ) + getWidth ( ball ) >= getWidth ( window ) )
        {
           x_direction = - x_direction ;
        }
        else if ( getX ( ball ) <= 0 )
        {
           x_direction = - x_direction ;
        }
        else if ( getY ( ball ) + getHeight ( ball ) >= getHeight ( window ) )
        {
           lives--;
           setLocation ( ball , getWidth ( window ) / 2 , getHeight ( window ) / 2 ) ;
           waitForClick ();
           
        }
        else if ( getY ( ball ) <= 0 )
        {
          y_direction = - y_direction  ; 
        }
        pause ( 10 );

        // if the event of type mouse movement
        GEvent event = getNextEvent ( MOUSE_EVENT );
        
        // handles the movement of paddle
         if ( event != NULL )
        {
           if ( getEventType( event ) == MOUSE_MOVED )
           {
              double x = ( getX( event )  - getWidth( paddle ) / 2  ) ; // get the x location of paddle
              double y = ( getHeight( window ) - getHeight( paddle ) ) / 1.09 ; // get the y location of paddle
              if ( x > 0 && x < 340 )
              {
                 setLocation( paddle , x , y ); // use to move the paddle.
              }
           }

        }

        GObject object = detectCollision ( window , ball );
        if ( object != NULL )
        {

           if ( object == paddle ) 

           {
              y_direction = - y_direction ;
              
           }
         else  if( strcmp ( getType( object ) ,"GRect") == 0 ) // detect hit , remove bricks and  update score
         {
            y_direction = - y_direction;
            removeGWindow ( window , object );
            points++; 
            bricks--;
            updateScoreboard ( window , label , points );
         } 

        }   
           
           
    }


    // wait for click before exiting
    waitForClick();

    // game over
    closeGWindow(window);
    return 0;
}

/**
 * Initializes window with a grid of bricks.
 */
void initBricks(GWindow window)
{
    // initialize the following bricks as rectengles some height will be fixed 1st = 50 
   int x = 2; 
   int i ;
   for ( i = 0 ; i < 400 ; i += 40 ) 
   {
      GRect b_row1 = newGRect ( 0 , 0 , 35 , 10 ) ;
      
      setFilled ( b_row1 , true ) ;
      setColor ( b_row1 , "BLUE") ;
       
      add ( window , b_row1 );
      setLocation ( b_row1 , x , 50 );
      x += 40 ;
   }
   x = 2 ;
   for ( i = 0 ; i < 400 ; i += 40 ) 
   { 
      GRect b_row2 = newGRect ( 0 , 0 , 35 , 10 );

      setFilled ( b_row2 , true );
      setColor ( b_row2 , "GRAY" ) ;

      add ( window , b_row2 );
      setLocation ( b_row2 , x , 65 );
      x += 40 ;

   }
   x = 2 ;
   for ( i = 0 ; i < 400 ; i += 40 ) 
   {
      GRect b_row3 = newGRect ( 0 , 0 , 35 , 10 );

      setFilled ( b_row3 , true ) ;
      setColor ( b_row3 , "ORANGE");

      add ( window , b_row3 );
      setLocation ( b_row3 , x , 80 );
      x += 40 ; 
   }
   x = 2 ;
   for ( i = 0 ; i < 400 ; i += 40 ) 
   {
      GRect b_row4 = newGRect ( 0 , 0 , 35 , 10 );

      setFilled ( b_row4 , true );
      setColor ( b_row4 , "MAGENTA" );

      add ( window , b_row4 );
      setLocation ( b_row4 , x , 95 );
      x += 40 ;
   }
   x = 2 ;
   for ( i = 0 ; i < 400 ; i += 40 )
   {
      GRect b_row5 = newGRect ( 0 , 0 , 35 , 10 );

      setFilled ( b_row5 , true );
      setColor( b_row5 , "CYAN" );

      add ( window , b_row5 );
      setLocation ( b_row5 , x , 110 );
      x += 40;
   }

}

/**
 * Instantiates ball in center of window.  Returns ball.
 */
GOval initBall(GWindow window)
{
    // creating a circle 
     GOval ball = newGOval ( 0 , 0 , 20 , 20 );

     setFilled ( ball , true );
     setColor ( ball , "BLACK");

     add ( window , ball );
     setLocation ( ball , getWidth ( window ) / 2 , getHeight ( window ) / 2 );


     return ball;
}

/**
 * Instantiates paddle in bottom-middle of window.
 */
GRect initPaddle(GWindow window)
{
    // initialize the paddle position in the middle of the application's window
    GRect paddle = newGRect( 0, 0, paddle_width, paddle_height );

    setFilled(paddle, true );
    setColor( paddle , "BLACK" );

    double x = ( getWidth ( window ) - getWidth( paddle ) ) / 2.09 ;
    double y = ( getHeight ( window ) - getHeight( paddle ) ) /1.09;
    
    add( window , paddle );
    setLocation( paddle, x, y );
    
    return paddle;


}

/**
 * Instantiates, configures, and returns label for scoreboard.
 */
GLabel initScoreboard(GWindow window)
{
    // initialize the score board 
    GLabel score_board = newGLabel ("0");
   
   setFont ( score_board , "SansSerif-40" );
   setColor ( score_board , "GRAY" );
  
   add ( window , score_board );
   setLocation ( score_board , 200 , 300 );
   
   return score_board;
}

/**
 * Updates scoreboard's label, keeping it centered in window.
 */
void updateScoreboard(GWindow window, GLabel label, int points)
{
    // update label
    char s[12];
    sprintf(s, "%i", points);
    setLabel(label, s);

    // center label in window
    double x = (getWidth(window) - getWidth(label)) / 2;
    double y = (getHeight(window) - getHeight(label)) / 2;
    setLocation(label, x, y);
}

/**
 * Detects whether ball has collided with some object in window
 * by checking the four corners of its bounding box (which are
 * outside the ball's GOval, and so the ball can't collide with
 * itself).  Returns object if so, else NULL.
 */
GObject detectCollision(GWindow window, GOval ball)
{
    // ball's location
    double x = getX(ball);
    double y = getY(ball);

    // for checking for collisions
    GObject object;

    // check for collision at ball's top-left corner
    object = getGObjectAt(window, x, y);
    if (object != NULL)
    {
        return object;
    }

    // check for collision at ball's top-right corner
    object = getGObjectAt(window, x + 2 * RADIUS, y);
    if (object != NULL)
    {
        return object;
    }

    // check for collision at ball's bottom-left corner
    object = getGObjectAt(window, x, y + 2 * RADIUS);
    if (object != NULL)
    {
        return object;
    }

    // check for collision at ball's bottom-right corner
    object = getGObjectAt(window, x + 2 * RADIUS, y + 2 * RADIUS);
    if (object != NULL)
    {
        return object;
    }

    /* no collision
      hefeflkf
      hefefk
      */
      // helloooooo
    return NULL;
}

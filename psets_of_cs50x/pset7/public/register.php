<?php 
    
        //configuration
        require("../includes/config.php");

        //if form was submitted 
        if ($_SERVER["REQUEST_METHOD"] == "POST" )
        {
           // todo

           // VALIDATING inputs
           if ( empty( $_POST["username"] ) )
           {
               //message
               apologize ("you must have a username.") ;
           }
           else if ( empty ( $_POST["password"] ) )
           {
              apologize ("you must create a password.") ;
           }
          else if ( $_POST["password"] !== $_POST["confirmation"] )
           {
              apologize ( "password does not match." ) ;
           }

           // Insert new user into database 
           $qreturn = query ("INSERT INTO users ( username , hash , cash ) VALUES ( ? , ? , 10000.0000 )" , $_POST["username"] , 
           crypt ( $_POST["password"] ) ) ;
           
             // check for update . database returns 
           if ( $qreturn === false ) 
           {
              // may be the username already exist in database
              apologize ( "username already exist." ) ;
           }

           // if successfully add to database
           $rows = query ("SELECT LAST_INSERT_ID() AS id" );
           $id = $rows [ 0 ] [ "id" ] ;

           // log the user in
           $_SESSION["id"] = $id ;
           
           // redirect to portfolio
           redirect("/");


        }
        else 
        {
           // else render form 
           render("register_form.php", [ "title" => "Register" ] );
        }

?>

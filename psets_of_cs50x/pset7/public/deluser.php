<?php
 /*
  * 
  *
  * deluser.php
  * Deletes the user from the database 
  * Works without admin login
  *
  * Created by - Avishek Arora
  * E-mail- Avi.arora25@gmail.com
  *
 */

 //if form was submitted
 // required function
    require("../includes/config.php");
 
    if ( $_SERVER["REQUEST_METHOD"] == "POST" ) 
    {
        if(isset($_POST["submit"]))
        {
            // perform the deletion operation 
            query("DELETE FROM users WHERE username = ?",$_POST["username"]);

            render("duser.php");
        }
    }
    else 
    {
        //save all the users detail in variable
      //  $usernames = query("SELECT username FROM users");
        //send username to pages where it shows all usersT
        render("duser.php");
    }

?>

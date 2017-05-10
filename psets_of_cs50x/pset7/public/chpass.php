<?php
 /*
  * 
  * changes the user password
  * 
  * Created by - Avishek arora
  * Email - Avi.arora25@gmail.com
  *
 */

        //configure page
        require("../includes/config.php");

        //validate
        if ( $_SERVER["REQUEST_METHOD"] == "POST")
        {
            if ( empty($_POST["current"] ) || empty( $_POST["new"] ) || empty( $_POST["confirm"] ) ) 
            {
                apologize("Please fill up all fields.");
            }

            if ( $_POST["new"] !== $_POST["confirm"] ) 
            {
                apologize("Password not matched.");
            }

            $current = query("SELECT * FROM users WHERE id = ?",$_SESSION["id"] ) ;
             
            $cur = $current[0];
            if ( crypt($_POST["current"] , $cur["hash"] ) !== $cur["hash"] ) 
            {
                apologize("Incorrect Current Password.");
            }

            //change password
            query("UPDATE users SET hash = ? WHERE id = ? ", crypt($_POST["new"] ) , $_SESSION["id"] ) ;

            redirect("index.php");
        }
        else
        {
            render("cpass.php");
        }


?>

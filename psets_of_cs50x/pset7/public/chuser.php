<?php
 /*
  * changes the Username of the current user
  *
  * Created by - Avishek arora
  * Email - Avi.arora25@gmail.com
  *
*/
        //configure file
        require("../includes/config.php");

        // validation
        if ($_SERVER["REQUEST_METHOD"] == "POST" ) 
        {
            if ( empty($_POST["newusername"]) ) 
            {
                apologize("Please Enter the Username.");
            }
            if ( empty($_POST["cusername"] ) ) 
            {
                apologize("Please Confirm Username.");
            }
            if ( $_POST["newusername"] !== $_POST["cusername"] )
            {
                apologize("both Username must be same.");
            }
            
            // change username
            query("UPDATE users SET username = ? WHERE id = ?",$_POST["cusername"] , $_SESSION["id"] ) ;

            redirect("index.php");
        }
        else
        {
            render("cuser.php");
        }




?>

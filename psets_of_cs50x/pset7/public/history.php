<?php
/*
 * 
 * history.php 
 * Shows the history of every transaction in the user profile
 *
 * Created by - Avishek Arora
 * Email - Avi.arora25@gmail.com
 *
*/
        //configure the page
        require("../includes/config.php");

        // get the history data 
        $history = query("SELECT type , time , symbol , shares , price FROM history WHERE id = ?", $_SESSION["id"]);


        // arrange data in array

        
        // temporay action
        render("history_show.php",[ "history" => $history ] );





?>



<?php
/*
 * 
 *
 * sell.php - implement a selling algorithm for sell stocks
 * created by - Avishek Arora
 *
 *
*/ 
    //uses inbuild functions for rendering and other things
    require("../includes/config.php");
        
    // get the user's stock data ( stock owned by user's ) 
    $stocks = query("SELECT symbol, shares FROM stocks WHERE id = ?",$_SESSION["id"] ) ;

    // render information
    render("sell_stock.php", [ "stocks" => $stocks ] ) ;
?>




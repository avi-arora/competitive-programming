<?php
        //requires files 
        require("../includes/functions.php");

       if ($_SERVER["REQUEST_METHOD"] == "POST" )
       {

          if (!empty($_POST["symbol"] ))
          {
            if ( htmlspecialchars ( $_POST["symbol"] ) )
            {
                

                //search for a valid stock
                $stock = lookup($_POST["symbol"] ) ;
            
            
                if ($stock === false ) 
                {
                apologize("please enter Valid symbol.");
                }
                else
                {
                        render("quote_result.php",[ "stock" => $stock ] );
                }

            }

                else
                {
                      apologize("Please Enter any symbol.");
                }
            } 
       }
       else 
       {
          render("quote_search.php" ) ;
       }
?>


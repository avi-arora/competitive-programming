<?php
/*
 * 
 * 
 *  working of buying stocks from the exchange.
 * 
 * Created by - Avishek Arora
 * email - Avi.arora25@gmail.com
 *
*/
        require("../includes/config.php");

        if($_SERVER["REQUEST_METHOD"] == "POST") 
        {
            if ( !empty($_POST["symbol"]) && !empty($_POST["shares"]))
            {

                if ( !empty($_POST["symbol"]) )
                    {
                        if ( !empty($_POST["shares"] )) 
                        {
    
                            if ( htmlspecialchars ($_POST["symbol"] ) && htmlspecialchars ( $_POST["shares"] )) 
                            {
                                $quantity = $_POST["shares"] ;
                                // check for valid no: of shares ( share should be a non-negative integer ) 
                                $check = preg_match("/^\d+$/",$_POST["shares"] ); 
                                 
                                 if ($check == false ) 
                                 {
                                    apologize("You can only buy whole shares of stock");
                                 }
                                
                                // check for the users stock
                                $stock_check = lookup($_POST["symbol"]);
                                if ( $stock_check === false ) 
                                {
                                    // print error message
                                    apologize("Invalid stock symbol.");
                                }
                                else
                                {
                                    // later functionality
                                     // for checking weather the users can afford the shares
                                    $current_cash = query("SELECT cash FROM users WHERE id = ?",$_SESSION["id"] ) ;
                                    
                                    // user stock request ( cash value for buy that stock ) 
                                    $stock_buy = $stock_check["price"] * $quantity ;

                                    if ( $current_cash[0]["cash"] < $stock_buy ) 
                                    {
                                        // message of insufficient balance
                                        apologize("you do not have much cash to buy.");
                                    }
                                     //update the database
                                        
                                        if ( ctype_lower($_POST["symbol"]) )
                                        {
                                            $stock_symbol = strtoupper($_POST["symbol"] ) ;
                                        }
                                        else
                                        {
                                            $stock_symbol = $_POST["symbol"] ;
                                        }
                                        
                                    // checking query
                                    query("INSERT INTO stocks ( id , symbol , shares ) VALUES ( ? , ? , ? ) ON DUPLICATE KEY UPDATE shares =
                                    shares + VALUES(shares)",$_SESSION["id"] , $stock_symbol , $_POST["shares"] ) ;

                                    // update cash
                                    query("UPDATE users SET cash = cash - ? WHERE id = ? " , $stock_buy , $_SESSION["id"]);

                                    // update history of users
                                    query("INSERT INTO history ( id , type , time , symbol , shares , price ) VALUES ( ? , 'BUY' , CURRENT_TIMESTAMP , ? , ? , ?)", $_SESSION["id"] , $stock_symbol , $_POST["shares"] , $stock_buy );

                                    // redirect to home
                                    redirect("index.php");
                                }
                                    
                            }
                        }
                        else
                        {
                                apologize("please enter number of shares.");
                        }
                    }   
                else
                {
                    apologize("Please enter any symbol.");
                }

            }
            else
            {
                apologize("Please fill information.");
            }
        }
        else 
        {
            render("buy_form.php");
        }
?>

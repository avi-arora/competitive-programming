<!-- sold the stock and update the user's portfolio
 *
 * 
 * stock_sold.php
 *
 * Created by - Avishek Arora
 *
 *
-->
<!-- <div id="middle"> -->
        
    <?php
            require("../includes/config.php");

            // deletes the user's stock own and update the cash balance.
            $stock = lookup($_POST["stocks"]);
            
            // get how much a person own ( cash value of stock ) 
            if ( $stock !== false )
            {
                $shares = query("SELECT shares FROM stocks WHERE id = ?",$_SESSION["id"] ) ;
                $stockvalue = $shares[0]["shares"] * $stock["price"] ;
                //update the current cash and delete the stocks 
                        
                        // conver to transaction START TRANSACTION { 
                        query("UPDATE users SET cash = cash + ? WHERE id = ?",$stockvalue , $_SESSION["id"]);

                        query("DELETE FROM stocks WHERE id = ? AND symbol = ?",$_SESSION["id"] ,$_POST["stocks"] );
                        // finish transaction COMMIT; }
                        
                        //update history of user
                        query("INSERT INTO history ( id , type , time , symbol , shares , price ) VALUES ( ? ,'SELL' , CURRENT_TIMESTAMP , ? , ? , ? )",$_SESSION["id"] , $_POST["stocks"] , $shares[0]["shares"] , $stockvalue ) ;

                        //show profile
                       redirect("index.php");
            }
            else
            {
                redirect("index.php");
            }
    ?>
<!-- </div> -->



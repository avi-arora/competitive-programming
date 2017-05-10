<div id="user">
    </br>
    <?php
        print("<h3>Welcome ,  ".$user[0]["username"]."</h3>");
    ?>
            
<div id="middle">
    </br>
    </br>
    <ul class="navbar" >
        <li><a href="quote.php">Qoute</a></li>
        <li><a href="buy.php">Buy</a></li>
        <li><a href="sell.php">Sell</a></li>
        <li><a href="history.php">History</a></li>
        <li><a href="settings.php">Settings</a></li>
        <li><a href="logout.php"><strong>Logout</strong></a></li>
    </ul>
</div>
<div id="portfolio">
    <table class="table table-striped">
        <thead>
            <tr>
            <th>Symbol</th>
            <th>Name  </th>
            <th>Shares</th>
            <th>Price </th>
            <th>Total </th>
            </tr>
        </thead>
      <tbody align="left"> 
                <?php
                       
                    foreach ( $positions as $position ) 
                    {
                        $total = $position["shares"] * $position["price"] ;
                        
                        print("<tr>");
                        print("<td>".$position["symbol"] . "</td>");
                        print("<td>".$position["name"]  . "</td>");
                        print("<td>".$position["shares"] . "</td>");
                        print("<td>".number_format($position["price"],2) . "</td>");
                        print("<td>".number_format($total,2)."</td>");
                        print("</tr>");
                    }
                ?>
                <?php ?>
                <tr>
                <td colspan="4"> CASH $ </td>
                <td> <?=number_format($cash[0] ["cash"],2); ?> </td>
                </tr>
                <?php ?>
        
        <!-- info related portfolio -->



       </tbody> 
    </table>

        



<div>
    <a href="logout.php">Log Out</a>
</div>

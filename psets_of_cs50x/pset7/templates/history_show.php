<!-- * Manages the history of every transaction. show's via html page view 
     *
     * Created by - Avishek Arora
     * Email - Avi.arora25@gmail.com
     *
-->
<div id="middle">
    </br>
    </br>
    <table class="table table-striped">
        <thead>
            <tr>
            <th>Transaction</th>
            <th>Date/Time</th>
            <th>Symbol </th>
            <th>Shares</th>
            <th>Price</th>
            </tr>
        </thead>
        <tbody align="left">
            <?php
                
                foreach( $history as $his ) 
                {
                    print("<tr>");
                    print("<td>".$his["type"]."</td>");
                    print("<td>".$his["time"]."</td>");
                    print("<td>".$his["symbol"]."</td>");
                    print("<td>".$his["shares"]."</td>");
                    print("<td>".$his["price"]."</td>");
                    print("</tr>");
                }
            ?>
        </tbody>
    </table>



</div>

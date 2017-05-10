<!-- creates the structure of the page sell using dynamic entry 
  *
  * 
  * sell_stock.php
  * Created by - Avishek Arora
  *
  *
-->
<form action="stock_sold.php" method="post" >
<fieldset>
<div id="middle">
    </br>
    </br>
    <select name="stocks" class="form-control">
        <?php   ?>
           <!-- 1st option void -->
            <option value=""></option>

        <? foreach ( $stocks as $stock ) : ?>
            
            <option value="<?= $stock["symbol"] ?>"><?= $stock["symbol"] ?> </option>
        <?php endforeach  ?>
    </select>
    <div class="form-group">
    </br>
    <button type="submit" class="btn btn-default">Sell</button>
</div>
</fieldset>
</form>

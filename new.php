<html>
<head>
         <title>NYSE Most Active Stocks  </title>
</head>
<body>
<?php
ini_set('display_errors', 'On');
error_reporting(E_ALL);

$cnx=mysqli_connect("localhost","root","xxx")or die("Could not connect: " . mysqli_error());
mysqli_select_db($cnx,"demo") or die("Could not select database");


echo "<table align=center>\n";
$query = "SHOW COLUMNS FROM nyexchange";
$result = mysqli_query($cnx,$query) or die($query." query failed: ".mysqli_error());
echo "\t<tr>\n";
while($row = mysqli_fetch_assoc($result)) {
    echo "\t\t<td><b>$row[Field]</b></td>\n";

}
echo "\t</tr>\n";

$query = "SELECT * FROM nyexchange";
$result = mysqli_query($cnx,$query) or die($query." query failed: ".mysqli_error());


while($row = mysqli_fetch_assoc($result)) {
    echo "\t<tr>\n";
   foreach ($row as $col_value) {
        echo "\t\t<TD>$col_value</TD>\n";
    }

    echo "\t</tr>\n";
}
echo "</table>\n";
?>
</body>
</html>



<?php
$q = intval($_GET['q']);

$con = mysqli_connect('localhost','newuser','password','ajaxtest');
if (!$con) {
    die('Could not connect: ' . mysqli_error($con));
}

mysqli_select_db($con,"test");
$sql="INSERT INTO ajaxtest(id) VALUES (" + .$q. + ")"
mysqli_query($con,$sql);

mysqli_close($con);
?>
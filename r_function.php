<?php
echo shell_exec("Rscript my_script.r {$_GET['range']}");
// return image tag
$nocache = rand();
echo("<img src='/opt/bitnami/apache/htdocs/temp.png?$nocache' />");
?>
<?php
echo shell_exec("Rscript my_spatial_script.r {$_POST['geojson']}");
// return image tag
$nocache = rand();
echo("<img src='temp.png?$nocache' />");
?>
<?php

echo shell_exec("Rscript my_script.r {$_GET['range']}");

?>
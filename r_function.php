<?php

echo shell_exec("Rscript my_script.R {$_GET['range']}");

?>
<?php
    putenv('PATH=/usr/bin');
    ob_start();
    echo shell_exec('python python_test.py 1809145475data.geojson');
    $output = ob_get_clean();
    echo $output;
?>
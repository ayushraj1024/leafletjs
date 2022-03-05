<?php
    $nocache = rand();
    file_put_contents($nocache.'data.geojson', $_POST['geojson']);
    ob_start();
    passthru('python /opt/bitnami/apache/htdocs/python_count.py '.$nocache.'data.geojson');
    $output = ob_get_clean(); 
    echo $output;
?>
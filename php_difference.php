<?php
    ini_set('max_execution_time', 300);
    set_time_limit (300); 
    $nocache = rand();
    file_put_contents($nocache.'data.geojson', $_POST['geojson']);
    file_put_contents($nocache.'_1data.geojson',$_POST['geojson_1']);
    /*ob_start();
    passthru('python -W ignore python_standard_deviational_ellipse.py '.$nocache.'data.geojson');
    $output = ob_get_clean();
    echo $output;*/
       
    exec('python3 -W ignore python_difference.py '. $nocache .'data.geojson >'. $nocache .'stderr.log 2>' . $nocache . 'stderr.log', $out, $status);
    echo ($nocache.'difference.geojson');
?>
<?php
    ini_set('max_execution_time', 300);
    set_time_limit (300); 
    $nocache = rand();
    file_put_contents($nocache.'data.geojson', $_POST['geojson']);
    /*ob_start();
    passthru('python -W ignore python_standard_deviational_ellipse.py '.$nocache.'data.geojson');
    $output = ob_get_clean();
    echo $output;*/
       
    exec('python3 -W ignore python_voronoi_polygons.py '. $nocache .'data.geojson >'. $nocache .'stderr.log 2>' . $nocache . 'stderr.log', $out, $status);
    echo ($nocache.'voronoi.geojson');
?>
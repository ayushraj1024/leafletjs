<?php
header('Access-Control-Allow-Origin: *');
?>

<!DOCTYPE html>
<html>
  <head>
    <title>2020GI07 MNNIT Mtech Research GIS</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.draw/0.4.2/leaflet.draw.css"/>
    <style>
      body {
        padding: 0;
        margin: 0;
      }
      html, body, #map {
        height: 100%;
        width: 100%;
      }
      #overpass-api-controls {
        padding: 10px;
        background-color: rgb(255, 255, 255);
      }
      #overpass-api-controls a {
        display: inline;
      }
    </style>
  </head>
  <body>
    <div id="map">

      <!--<div class="leaflet-control-container">
        <div class="leaflet-top leaflet-right">
          <div id="overpass-api-controls" class="leaflet-bar leaflet-control">
            <input id="query-textfield" value="leisure=playground" size="50">
            <input id="query-button" type="button" value="Laden">
          </div>
        </div>
      </div>-->
    
    </div>
 
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.draw/0.4.2/leaflet.draw.js"></script>
    <script src="Leaflet.draw-develop\src\draw\handler\Draw.Polygon.js"></script>
    <script src="https://unpkg.com/osmtogeojson@2.2.12/osmtogeojson.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

    <script>
      var map = L.map('map').setView([25.320021, 82.973564], 12);
      var OSMLayer = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);

      var baseMaps = {
        "OSM Standard": OSMLayer
      };
      var overLays = {};
      var layerControl = L.control.layers(baseMaps, overLays, { collapsed: false, position: 'bottomleft'}).addTo(map);

     // FeatureGroup is to store editable layers
     var drawnItems = new L.FeatureGroup();
     map.addLayer(drawnItems);

     map.on('draw:created', function (e) {
          var type = e.layerType,
              layer = e.layer;
          var vectorLayer = {};
          if (type === 'marker') {
              vectorLayer = {
                "Marker": layer
              };
          }
          else {
            vectorLayer = {
              "Polygon": layer
            };  
          }

          // Do whatever else you need to. (save to db, add to map etc)
          //map.addLayer(layer);
          drawnItems.addLayer(layer);
          layerControl.addOverlay(layer,type);
      });

     var drawControl = new L.Control.Draw({
         edit: {
             featureGroup: drawnItems
         }
     });
     map.addControl(drawControl);

     // control that shows state info on hover
	var info = L.control();

  info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info');
    this.update();
    return this._div;
  };

  info.update = function (props) {
    this._div.innerHTML = '<h4>US Population Density</h4>' +  (props ?
      '<b>' + props.name + '</b><br />' + props.density + ' people / mi<sup>2</sup>' : 'Hover over a state');
  };

  info.addTo(map);

      function buildOverpassApiUrl(map, overpassQuery) {
        var bounds = map.getBounds().getSouth() + ',' + map.getBounds().getWest() + ',' + map.getBounds().getNorth() + ',' + map.getBounds().getEast();
        var nodeQuery = 'node[' + overpassQuery + '](' + bounds + ');';
        var wayQuery = 'way[' + overpassQuery + '](' + bounds + ');';
        var relationQuery = 'relation[' + overpassQuery + '](' + bounds + ');';
        var query = '?data=[out:json][timeout:15];(' + nodeQuery + wayQuery + relationQuery + ');out body geom;';
        var baseUrl = 'http://overpass-api.de/api/interpreter';
        var resultUrl = baseUrl + query;
        return resultUrl;
      }

      $("#query-button").click(function () {
        var queryTextfieldValue = $("#query-textfield").val();
        var overpassApiUrl = buildOverpassApiUrl(map, queryTextfieldValue);
        
        $.get(overpassApiUrl, function (osmDataAsJson) {
          var resultAsGeojson = osmtogeojson(osmDataAsJson);
          var resultLayer = L.geoJson(resultAsGeojson, {
            style: function (feature) {
              return {color: "#ff0000"};
            },
            filter: function (feature, layer) {
              var isPolygon = (feature.geometry) && (feature.geometry.type !== undefined) && (feature.geometry.type === "Polygon");
              if (isPolygon) {
                feature.geometry.type = "Point";
                var polygonCenter = L.latLngBounds(feature.geometry.coordinates[0]).getCenter();
                feature.geometry.coordinates = [ polygonCenter.lat, polygonCenter.lng ];
              }
              return true;
            },
            onEachFeature: function (feature, layer) {
              var popupContent = "";
              popupContent = popupContent + "<dt>@id</dt><dd>" + feature.properties.type + "/" + feature.properties.id + "</dd>";
              var keys = Object.keys(feature.properties.tags);
              keys.forEach(function (key) {
                popupContent = popupContent + "<dt>" + key + "</dt><dd>" + feature.properties.tags[key] + "</dd>";
              });
              popupContent = popupContent + "</dl>"
              layer.bindPopup(popupContent);
            }
          }).addTo(map);
        });
      });

    </script>
  </body>
</html>

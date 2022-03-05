async function addWFSLayerFromSDI(url,map) {
    var geojsonLayer;
    var markers = [];       

    await $.getJSON(url)
        .then(function (data) {
            geojsonLayer = L.geoJson(data, {
                pointToLayer: function (feature, latlng) {
                    var marker = L.circleMarker(latlng,{radius:2});
                    //marker.bindPopup(feature.properties.Location + '<br/>' + feature.properties.OPEN_DT);
                    markers.push(marker);
                    return marker;
                }
            }).addTo(map);
        })
        .fail(function(err){
            console.log(err.responseText)
    });

    return [geojsonLayer,markers];
}

function addLayerFromDevice() {

}
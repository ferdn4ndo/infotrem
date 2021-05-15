<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
<?
$Lat = $_GET['Lat'];
$Lon = $_GET['Lon'];
$Nome = $_GET['Nome'];
?>
<style type="text/css">
  html { height: 100% }
  body { height: 100%; margin: 0px; padding: 0px }
  #map_canvas { height: 100% }
</style>
<script type="text/javascript"
    src="https://maps.google.com/maps/api/js?libraries=panoramio&sensor=false">
</script>
<script type="text/javascript">
  function initialize() {
    var latlng = new google.maps.LatLng(<? echo $Lat; ?>, <? echo $Lon; ?>);
    var myOptions = {
      zoom: 15,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.HYBRID
    }
    var map = new google.maps.Map(document.getElementById("map_canvas"),
        myOptions);
	
//Adicionando um marcador
	var marker = new google.maps.Marker({
      		position: latlng,
		map: map,
      		title:"<? echo $Nome; ?>"
  	});

//Caso queria adicionar a camada do panoramio
//var panoramioLayer = new google.maps.panoramio.PanoramioLayer();
//panoramioLayer.setMap(map);
  
//Caso queria adicionar dados de um KML
//var ctaLayer = new google.maps.KmlLayer('http://gmaps-samples.googlecode.com/svn/trunk/ggeoxml/cta.kml');
//ctaLayer.setMap(map);


  // To add the marker to the map, call setMap();
  //marker.setMap(map);  
  }

</script>
</head>
<body onLoad="initialize()">
  <div id="map_canvas" style="width:100%; height:100%"></div>
</body>
</html>
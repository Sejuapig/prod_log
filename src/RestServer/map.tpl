<!DOCTYPE html>
<html>
  <head>
    <title>Map</title>
    <meta charset='utf-8'>
    <style>
      html, body {
        height: 600px;
        width: 600px;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
    </style>
  </head>
  <body>
  	Voici les installations de la ville choisi 
    <div id='map'></div>

    %for row in rows:
    <input type="text" style="visibility:hidden" id="lat" value="{{row[0]['latitude']}}">
    <input type="text" style="visibility:hidden" id="long" value="{{row[0]['longitude']}}">
    %end

    <script>

    var a = document.getElementById('lat').val();
    var b = document.getElementById('long').val();

		var map;
		function initMap(a, b) {
		  map = new google.maps.Map(document.getElementById('map'), {
		    center: {lat: a, lng: b},
		    zoom: 8
		  });
		}
    </script>
    <script src='https://maps.googleapis.com/maps/api/js?key=AIzaSyAJGEK80Ct4hu9WYtT5Baf0Gue8InAO9mo&callback=initMap'
        async defer></script>
  </body>
</html>
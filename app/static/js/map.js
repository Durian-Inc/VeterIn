document.addEventListener("DOMContentLoaded", function(event) {
  var amerIcon = L.icon({
    iconUrl: '/static/img/new.png',
    iconSize: [48, 48],
    iconAnchor: [15, 48],
    popupAnchor: [10, -48]
  });

  // Map object
  var map = L.map('map').setView([37.9485, -91.7715], 13);
  map.scrollWheelZoom.disable()

  // Set map source and attribution
  L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  var xhttp = new XMLHttpRequest();

  const address = window.location.protocol + "//" + window.location.hostname + ":" + window.location.port;

  navigator.geolocation.getCurrentPosition(function (position) {
    map.flyTo([position.coords.latitude, position.coords.longitude], 13);
  });

  xhttp.onreadystatechange = function() {
          if(this.readyState == 4 && this.status == 200) {
      waypoints = JSON.parse(this.responseText);
      for (var waypoint of waypoints) {
        loc = waypoint.location.split(',');
        loc[0] = Number(loc[0]);
        loc[1] = Number(loc[1]);
        L.marker(loc, {icon: amerIcon}).addTo(map).bindPopup(
          "<a href='" + address + "/organization/" + waypoint.id + "'>" +
          waypoint.name + "</a>"
        );
      }
          }
  };
  xhttp.open("GET", address + "/api/waypoints", true);
  xhttp.send();
});

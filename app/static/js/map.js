print = console.log;

// Map object
var map = L.map('map').setView([0, 0], 13);

// Set map source and attribution
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

var xhttp = new XMLHttpRequest();

const address = window.location.protocol + "//" + window.location.hostname + ":" + window.location.port;

print(address + "/api/waypoints");

xhttp.onreadystatechange = function() {
  print(this.readyState);
  print(this.status);
  print(this.responseText);
	if(this.readyState == 4 && this.status == 200) {
    waypoints = JSON.parse(this.responseText);
    for (var waypoint of waypoints) {
      loc = waypoint.location.split(',');
      loc[0] = Number(loc[0]);
      loc[1] = Number(loc[1]);
      L.marker(loc).addTo(map).bindPopup(
        "<a href='" + address + "/organization/" + waypoint.id + "'>" +
        waypoint.name + "</a>"
      );
    }
	} else {
		print("rip you done got wackoed");
	}
};
xhttp.open("GET", address + "/api/waypoints", true);
xhttp.send();

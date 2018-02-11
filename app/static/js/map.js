print = console.log;

// Map object
var map = L.map('map').setView([51.505, -0.09], 13);

var xhttp = new XMLHttpRequest();

xhttp.open("GET", window.location.hostname + "/api/waypoints", true);
xhttp.onreadystatechange = function() {
	if(this.readyState == 4 && this.status == 200) {
		waypoints = JSON.parse(this.responseText);
	}
	else {
		print("rip you done got wackoed");
	}
};

// Set map source and attribution
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

print = console.log;
// Map object
var map = L.map('map').setView([51.505, -0.09], 13);

// Set map source and attribution
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);
// Add geocoder
geocoder = L.Control.geocoder().addTo(map);

print(L.Control.Geocoder());

geocoder.geocoder.geocode("help")

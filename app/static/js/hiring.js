var body;
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      body = JSON.parse(xhttp.responseText);

      for (var i of body) {
        var hire = document.createElement("li");

        var hireImage = document.createElement("img");
        hireImage.src = "/static/img/" + i.image;
        hireImage.className = "hire___image";

        var hireName = document.createElement("h3");
        var name = document.createTextNode(i.name);

        var hireSub = document.createElement("h5");
        if (i.years_served) {
          var sub = document.createTextNode("Years Served: " + i.years_served);
        } else if (!i.profit) {
          var sub = document.createTextNode("non-profit");
        } else {
          var sub = document.createTextNode("company");
        }

        var hireInfo = document.createElement("a");
        var info = document.createTextNode("More Info");
        if (i.profit != undefined) {
          hireInfo.href = "/organization/" + i.id;
        } else {
          hireInfo.href = "/veteran/" + i.username;
        }

        hireName.appendChild(name);
        hireName.className = "hire___name";
        hireSub.appendChild(sub);
        hireSub.className = "hire___sub";
        hireInfo.appendChild(info);
        hireInfo.className = "hire___link";

        hire.appendChild(hireImage);
        hire.appendChild(hireName);
        hire.appendChild(hireSub);
        hire.appendChild(hireInfo);

        var list = document.getElementsByClassName("hires")[0];
        hire.className = "hires___hire";
        list.appendChild(hire);
      }
    }
};
xhttp.open("GET", window.location.protocol + "//" + window.location.hostname + ":" + window.location.port + "/api/hires", true);
xhttp.send();

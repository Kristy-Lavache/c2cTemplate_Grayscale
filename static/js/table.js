function loadtable () {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("data").innerHTML=xhttp.responseText
        }
    };
    xhttp.open("GET", "/data", true);
    xhttp.send();
}
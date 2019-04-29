function loadtable () {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           var apiResponse = JSON.parse(xhttp.responseText);
            var soldiers = apiResponse;
            soldiers.forEach(function(soldier) {
                addSoldier(soldier);
            })
        }
    };
    xhttp.open("GET", "/data?name=" + document.getElementById("firstName").value + "&branch=" + document.getElementById("Branch").value + "&birth=" + document.getElementById("Birth").value + "&death=" + document.getElementById("Death").value, true);
    xhttp.send();


}

function addSoldier(soldier) {
    var output = document.getElementById("output");

    var newRow = document.createElement("tr");
    output.appendChild(newRow);

    var name = document.createElement("td");
    name.innerText = soldier.name;
    newRow.appendChild(name);

    var dob = document.createElement("td");
    dob.innerText = soldier.dob;
    newRow.appendChild(dob);

    var dod = document.createElement("td");
    dod.innerText = soldier.dod;
    newRow.appendChild(dod);

    var militaryBranch = document.createElement("td");
    militaryBranch.innerText = soldier.militaryBranch;
    newRow.appendChild(militaryBranch);

    var rank = document.createElement("td");
    rank.innerText = soldier.rank;
    newRow.appendChild(rank);

    // output.appendChild(newRow);
}
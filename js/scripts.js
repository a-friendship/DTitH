function showEur() {
  var x = document.getElementById("MedeaEur");
  var y = document.getElementById("MedeaApp");
  var z = document.getElementById("MedeaOvi");
  if (x.style.display === "none" || x.style.display === "") {
    x.style.display = "block";
    y.style.display = "none";
    z.style.display = "none";
  } else {
    x.style.display = "none";
  }
}

function showApR() {
  var x = document.getElementById("MedeaApp");
  var y = document.getElementById("MedeaEur");
  var z = document.getElementById("MedeaOvi");
  if (x.style.display === "none" || x.style.display === "") {
    x.style.display = "block";
    y.style.display = "none";
    z.style.display = "none";
  } else {
    x.style.display = "none";
  }
}

function showOvd() {
  var x = document.getElementById("MedeaOvi");
  var y = document.getElementById("MedeaEur");
  var z = document.getElementById("MedeaApp");
  if (x.style.display === "none" || x.style.display === "") {
    x.style.display = "block";
    y.style.display = "none";
    z.style.display = "none";
  } else {
    x.style.display = "none";
  }
}

function drawChart() {

    var data = google.visualization.arrayToDataTable([
      ['Chapter', 'Frequency'],
      ['Chapter 1', 2],
      ['Chapter 2', 1],
      ['Chapter 3', 1],
      ['Chapter 4', 5],
      ['Chapter 5', 1],
      ['Chapter 6', 5],
      ['Chapter 7', 1],
      ['Chapter 8', 5],
      ['Chapter 9', 13],
      ['Chapter 10', 7],
      ['Chapter 11', 23],
      ['Chapter 12', 15],
      ['Chapter 13', 7],
      ['Chapter 14', 5],
      ['Chapter 15', 4],
      ['Chapter 16', 3]
      ['Chapter 17', 10],
      ['Chapter 18', 20],
      ['Chapter 19', 11],
      ['Chapter 20', 11],
      ['Chapter 21', 11]
    ]);
    
    var options = {
      title: 'Lila'
    };
    
    var chart = new google.visualization.BarChart(document.getElementById('myChart'));
    chart.draw(data, options);
    
    }

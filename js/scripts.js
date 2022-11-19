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
      ['Chapter 1', 5],
      ['Chapter 2', 1],
      ['Chapter 3', 5],
      ['Chapter 4', 1],
      ['Chapter 5', 5],
      ['Chapter 6', 13],
      ['Chapter 7', 7],
      ['Chapter 8', 23],
      ['Chapter 9', 15],
      ['Chapter 10', 7],
      ['Chapter 11', 5],
      ['Chapter 12', 4],
      ['Chapter 13', 3]
      ['Chapter 14', 10],
      ['Chapter 15', 20],
      ['Chapter 16', 11],
      ['Chapter 17', 11],
      ['Chapter 18', 11]
    ]);
    
    var options = {
      title: 'Lila'
    };
    
    var chart = new google.visualization.BarChart(document.getElementById('myChart'));
    chart.draw(data, options);
    
    }

function drawChart() {

    var data = google.visualization.arrayToDataTable([
      ['Chapter', 'Frequency'],
      ['Chapter 1', 0],
      ['Chapter 2', 0],
      ['Chapter 3', 2],
      ['Chapter 4', 0],
      ['Chapter 5', 1],
      ['Chapter 6', 2],
      ['Chapter 7',2],
      ['Chapter 8', 4],
      ['Chapter 9', 3],
      ['Chapter 10', 1],
      ['Chapter 11', 1],
      ['Chapter 12', 1],
      ['Chapter 13', 2]
      ['Chapter 11', 2],
      ['Chapter 15', 7],
      ['Chapter 16', 2],
      ['Chapter 17', 2],
      ['Chapter 18', 3]]);
    
    var options = {
      title: 'Lenù'
    };
    
    var chart = new google.visualization.BarChart(document.getElementById('myChartLenù'));
    chart.draw(data, options);
    
    }

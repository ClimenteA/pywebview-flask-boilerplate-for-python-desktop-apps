function showPleasewait(the_id) {
  document.getElementById(the_id).innerHTML = "Please wait..";
  setTimeout(function () {
        document.getElementById(the_id).style.display='none';
    }, 5000); // 10000 sec
    return false;
}


function toggle(theID) {
  var x = document.getElementById(theID);
  var tohide = document.getElementById("tohide");
  x.className = "";
  if (x.style.display === "none") {
      x.style.display = "block";
      tohide.style.display = "none";
  } else {
      x.style.display = "none";
      tohide.style.display = "block";
  }
}



//Simple filtering table for the first column (not used)
function filterTable() {
  // Declare variables
  var input, filter, table, tr, td, i;
  input = document.getElementById("searchfor");
  filter = input.value;
  table = document.getElementById("table");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      if (td.innerHTML.indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}



//Filter multiple columns 
function filterColumnsTable(event) {
  var filter = event.target.value;
  var rows = document.querySelector("#table tbody").rows;
  
  for (var i = 0; i < rows.length; i++) {
      var col0 = rows[i].cells[0].textContent;
      var col1 = rows[i].cells[1].textContent;
      var col2 = rows[i].cells[2].textContent;
      var col3 = rows[i].cells[3].textContent;
      var col4 = rows[i].cells[4].textContent;
      var col5 = rows[i].cells[5].textContent;
      var col6 = rows[i].cells[6].textContent;
      var col7 = rows[i].cells[7].textContent;
      var col8 = rows[i].cells[8].textContent;
      var col9 = rows[i].cells[9].textContent;
      
      if (col0.indexOf(filter) > -1 || col1.indexOf(filter) > -1 || col2.indexOf(filter) > -1 || col3.indexOf(filter) > -1 || col4.indexOf(filter) > -1 || col5.indexOf(filter) > -1 || col6.indexOf(filter) > -1 || col7.indexOf(filter) > -1 || col8.indexOf(filter) > -1 || col9.indexOf(filter) > -1) {
          rows[i].style.display = "";
      } else {
          rows[i].style.display = "none";
      }      
  }
}

document.querySelector('#searchfor').addEventListener('keyup', filterColumnsTable, false);












// Bind to the onload event for the span
var counter = document.getElementById("scriptCloseCounter");
counter.onload = function() {closeTimer(counter)};

function closeTimer(counter) {
  counter.innerHTML = "10";
  setInterval(windowClose(counter), 1000);
}

function windowClose(counter) {
  var count = parseInt(counter.innerHTML);
  if (count === 0) {
    close();
  } else {
    counter.innerHTML = (count--).toString();
  }
}

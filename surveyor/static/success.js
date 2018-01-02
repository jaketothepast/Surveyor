// Bind to the onload event for the span
window.onload = function() {
  var counter = document.querySelector("#scriptCloseCounter");
  counter.innerHTML = "10";
  setInterval(windowClose, 1000, counter);
}

function windowClose(counter) {
  console.log("Inside windowClose");
  var count = parseInt(counter.innerHTML);
  if (count === 0) {
    close();
  } else {
    count--;
    counter.innerHTML = count.toString();
  }
}

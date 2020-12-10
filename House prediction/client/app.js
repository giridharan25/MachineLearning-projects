function getBathValue() {
  var uiBath = document.getElementsByName("uiBath");
  for(var i in uiBath) {
    if(uiBath[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}
function getRoomsValue() {
  var uirooms = document.getElementsByName("uirooms");
  for(var i in uirooms) {
    if(uirooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}
function getBedValue() {
  var uiBed = document.getElementsByName("uiBed");
  for(var i in uiBed) {
    if(uiBed[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var location = document.getElementById("uiLocations");
  var sqft = document.getElementById("uiSqft");
  var bed = getBHKValue();
  var bath = getBathValue();
  var rooms = getRoomsValue()
  var estPrice = document.getElementById("uiEstimatedPrice");
  var park = document.getElementById("uipark");
  var type = document.getElementById("uitype")
  var regfee = document.getElementById("uiregfee");
  var commis = document.getElementById("uicommis");
  var age = document.getElementById("uiage");

  var url = "http://127.0.0.1:5000/estimation"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      location: location.value
      sqft: parseFloat(sqft.value),
      bed: bed,
      bath: bath,
      rooms: rooms,
      park: park,
      type: type,
      regfee: parseFloat(regfee.value)
      commis: parseFloat(commis.value)
      age: parseFloat(age.value)
  },function(data, status) {
      console.log(data.estimation);
      estPrice.innerHTML = "<h2>" + data.estimation.toString() + " Lakh</h2>";
      console.log(status);
  });
}


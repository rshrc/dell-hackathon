$(document).ready(function() {
  // initialize slider
  $("#price-slider")
    .slider({
      min: 0,
      max: 1000,
      step: 10,
      value: [0, 1000]
    })
    .on("slide", function(obj) {
      $("#price-slider-min-value").text(` ${obj.value[0]}`);
      $("#price-slider-max-value").text(` ${obj.value[1]}`);
    });

  $("#price-slider-min-value").text(` ${$("#price-slider").slider('getValue')[0]}`);
  $("#price-slider-max-value").text(` ${$("#price-slider").slider('getValue')[1]}`);
});

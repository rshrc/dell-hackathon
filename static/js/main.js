$(document).ready(function() {
  // fix size of search bar
  $(window).ready(function() {
    $(".eac-square").css("width", "80%");
  });

  //search
  let options = {
    url: "/api/products",
    getValue: "name",
    list: {
      match: {
        enabled: true
      }
    },
    theme: "square",
    placeholder: "Search"
  };

  $("#search_input").easyAutocomplete(options);

  // initialize slider
  let productTitles = $(".products .card-title").toArray();
  productTitles = productTitles.map(product => product.innerText);
  let productPrices = $(".products .card-text").toArray();
  let productImages = $(".products .card-img-top").toArray().map(product=>product.src);
  let productUrls = $(".products a").toArray().map(product=>product.href);
  console.log(productImages);
  productPrices = productPrices.map(product => product.innerText);
  let products = productTitles.map((title, index) => {
    return {
      title: title,
      price: productPrices[index],
      image: productImages[index],
      url: productUrls[index]
    };
  });
  let maxPrice = productPrices.reduce((accumulator, currentValue)=>Math.max(accumulator, currentValue), 0);
  $("#price-slider")
    .slider({
      min: 0,
      max: parseInt(maxPrice),
      step: 10,
      value: [0, parseInt(maxPrice)]
    })
    .on("slide", function(obj) {
      $("#price-slider-min-value").text(` ${obj.value[0]}`);
      $("#price-slider-max-value").text(` ${obj.value[1]}`);
    });
  
  $("")
  $("#price-slider-min-value").text(
    ` ${$("#price-slider").slider("getValue")[0]}`
  );
  $("#price-slider-max-value").text(
    ` ${$("#price-slider").slider("getValue")[1]}`
  );

  $("#filter-btn").on("click", () => {
    let slider = $("#price-slider").slider("getValue")
    let minPrice = slider[0]
    let maxPrice = slider[1]
    let productsHtml = "";
    filteredProducts = products.filter(product => parseInt(product.price) >= minPrice && parseInt(product.price) <= maxPrice);
    console.log(products);
    filteredProducts.forEach(product => {
      productsHtml += 
      `
        <div class="products col-auto px-2 py-2">
        <div class="card" style="width: 16.8rem; height: 25rem;">
        <img src="${product.image}" class="card-img-top">
        <div class="card-body">
            <h3 class="card-title"><a href="${product.url}">${product.title}</a></h3>
            <p class="card-text"><i class="fa fa-inr"> <span class="h4">${product.price}</span></i></p>
        </div>
        </div>  
        </div>
      `;
    });
    $("#product-container").html(productsHtml);
  })
});

$(document).ready(function() {
  // initialize slider
  let productTitles = $(".products .card-title").toArray();
  productTitles = productTitles.map(product => product.innerText);
  let productPrices = $(".products .card-text").toArray();
  productPrices = productPrices.map(product => product.innerText);
  let products = productTitles.map((title, index)=>{
    return {
      title: title, 
      price: productPrices[index]
    }
  })
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
      let productsHtml = "";
      filteredProducts = products.filter(product => parseInt(product.price) >= obj.value[0] && parseInt(product.price) < obj.value[1]);
      console.log(products);
      filteredProducts.forEach(product => {
        productsHtml += `
        
        <div class="card" style="width: 16.8rem; height: 25rem;">
        <img src="{% if product.image %}{{ product.image.url }}{% else %}{% static "img/no_image_256x256.png" %}{% endif %}" class="card-img-top">
        <div class="card-body">
            <h3 class="card-title"><a href="{{ product.get_absolute_url_visit_1 }}">${product.title}</a></h3>
            <p class="card-text"><i class="fa fa-inr"> <span class="h4">${product.price }</span></i></p>
        </div>
    </div>  
        `
      })
      // console.log(productsHtml);
      $("#product-container").html(productsHtml)

      
    });

  $("#price-slider-min-value").text(` ${$("#price-slider").slider('getValue')[0]}`);
  $("#price-slider-max-value").text(` ${$("#price-slider").slider('getValue')[1]}`);
  
  console.log(productPrices);
  

  //search
  let options = {
    url: "/api/products",
    getValue: "name",
    list: {
      match: {
        enabled: true
      }
    },
    theme: "square"
  }
  $("#search_input").easyAutocomplete(options); 
  // let searchQuery = new Bloodhound({
  //   datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
  //   queryTokenizer: Bloodhound.tokenizers.whitespace,
  //   prefetch: '/api/products',
  //   remote :{
  //     url: '/api/products/%QUERY',
  //     wildcard: '%QUERY'
  //   }
  // });
  // $("#remote .typeahead").typeahead({}, {
  //   name: 'search-query',
  //   display: 'value',
  //   source: searchQuery
  // })
});

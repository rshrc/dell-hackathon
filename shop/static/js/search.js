let searchButton = document.getElementById("search_btn");
searchButton.onclick = async () => {
    console.log("clicked");
    let searchInput = document.getElementById("search_box").value;
    let query = 'http://localhost:8000/api/products/?search=' + searchInput;
    console.log(query);
    let response = await fetch(query);
    let jsonResponse = await response.json();
    console.log(jsonResponse);
    let imageElement = document.getElementById('contentImage');
    imageElement.setAttribute("src", jsonResponse[0]['image']);
};
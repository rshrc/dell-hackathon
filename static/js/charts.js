function drawConversionChart(data) {
    let labels = Object.keys(data);
    let yOutput = labels.map(label => data[label]);
    let ctx = document.getElementById("conversion-chart");

    let lineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels,
            datasets: [{
                label: 'Conversion rate',
                data: yOutput
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            responsive: false,
        }
    })
}

function drawRatingsDistribution(data) {
    let labels = Object.keys(data);
    let pieOutput = labels.map(label => data[label]);
    let ctx = document.getElementById("ratings-chart");
    let ratingsChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: pieOutput
            }]
        },
        options: {
            responsive: false,
        }
    }

    )

}

async function getRatingsData(productId){
    let response = await fetch(`/api/reviews/${productId}`);
    let reviews = await response.json();
    let ratings = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5:0};
    reviews.forEach(review=>{
        let stars = review.stars;
        
        ratings[stars]+=1;
    })
    return ratings
}
window.addEventListener('load', async () => {
    ratingsData = await getRatingsData(productId);
    drawConversionChart({
        'January': 50,
        'February': 60,
        'March': 80,
        'April': 20,
        'May': 100
    })

    drawRatingsDistribution(ratingsData);

    // drawRatingsDistribution({
    //     '5 star': 12,
    //     '4 star': 9,
    //     '3 star': 21,
    //     '2 star': 2,
    //     '1 star': 5
    // })
})

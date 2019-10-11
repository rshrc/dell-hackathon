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
window.addEventListener('load', () => {
    drawConversionChart({
        'January': 50,
        'February': 60,
        'March': 80,
        'April': 20,
        'May': 100
    })
})
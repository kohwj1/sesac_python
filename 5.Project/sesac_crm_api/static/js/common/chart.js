function drawChart(itemLabels, lineValues, barValues) {
    const ctx = document.getElementById('myChart')
    const data = {
        labels: itemLabels,
        datasets: [
            {
            type: 'line',
            label: '매출(원)',
            data: lineValues,
            //fill: false,
            //borderDash: [5, 5],
            borderColor: '#212121',
            backgroundColor: '#212121',
            borderWidth: 2,
            tension:0,
            yAxisID: 'yleft'
        },
            {
            type: 'bar',
            label: '판매량(개)',
            data: barValues,
            backgroundColor: '#0088ff55',
            yAxisID: 'yright'
        }]
        };

        const config = {
        type: 'scatter',
        data: data,
        options: {
            interaction: {intersect: true, mode: 'index'},
            aspectRatio:2.5,
            scales: {yleft: {position: 'left'}, yright: {position:'right', grid: {drawOnChartArea: false}}},
            plugins: {legend: {align: 'start'}}
        }
        };

    new Chart(ctx, config);
}
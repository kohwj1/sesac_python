function drawMixedChart(canvas, itemLabels, lineValues, barValues) {
    const ctx = document.getElementById(canvas)
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

function drawLineChart(canvas, itemLabels, lineValue_1, lineValue_2) {
    const ctx = document.getElementById(canvas)
    const data = {
        labels: itemLabels,
        datasets: [
            {
                type: 'line',
                label: '남성 주문(건)',
                data: lineValue_1,
                fill: true,
                //borderDash: [5, 5],
                borderColor: '#5179d4',
                backgroundColor: '#5178d47f',
                borderWidth: 2,
                tension:0.3,
                yAxisID: 'yleft'
            },
            {
                type: 'line',
                label: '여성 주문(건)',
                data: lineValue_2,
                fill: true,
                borderColor: '#d37d7d',
                backgroundColor: '#d37d7d72',
                borderWidth: 2,
                tension:0.3,
                yAxisID: 'yleft'
            }]
        };
        
        const config = {
            data: data,
            options: {
                interaction: {intersect: true, mode: 'index'},
                aspectRatio:2.5,
                scales: {yleft: {position: 'left'}},
                plugins: {legend: {align: 'start'}}
            }
        };

    new Chart(ctx, config);
}

function drawBubbleChart(canvas, dataLabel_1, dataset_1, dataLabel_2, dataset_2) {
    const ctx = document.getElementById(canvas)
    const data = {
        datasets: [{
                label: dataLabel_1,
                data: dataset_1,
                borderColor: 'rgba(83, 113, 141, 1)',
                backgroundColor: 'rgb(147, 202, 253)'
            },
            {
                label: dataLabel_2,
                data: dataset_2,
                borderColor: '#e74242ff',
                backgroundColor: 'rgb(255, 99, 132)'
            }]
        };

        const config = {
        type: 'bubble',
        data: data,
        options: {
            // interaction: {intersect: true, mode: 'index'},
            aspectRatio:2.5,
            plugins: {legend: {align: 'start'}}
        }
        };

    new Chart(ctx, config);
}
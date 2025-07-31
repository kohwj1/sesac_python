function getChartData() {
    const dataArray = document.getElementsByClassName('chartdata')
    let itemLabels = []
    let lineValues = []
    let barValues = []
    for (i = 0; i + 2 < dataArray.length; i += 3) {
        itemLabels.push(dataArray[i].textContent);
        lineValues.push(dataArray[i+1].textContent);
        barValues.push(dataArray[i+2].textContent);
    }
    
    itemLabels.reverse();
    lineValues.reverse();
    barValues.reverse();
    
    return {'itemLabels':itemLabels, 'lineValues':lineValues, 'barValues':barValues}
}

function drawChart() {
    const ctx = document.getElementById('myChart')
    const raw_data = getChartData()  //API 방식으로 교체할 거면 여기 나중에 수정하기
    // console.log(raw_data)

    const data = {
        labels: raw_data.itemLabels,
        datasets: [
            {
            type: 'line',
            label: '매출(원)',
            data: raw_data.lineValues,
            //fill: false,
            //borderDash: [5, 5],
            borderColor: '#136262',
            backgroundColor: '#136262',
            borderWidth: 2,
            tension:0,
            yAxisID: 'yleft'
        },
            {
            type: 'bar',
            label: '판매량(개)',
            data: raw_data.barValues,
            backgroundColor: '#6c848452',
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

document.addEventListener('DOMContentLoaded', drawChart)
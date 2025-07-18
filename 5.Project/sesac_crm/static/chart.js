function getChartData() {
    const dataArray = document.getElementsByClassName('chartdata')
    let itemLabels = []
    let barValues = []
    let lineValues = []
    for (i = 0; i < dataArray.length; i += 3) {
        itemLabels.push(dataArray[i].innerText);
        barValues.push(dataArray[i+1].innerText);
        lineValues.push(dataArray[i+2].innerText);
    }
    
    itemLabels.reverse();
    barValues.reverse();
    lineValues.reverse();
    
    return {'itemLabels':itemLabels, 'barValues':barValues, 'lineValues':lineValues}
}

function drawChart() {
    const ctx = document.getElementById('myChart')
    const raw_data = getChartData()  //API 방식으로 교체할 거면 여기 나중에 수정하기
    // console.log(raw_data)

    const data = {
        labels: raw_data.itemLabels,
        datasets: [{
            type: 'bar',
            label: '매출(원)',
            data: raw_data.barValues,
            backgroundColor: '#6c848452',
            yAxisID: 'yleft'
        }, {
            type: 'line',
            label: '판매량(개)',
            data: raw_data.lineValues,
            fill: false,
            borderColor: '#6c8484',
            borderWidth: 1,
            fill: false,
            tension:0.1,
            yAxisID: 'yright'
        }]
        };

        const config = {
        type: 'scatter',
        data: data,
        options: {
            aspectRatio:2.5,
            scales: {
                yleft: {position: 'left'},
                yright: {position:'right'}
            }
        }
        };

    new Chart(ctx, config);
}

document.addEventListener('DOMContentLoaded', drawChart)
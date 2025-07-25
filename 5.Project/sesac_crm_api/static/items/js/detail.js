const args = new URLSearchParams(window.location.search)
const itemId = args.get('id')
let itemLabels = []
let lineValues = []
let barValues = []

function displaySummary() {
    fetch(`/items/api/summary/${itemId}`)
        .then((response) => response.json())
        .then((data) => {
            document.title += data.Name;
            const itemId = document.getElementById('itemId')
            itemId.textContent = data.ItemId

            const itemSummary = document.getElementById('summary');
            itemSummary.innerHTML = `<tr>
                                        <td>${data.Name}</a></td>
                                        <td>${data.Type}</td>
                                        <td>${data.UnitPrice}원</a></td>
                                    </tr>`;
    })
    };

function displaySales() {    
    fetch(`/items/api/sales_monthly/${itemId}`)
        .then((response) => response.json())
        .then((data) => {
            table_data = data.data;
            const monthlySales = document.getElementById('monthlySales')
            // console.log(table_data)
            if (table_data.length == 0) {
                monthlySales.innerHTML = '<tr><td colspan="3" class="noResult">표시할 데이터가 없습니다</td></tr>'
            } else {
                monthlySales.innerHTML = ''
                for (row of table_data) {
                    monthlySales.innerHTML += `                    
                            <tr>
                                <td>${row.Month}</td>
                                <td>${row.Sales}</td>
                                <td>${row.SalesCount}</td>
                            </tr>`;
                    itemLabels.push(row.Month);
                    lineValues.push(row.Sales);
                    barValues.push(row.SalesCount);
                }
            };
        })
        .then(() => {
            // console.log('역순으로 담긴 리스트 순서 리버스');
            itemLabels.reverse();
            lineValues.reverse();
            barValues.reverse();
            // console.log(itemLabels, lineValues, barValues)
        })
        .then(() => {
            // console.log('이제차트그릴타이밍');
            if (table_data.length != 0) {
                drawMixedChart('myChart', itemLabels, lineValues, barValues);
        }   else {
                console.log('차트 그릴 데이터가 없어요!!');
        }
    })
    };

document.addEventListener('DOMContentLoaded', displaySummary)
document.addEventListener('DOMContentLoaded', displaySales)
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
            itemLabels.reverse();
            lineValues.reverse();
            barValues.reverse();
        })
        .then(() => {
            if (table_data.length != 0) {
                drawMixedChart('myChart', itemLabels, lineValues, barValues);
        }   else {
                console.log('차트 데이터가 존재하지 않습니다.');
        }
    })
    };

document.addEventListener('DOMContentLoaded', () => {
    displaySummary()
    displaySales()
})
// document.addEventListener('DOMContentLoaded', displaySales)
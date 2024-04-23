document.addEventListener('DOMContentLoaded', function () {
    var options = {
        chart: {
            type: 'line',
            height: 400
        },
        series: [{
            name: 'Insonlar Kirishi',
            data: [30, 90, 10, 100, 150, ] // Ma'lumotlar o'zgartirilishi mumkin
        }],
        xaxis: {
            categories: ['Dekabr','Yanvar', 'Fevral', 'Mart', 'Aprel', ]
        }
    };

    var chart = new ApexCharts(document.querySelector("#chartContainer"), options);

    chart.render();
});

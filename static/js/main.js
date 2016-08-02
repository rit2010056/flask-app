var autocall = $(document).ready(function() {
console.log(chart_id)
// console.log('hjhjhjh',chartData)
chartData1= generatechartData(chartData)
function generatechartData(chartData) {
console.log("krishna",chartData)
chartData_in = []
  for (var i = 0; i < chartData.length; i++) {
    // we create date objects here. In your data, you can have date strings
    // and then set format of your dates using chart.dataDateFormat property,
    // however when possible, use date objects, as this will speed up chart rendering.
    var newDate = new Date(chartData[i]['date']);
// console.log(newDate)
    // newDate.setDate(newDate.getDate() + i);

    //var price = Math.round(Math.random() * 90 - 45);

    chartData_in.push({
      date: newDate,
      price_go: chartData[i]['price_go'],
      price_x: chartData[i]['price_x']
    });
  }
  return chartData_in;
}
console.log('hjhjhjh',chartData1)

var chart = AmCharts.makeChart(chart_id, {
  "theme": "light",
  "type": "serial",
  "legend": {
        "useGraphSettings": true
    },
  "synchronizeGrid":true,
  "dataProvider": chartData1,
  "valueAxes":[{
        "id":"v1",
        "axisColor": "#FF6600",
        "axisThickness": 4,
        "axisAlpha": 5,
        "position": "left"
    }],
  "graphs": [{
        "valueAxis": "v1",
        "lineColor": "#FF6600",
        "bullet": "round",
        "bulletBorderThickness": 1,
        "hideBulletsCount": 30,
        "title": "Uber GO",
        "valueField": "price_go",
    "fillAlphas": 0
    },
    {
        "valueAxis": "v2",
        "lineColor": "#FCD202",
        "bullet": "square",
        "bulletBorderThickness": 1,
        "hideBulletsCount": 30,
        "title": "Uber X ",
        "valueField": "price_x",
    "fillAlphas": 0
    }
    ],
  "chartScrollbar": {

  },
  "chartCursor": {
        "cursorPosition": "mouse"
    },
  "categoryField": "date",
  "categoryAxis": {
        "parseDates": true,
        "axisColor": "#DADADA",
        "minorGridEnabled": true
    },
    "export": {
      "enabled": true,
        "position": "bottom-right"
     }
});

chart.addListener("dataUpdated", zoomChart);
zoomChart();

function zoomChart(){
    chart.zoomToIndexes(chart.dataProvider.length - 20, chart.dataProvider.length - 1);
}


});
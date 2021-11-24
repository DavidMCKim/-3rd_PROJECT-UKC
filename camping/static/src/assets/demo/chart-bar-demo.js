// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example

var ctx = document.getElementById("main_line");
var main_line_lbl = $('#main_line_lbl').val(); //서버에서 전송된 차트 label 값
var main_line_val = $('#main_line_val').val(); //서버에서 전송된 차트 data 값

// 서버에서 리스트로 전송됨 장고는 리스트 처리가 어려움 text 형태로 들어옴
// 텍스트를 숫자로 변경
var main_lbl = main_line_lbl.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '').replaceAll("'", '')
var main_val = main_line_val.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '')

var main_lbl_final = main_lbl.split(' ')
var main_val_final = main_val.split(' ')

//chart.js 형식 코드
var myLineChart = new Chart(ctx, {
  type: 'line', // 차트 종류
  data: {
    labels: main_lbl_final, //x축 값
    datasets: [{
      label: "종가",
      lineTension: 0.3,
      backgroundColor: "rgba(218,241,223,0.4)",
      borderColor: "rgba(95,196,118,1)",
      pointRadius: 6,
      pointBackgroundColor: "rgba(255,255,255,1)",
      pointBorderColor: "rgba(95,196,118,1)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(90,194,114,0.9)",
      pointHitRadius: 50,
      pointBorderWidth: 3,
      data: main_val_final,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: true
        },
        ticks: {
          maxTicksLimit: 31
        }
      }],
      yAxes: [{
        ticks: {
          min: 50000, //y축값
          max: 60000,
          maxTicksLimit: 100
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});

// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

var ctx = document.getElementById("main_line2");
var main_line2_lbl = $('#main_line2_lbl').val();
var main_line2_val = $('#main_line2_val').val();

var main_lbl2 = main_line2_lbl.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '').replaceAll("'", '')
var main_val2 = main_line2_val.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '')

var main_lbl2_final = main_lbl2.split(' ')
var main_val2_final = main_val2.split(' ')

var myLine2Chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: main_lbl2_final,
    datasets: [{
      label: "종가",
      lineTension: 0.3,
      backgroundColor: "rgba(218,241,223,0.4)",
      borderColor: "rgba(95,196,118,1)",
      pointRadius: 6,
      pointBackgroundColor: "rgba(255,255,255,1)",
      pointBorderColor: "rgba(95,196,118,1)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(90,194,114,0.9)",
      pointHitRadius: 50,
      pointBorderWidth: 3,
      data: main_val2_final,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: true
        },
        ticks: {
          maxTicksLimit: 31
        }
      }],
      yAxes: [{
        ticks: {
          min: 190,
          max: 210,
          maxTicksLimit: 10
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
// Pie Chart Example
//var ctx = document.getElementById("main_line2");
//
//var main_pie_lbl = $('#main_pie_lbl').val();
//var main_pie_val = $('#main_pie_val').val();
//
//var pie_lbl = main_pie_lbl.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '').replaceAll("'", '')
//var pie_val = main_pie_val.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '').replaceAll('.  ', '.00 ').replaceAll('   ', ' ').replaceAll('  ', ' ')
//
//var pie_lbl_final = pie_lbl.split(' ')
//var pie_val_final = pie_val.split(' ')
//
//var myPieChart = new Chart(ctx, {
//  type: 'pie',
//  data: {
//    labels: pie_lbl_final,
//    datasets: [{
//      data: pie_val_final,
//      backgroundColor: ['#037F8C', '#205459', '#F2E7C4', '#F28F38', '#F25757', '#03738C', '#04BFAD', '#D9CE36',
//      '#F2E8B6','#F26B6B' ,'#153259'],
//    }],
//  },
//});



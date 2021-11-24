// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// 경기도 일자별 평균 line 그래프

var ctx = document.getElementById("gg_daily_chart");

var gg_daily_lbl = $('#gg_daily_lbl').val();
var gg_daily_val = $('#gg_daily_val').val();

var gg_lbl = gg_daily_lbl.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '').replaceAll("'", '');
var gg_val = gg_daily_val.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '');

var gg_lbl_final = gg_lbl.split(' ');
var gg_val_final = gg_val.split(' ');

var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: gg_lbl_final,
    datasets: [{
      label: "일자별종가",
      lineTension: 0.3,
      backgroundColor: "rgba(236,245,254,0.4)",
      borderColor: "rgba(73,166,255,1)",
      pointRadius: 6,
      pointBackgroundColor: "rgba(255,255,255,1)",
      pointBorderColor: "rgba(73,166,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,117,216,0.9)",
      pointHitRadius: 50,
      pointBorderWidth: 3,
      data: gg_val_final,
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
          min: 0,
          max: 100000,
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

// 경기도 시간대별 bar 그래프

var ctx_hour = document.getElementById("gg_hour_chart");

var gg_hour_lbl = $('#gg_hour_lbl').val();
var gg_hour_val = $('#gg_hour_val').val();

var gg_lbl = gg_hour_lbl.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '').replaceAll("'", '');
var gg_val = gg_hour_val.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '');

var gg_lbl_final = gg_lbl.split(' ');
var gg_val_final = gg_val.split(' ');


var myLineChart = new Chart(ctx_hour, {
  type: 'bar',
  data: {
    labels: gg_lbl_final,
    datasets: [{
      label: "시간대별 주문예측건수",
      lineTension: 0.3,
      backgroundColor: "rgba(73,167,255,1)",
      borderColor: "rgba(2,117,216,1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(2,117,216,1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,117,216,1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: gg_val_final,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 31
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 2000,
          maxTicksLimit: 20
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



// 서울 일자별 line 그래프

var ctx = document.getElementById("sl_daily_chart");

var sl_daily_lbl = $('#sl_daily_lbl').val();
var sl_daily_val = $('#sl_daily_val').val();

var sl_lbl = sl_daily_lbl.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '').replaceAll("'", '');
var sl_val = sl_daily_val.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '');

var sl_lbl_final = sl_lbl.split(' ');
var sl_val_final = sl_val.split(' ');


var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: sl_lbl_final,
    datasets: [{
      label: "일자별 평균 주문예측건수",
      lineTension: 0.3,
      backgroundColor: "rgba(254,218,224,0.2)",
      borderColor: "rgba(241,107,121,0.8)",
      pointRadius: 6,
      pointBackgroundColor: "rgba(255,255,255,1)",
      pointBorderColor: "rgba(241,107,121,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(251,70,102,0.8)",
      pointHitRadius: 50,
      pointBorderWidth: 3,
      data: sl_val_final,
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
          min: 0,
          max: 150,
          maxTicksLimit: 15
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

// 서울 시간대별 bar 그래프

var ctx_hour = document.getElementById("sl_hour_chart");

var sl_hour_lbl = $('#sl_hour_lbl').val();
var sl_hour_val = $('#sl_hour_val').val();

var sl_lbl = sl_hour_lbl.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '').replaceAll("'", '');
var sl_val = sl_hour_val.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '');

var sl_lbl_final = sl_lbl.split(' ');
var sl_val_final = sl_val.split(' ');


var myLineChart = new Chart(ctx_hour, {
  type: 'bar',
  data: {
    labels: sl_lbl_final,
    datasets: [{
      label: "시간대별 주문예측건수",
      lineTension: 0.3,
      backgroundColor: "rgba(255,128,128,0.9)",
      borderColor: "rgba(2,117,216,1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(2,117,216,1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,117,216,1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: sl_val_final,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 31
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 300,
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

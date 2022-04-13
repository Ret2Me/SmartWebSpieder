type = ['primary', 'info', 'success', 'warning', 'danger'];

demo = {
  initPickColor: function() {
    $('.pick-class-label').click(function() {
      var new_class = $(this).attr('new-class');
      var old_class = $('#display-buttons').attr('data-class');
      var display_div = $('#display-buttons');
      if (display_div.length) {
        var display_buttons = display_div.find('.btn');
        display_buttons.removeClass(old_class);
        display_buttons.addClass(new_class);
        display_div.attr('data-class', new_class);
      }
    });
  },

  initDocChart: function() {
    chartColor = "#FFFFFF";

    // General configuration for the charts with Line gradientStroke
    gradientChartOptionsConfiguration = {
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        }
      },
      tooltips: {
        bodySpacing: 4,
        mode: "nearest",
        intersect: 0,
        position: "nearest",
        xPadding: 10,
        yPadding: 10,
        caretPadding: 10
      },
      responsive: true,
      scales: {
        yAxes: {
          display: 0,
          gridLines: 0,
          ticks: {
            display: false
          },
          gridLines: {
            zeroLineColor: "transparent",
            drawTicks: false,
            display: false,
            drawBorder: false
          }
        },
        xAxes: {
          display: 0,
          gridLines: 0,
          ticks: {
            display: false
          },
          gridLines: {
            zeroLineColor: "transparent",
            drawTicks: false,
            display: false,
            drawBorder: false
          }
        }
      },
      layout: {
        padding: {
          left: 0,
          right: 0,
          top: 15,
          bottom: 15
        }
      }
    };
  },

  initDashboardPageCharts: function() {

    gradientChartOptionsConfigurationWithTooltipBlue = {
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        }
      },
      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: {
          beginAtZero: true,
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#2380f7"
          }
        },

        xAxes: {
          beginAtZero: true,
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#2380f7"
          }
        }
      }
    };

    gradientChartOptionsConfigurationWithTooltipPurple = {
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        }
      },
      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: {
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            beginAtZero: true,
            suggestedMax: 100,
            padding: 20,
            fontColor: "#9a9a9a"
          }
        },

        xAxes: {
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(225,78,202,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }
      }
    };

    gradientChartOptionsConfigurationWithTooltipOrange = {
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        }
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: {
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 50,
            suggestedMax: 110,
            padding: 20,
            fontColor: "#ff8a76"
          }
        },

        xAxes: {
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(220,53,69,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#ff8a76"
          }
        }
      }
    };

    gradientChartOptionsConfigurationWithTooltipGreen = {
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        }
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: {
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 50,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#9e9e9e"
          }
        },

        xAxes: {
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(0,242,195,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }
      }
    };


    gradientBarChartConfiguration = {
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        }
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: {
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 120,
            padding: 20,
            fontColor: "#9e9e9e"
          }
        },

        xAxes: {
          beginAtZero: true,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }
      }
    };


    var ctfx = document.getElementById("chartLinePurple").getContext("2d");
    var gradientStroke = ctfx.createLinearGradient(0, 230, 0, 50);
    gradientStroke.addColorStop(1, 'rgba(72,72,176,0.2)');
    gradientStroke.addColorStop(0.2, 'rgba(72,72,176,0.0)');
    gradientStroke.addColorStop(0, 'rgba(119,52,169,0)'); //purple colors

    var date = new Date();
    var time_labels = []
    var hour = 0


    async function fetch_records_new(){
        var new_data = []
        let new_labels = []
        for (let i=5; i >= 0; i--) {
          var hour = date.getHours()
          hour = (hour - i < 0)? 24 + hour - i: hour - i;
          new_labels.push(hour)
          date_str = date.getDate() + '-' + (date.getMonth() + 1) + '-' + date.getFullYear() + '_' + hour + ':' + date.getMinutes() + ':' + date.getSeconds()
          await fetch('api/get_servers?lowest_severity_level=0&highest_severity_level=3&ending_time_period=' + date_str + '&count=true',)
              .then(res => {
                if (!res.ok) {
                  console.log('get_servers endpoint failed');
                }
                return res.text();
              })
              .then(res => {
                new_data.push(parseInt(res));
                time_labels.push(date.getHours() - i);
              })
        }
        return {chart_data: new_data, chart_label: new_labels}
      }

    var new_data = fetch_records_new().then(new_data => {
      var data = {
        labels: new_data.chart_label,
        datasets: [{
          label: "Hits",
          fill: true,
          backgroundColor: gradientStroke,
          borderColor: '#00f2c3',
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          pointBackgroundColor: '#00f2c3',
          pointBorderColor: 'rgba(255,255,255,0)',
          pointHoverBackgroundColor: '#00f2c3',
          pointBorderWidth: 20,
          pointHoverRadius: 4,
          pointHoverBorderWidth: 15,
          pointRadius: 4,
          data: new_data.chart_data
        }]
      };

      var myChart = new Chart(ctfx, {
        type: 'line',
        data: data,
        options: gradientChartOptionsConfigurationWithTooltipPurple
      });
    })


    let ctxGreen = document.getElementById("chartLineGreen").getContext("2d");
    var gradientStroke = ctxGreen.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(66,134,121,0.15)');
    gradientStroke.addColorStop(0.4, 'rgba(66,134,121,0.0)'); //green colors
    gradientStroke.addColorStop(0, 'rgba(66,134,121,0)'); //green colors


    time_labels = []
    async function fetch_records(){
        let new_data = []
        let new_labels = []
        for (let i=5; i >= 0; i--) {
          let hour = date.getHours()
          hour = (hour - i < 0)? 24 + hour - i: hour - i;
          new_labels.push(hour)
          date_str = date.getDate() + '-' + (date.getMonth() + 1) + '-' + date.getFullYear() + '_' + hour + ':' + date.getMinutes() + ':' + date.getSeconds()
          console.log(hour)
          console.log(date_str)
          await fetch('api/get_servers?lowest_severity_level=7&highest_severity_level=10&ending_time_period=' + date_str + '&count=true',)
              .then(res => {
                if (!res.ok) {
                  console.log('get_servers endpoint failed');
                }
                return res.text();
              })
              .then(res => {
                new_data.push(parseInt(res));
                time_labels.push(date.getHours() - i);
              })
        }
        return {chart_data: new_data, chart_label: new_labels}
      }

    let test = fetch_records().then((chart_info) => {
      let data = {
        labels: chart_info.chart_label,
        datasets: [{
          label: "Hits",
          fill: true,
          backgroundColor: gradientStroke,
          borderColor: '#d048b6',
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          pointBackgroundColor: '#d048b6',
          pointBorderColor: 'rgba(255,255,255,0)',
          pointHoverBackgroundColor: '#d048b6',
          pointBorderWidth: 20,
          pointHoverRadius: 4,
          pointHoverBorderWidth: 15,
          pointRadius: 4,
          data: chart_info.chart_data,
        }]
      };
      var myChart = new Chart(ctxGreen, {
        type: 'line',
        data: data,
        options: gradientChartOptionsConfigurationWithTooltipGreen
      });
    })





    var ctx = document.getElementById("chartBig1").getContext('2d');

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(72,72,176,0.1)');
    gradientStroke.addColorStop(0.4, 'rgba(72,72,176,0.0)');
    gradientStroke.addColorStop(0, 'rgba(119,52,169,0)'); //purple colors


    var date = new Date();
    var time_labels = []

    var chart_labels = [];
    var chart_data = [];
    var statistics = [];
    var disk_data = [];
    var cpu_data = []
    var data = []
    fetch('api/hardware_monitor')
      .then(res => {
        if (!res.ok) {
          console.log('hardware_monitor endpoint failed');
        }
        return res.json();
      })
      .then(json => {
        statistics = json['STATISTICS'];
        let date_arr = "";
        statistics.forEach((item, index) => {
          chart_labels[index] = item['DATE'].split(',')[3];
          chart_data[index] = item['RAM'];
          disk_data[index] = item['DISK'];
          cpu_data[index] = item['CPU'];
        })
        data = myChartData.config.data;
        data.datasets[0].data = chart_data;
        data.labels = chart_labels;
        myChartData.update();
      })

    var config = {
      type: 'line',
      data: {
        labels: chart_labels,
        datasets: [{
          label: "RAM usage",
          fill: true,
          backgroundColor: gradientStroke,
          borderColor: '#d346b1',
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          pointBackgroundColor: '#d346b1',
          pointBorderColor: 'rgba(255,255,255,0)',
          pointHoverBackgroundColor: '#d346b1',
          pointBorderWidth: 20,
          pointHoverRadius: 4,
          pointHoverBorderWidth: 15,
          pointRadius: 4,
          data: chart_data,
        }]
      },
      options: gradientChartOptionsConfigurationWithTooltipPurple
    };
    var myChartData = new Chart(ctx, config);

    $("#0").click(function() {
      data = myChartData.config.data;
      data.datasets[0].data = chart_data;
      data.labels = chart_labels;
      myChartData.update();
    });

    $("#1").click(function() {
      var chart_data = cpu_data;
      var data = myChartData.config.data;
      myChartData.config.data.datasets[0].label = 'CPU usage'
      data.datasets[0].data = chart_data;
      data.labels = chart_labels;
      myChartData.update();
    });


    $("#2").click(function() {
      var chart_data = disk_data;
      var data = myChartData.config.data;
      myChartData.config.data.datasets[0].label = 'DISK usage'
      data.datasets[0].data = chart_data;
      data.labels = chart_labels;
      myChartData.update();
    });


    var ctx = document.getElementById("CountryChart").getContext("2d");

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(29,140,248,0.2)');
    gradientStroke.addColorStop(0.4, 'rgba(29,140,248,0.0)');
    gradientStroke.addColorStop(0, 'rgba(29,140,248,0)'); //blue colors

    var myNewChart = new Chart(ctx, {
      type: 'line',
      responsive: true,
      plugins: {
        legend: {
          display: false
        }
      },
      data: {
        labels: [],
        datasets: [{
          label: "Hits",
          fill: true,
          backgroundColor: gradientStroke,
          hoverBackgroundColor: gradientStroke,
          borderColor: '#1f8ef1',
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          data: []
        }]
      },
      options: gradientBarChartConfiguration
    });

    date = new Date();
    for (let i=5; i >= 0; i--){
      hour = date.getHours() - i
      hour = (hour - i < 0)? 24 + hour - 1: hour - i;
      var date_str = date.getDate() + '-' + (date.getMonth() + 1) + '-' + date.getFullYear() + '_' + hour + ':' + date.getMinutes() + ':' + date.getSeconds()
      fetch('api/get_servers?lowest_severity_level=4&highest_severity_level=6&ending_time_period=' + date_str + '&count=true',)
          .then(res => {
            if (!res.ok) {
              console.log('get_servers endpoint failed');
            }
            return res.text();
          })
          .then(res => {
            data = myNewChart.config.data;
            data.datasets[0].data.push(res);
            data.labels.push(date.getHours() - i);
            myNewChart.update();
          })
    }
  }
};

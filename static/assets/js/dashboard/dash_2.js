try {


  /*
      ==============================
      |    @Options Charts Script   |
      ==============================
  */

  /*

    Dropdown

  */

  var filterDropdown = function() {
    var getDropdownElement = document.querySelectorAll('.filter.custom-dropdown-icon .dropdown-item');
    for (var i = 0; i < getDropdownElement.length; i++) {
        getDropdownElement[i].addEventListener('click', function() {
          console.log(this.getAttribute('data-value'))
            document.querySelectorAll('.custom-dropdown-icon .dropdown-toggle > span.text')[0].innerHTML = this.getAttribute('data-value');
        })
    }
  }

  /*
      ======================================
          Visitor Statistics | Options
      ======================================
  */


  // Total Visits

  var spark1 = {
      chart: {
          id: 'unique-visits',
          group: 'sparks2',
          type: 'line',
          height: 58,
          sparkline: {
              enabled: true
          },
      },
      series: [{
          data: [21, 9, 36, 12, 44, 25, 59, 41, 66, 25]
      }],
      stroke: {
        curve: 'smooth',
        width: 2,
      },
      markers: {
          size: 0
      },
      grid: {
        padding: {
          top: 0,
          bottom: 0,
          left: 0
        }
      },
      colors: ['#2196f3'],
      tooltip: {
          x: {
              show: false
          },
          y: {
              title: {
                  formatter: function formatter(val) {
                      return '';
                  }
              }
          }
      },
      responsive: [
      {
          breakpoint: 576,
          options: {
             chart: {
                height: 95,
            },
            grid: {
                padding: {
                  top: 45,
                  bottom: 0,
                  left: 0
                }
            },
          },
      }

      ]
  }

  // Paid Visits

  var spark2 = {
      chart: {
        id: 'total-users',
        group: 'sparks1',
        type: 'line',
        height: 58,
        sparkline: {
          enabled: true
        },
      },
      series: [{
        data: [22, 19, 30, 47, 32, 44, 34, 55, 41, 69]
      }],
      stroke: {
        curve: 'smooth',
        width: 2,
      },
      markers: {
        size: 0
      },
      grid: {
        padding: {
          top: 0,
          bottom: 0,
          left: 0
        }
      },
      colors: ['#e2a03f'],
      tooltip: {
        x: {
          show: false
        },
        y: {
          title: {
            formatter: function formatter(val) {
              return '';
            }
          }
        }
      },
      responsive: [
      {
          breakpoint: 576,
          options: {
             chart: {
                height: 95,
            },
            grid: {
                padding: {
                  top: 35,
                  bottom: 0,
                  left: 0
                }
            },
          },
      }
      ]
  }


  /*
      ===================================
          Unique Visitors | Options
      ===================================
  */

 var d_1options1 = {
    chart: {
      height: 350,
      type: 'line',
      toolbar: {
        show: false,
      }
    },
    plotOptions: {
      bar: {
          horizontal: false,
          columnWidth: '55%',
      },
    },
    legend: {
      offsetX: 0,
      offsetY: -10,
    },
    colors: ['#61b6cd', '#805dca'],

    series: [{
      name: 'Organic',
      type: 'column',
      data: [4400, 5050, 4140, 6710, 2270, 4130, 2010, 3520, 7520, 3200, 2570, 1600]
    }, {
      name: 'Direct',
      type: 'line',
      data: [230, 420, 350, 270, 430, 220, 170, 310, 220, 220, 120, 160]
    }],
    stroke: {
      show: true,
      curve: 'smooth',
      width: [0, 4],
      lineCap: 'square'
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    yaxis: [{
      title: {
        text: 'Organic',
      },

    }, {
      opposite: true,
      title: {
        text: 'Direct'
      }
    }],

    responsive: [{
      breakpoint: 576,
      options: {
        yaxis: [{
          title: {
            text: undefined,
          },

        }, {
          opposite: true,
          title: {
            text: undefined
          }
        }],
      },
    }]

  }

  /*
      ==============================
          Statistics | Options
      ==============================
  */

  // Followers


  /*
      ==============================
      |    @Render Charts Script    |
      ==============================
  */


  /*
      ======================================
          Visitor Statistics | Script
      ======================================
  */

  // Total Visits
  // d_1C_1 = new ApexCharts(document.querySelector("#total-users"), spark1);
  // d_1C_1.render();

  // Paid Visits
  // d_1C_2 = new ApexCharts(document.querySelector("#paid-visits"), spark2);
  // d_1C_2.render();

  /*
      ===================================
          Unique Visitors | Script
      ===================================
  */

  // var d_1C_3 = new ApexCharts(
  //     document.querySelector("#uniqueVisits"),
  //     d_1options1
  // );
  // d_1C_3.render();

  /*
      ==============================
          Statistics | Script
      ==============================
  */

/*
    =============================================
        Perfect Scrollbar | Notifications
    =============================================
*/
// const ps = new PerfectScrollbar(document.querySelector('.mt-container'));
// filterDropdown();

} catch(e) {
// statements
console.log(e);
}

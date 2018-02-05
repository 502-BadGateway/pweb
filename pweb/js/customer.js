//确定按钮事件：调用drawBar()函数画出重点客户和活跃客户TOP10的直方图
function submit(){
	var startTime=$("#startTime").val()
	var endTime=$("#endTime").val()
	$.ajax({
		type: "GET",  
        url: "http://localhost:8080/customers?startTime="+startTime+"&endTime="+endTime,
        contentType: "application/json",
        success: function (data) {
			console.log(data["cus1"],data["con1"],data["cus2"],data["con2"])
        	drawBar(data["cus1"],data["con1"],data["cus2"],data["con2"])
    	}
    })
}

//传入重点客户cus1和活跃客户cus2的TOP10列表，以及每个客户对应的满意度con1,con2
function drawBar(cus1,con1,cus2,con2){
        // 路径配置
        require.config({
            paths: {
                echarts: 'http://echarts.baidu.com/build/dist'
            }
        });
        
        // 使用
        require(
            [
                'echarts',
                'echarts/chart/bar' // 使用柱状图就加载bar模块，按需加载
            ],
            function (ec) {
                // 基于准备好的dom，初始化echarts图表
                var myChart = ec.init(document.getElementById('customergraph')); 
                
                var option = {
					
                    tooltip: {
                        trigger: 'axis',
						axisPointer : {            // 坐标轴指示器，坐标轴触发有效
							type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
						}
                    },
                    legend: {
                        data:[ '重点客户', '活跃客户']
                    },
					grid:{
						left: '3%',
						right: '4%',
						bottom: '3%',
						containLabel: true
					},
                    xAxis : [
                        {
                            type : 'value'
                        }
                    ],
                    yAxis : [
                        {
                            type : 'category',
							axisTick : {show: false},
							data :  cus1
                        },
						{
							
							
                            type : 'category',
							axisTick : {show: false},
							data:cus2
                        }
                    ],
                    series : [
                        {
                            name:"重点客户",
                            type:"bar",
                            stack: '总量',
							label: {
								normal: {
									show: true
								}
							},
							data: con1
                        },
						{
                            name:"活跃客户",
                            type:"bar",
                            stack: '总量',
							label: {
								normal: {
									show: true
									//position:'left'
								}
							},
							data:con2
                        }
                    ]
                };
        
                // 为echarts对象加载数据 
                myChart.setOption(option); 
            }
        );
 }

 //页面初始化函数，通过POST返回一个默认值的直方图
function init(){
	var startTime=$("#startTime").val()
	var endTime=$("#endTime").val()
		$.post("http://localhost:8080/customers",
		{
        	"startTime":startTime,
			"endTime":endTime

        },
		function (data,status) {
			console.log(data["cus1"],data["con1"],data["cus2"],data["con2"])
        	drawBar(data["cus1"],data["con1"],data["cus2"],data["con2"])
        	
    	}
	);
}

window.onload=init()
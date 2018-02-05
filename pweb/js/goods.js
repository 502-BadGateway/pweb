//确定按钮事件：调用drawBar()函数画出热销商品TOP10的条形图和单个热销商品热销原因分析的饼图
function submit(){
	var startTime=$("#startTime").val()
	var endTime=$("#endTime").val()
	$.ajax({
		type: "GET",  
        url: "http://localhost:8080/goods?startTime="+startTime+"&endTime="+endTime,
        contentType: "application/json",
        success: function (data) {
			console.log(data["data1"],data["data2"])
        	drawBar(data["data1"],data["data2"])
    	}
    })
}

//画出热销商品TOP10的条形图和单个热销商品热销原因分析的饼图
function drawBar(data1,data2){
	var dom = document.getElementById("container");
	var myChart = echarts.init(dom);
	var app = {};
	option = null;

	var builderJson = {
		"charts": data1
	};
	var downloadJson =data2;

	var waterMarkText = 'ECHARTS';

	var canvas = document.createElement('canvas');
	var ctx = canvas.getContext('2d');
	canvas.width = canvas.height = 100;
	ctx.textAlign = 'center';
	ctx.textBaseline = 'middle';
	ctx.globalAlpha = 0.08;
	ctx.font = '20px Microsoft Yahei';
	ctx.translate(50, 50);
	ctx.rotate(-Math.PI / 4);
	ctx.fillText(waterMarkText, 0, 0);

	option = {
		backgroundColor: {
			type: 'pattern',
			image: canvas,
			repeat: 'repeat'
		},
		tooltip: {},
		title: [{
			text: '热销商品排名',
			x: '25%',
			textAlign: 'center'
		}, {
			text: '单个商品热销分析',
			x: '75%',
			textAlign: 'center'
		}],	
		grid: [{
			top: 50,
			width: '50%',
			bottom: 10,
			left: 20,
			containLabel: true
		}, {
			top: '55%',
			width: '50%',
			bottom: 0,
			left: 10,
			containLabel: true
		}],
		xAxis: [{
			type: 'value',
			max: builderJson.all,
			splitLine: {
				show: false
			}
		}],
		yAxis: [{
			type: 'category',
			data: Object.keys(builderJson.charts),
			axisLabel: {
				interval: 0,
				rotate: 30
			},
			splitLine: {
				show: false
			}
		}],
		series: [{
			type: 'bar',
			stack: 'chart',
			z: 3,
			label: {
				normal: {
					position: 'right',
					show: true
				}
			},
			data: Object.keys(builderJson.charts).map(function (key) {
				return builderJson.charts[key];
			})
		}, {
			type: 'pie',
			radius: [0, '50%'],
			center: ['75%', '50%'],
			data: Object.keys(downloadJson).map(function (key) {
				return {
					name: key.replace('.js', ''),
					value: downloadJson[key]
				}
			})
		}]
	};
	if (option && typeof option === "object") {
		myChart.setOption(option, true);
	}
}

 //页面初始化函数，通过POST返回一个默认值的条形图和饼图
function init(){

	$.ajax({
		type: "POST",  
        url: "http://localhost:8080",
        contentType: "application/json",
        success: function (data) {
        	console.log(data["data1"],data["data2"])
        	drawBar(data["data1"],data["data2"])
        	
    	}
    })
}

window.onload=init()
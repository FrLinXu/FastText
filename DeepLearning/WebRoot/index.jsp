<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@ page language="java" import="bean.PageBean" %>
<%@ page language="java" import="bean.TableBean"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>法律类案要素提取系统</title>
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="css/bootstrap-theme.css">
	<link rel="stylesheet" type="text/css" href="css/bootstrap-theme.min.css">
	
	<script type="text/javascript"  src="js/jquery-1.11.0.min.js"></script>
	<script type="text/javascript"  src="js/bootstrap.js"></script>
	<script type="text/javascript"  src="js/bootstrap.min.js"></script>
	<script type="text/javascript"  src="js/echarts.js"></script>
		<script type="text/javascript">
		
		$(document).on("click", ".edit_btn", function() {
		    var tr = $(this).parent().parent()
		    var fact = tr.children('.fact').text()
		    var cri =tr.children('.cri').text()
			$("#showtext").text(fact)
			$("#showcri").text(cri)
			$("#myModal").modal({
			
			});
			
		});
		$(document).on("click", "#submitfact", function() {
		    $("#fact").text ( $("#showtext").text () )
			$("#myModal").modal('hide')
			
		});
		
		
	</script>
	
	
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">

	-->
  </head>
  
 <body>
<style type="text/css">

	body{

			background: url('img/1.jpeg');
		}
		
	p{
		font-size: 16px;
		font-family: "微软雅黑"


	}
	#top {
		color: blue;
		
	}
	table
	{
	 table-layout : fixed;
	 
	}
	td{
	white-space : nowrap ;
	overflow : hidden  ;
	text-overflow : ellipsis;
	}
	
</style>

<script>
 $(function() {
 		
        $("#myButton").click(function(){
            $(this).button('loading')
            fact =$("#fact").val ()
            $.ajax(
            {
             type: "POST",                           //传数据的方式
             url: "Deal?fact="+fact, //servlet地址
             
             data:{},
             success : function (result)
             {
             $("#keyword").val ("<%=request.getSession().getAttribute("keyword") %>")
             }
            }
            );
           
             //$(this).button('reset');
             //$(this).dequeue(); 
            
        });
    });  
</script>


<div class="container" id ="top" >
	<div class="row">
		<div class="col-md-4 col-md-offset-4" >
			<p>基于深度学习的法律类案提取系统</p>
		</div>
		<div  class="col-md-4 col-md-offset-4">
			<p>1500330316卢俊</p>
		</div>
	</div>	

</div>
<div class="container" id ="mid ">


		<!-- Modal -->
		<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
			<div class="modal-dialog" role="document">
				<div class="modal-content">
					<div class="modal-header">
						<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
						<h4 class="modal-title" id="myModalLabel">查看相关信息</h4>
					</div>
					<div class="modal-body">
						 <p>案件描述</p><br>
						 <p id="showtext"></p>
						 <p>案件所属类型</p><br>
						 <p id="showcri"></p>
					</div>
					<div class="modal-footer">
						<button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
						<button type="button" class="btn btn-primary" id="submitfact">添加到文本</button>
					</div>
				</div>
			</div>
		</div>

<!--  图表  -->


		<div class="row">	

			<div class="col-md-6" style="height:450px;">	
				<div style="height: 350px;">
					

					<table class="table table-hover" >
						<thead>
							<tr>
								<th>事件 </th>
								<th>罪名</th>
								<th> </th>	
							</tr>
							
						</thead>
						
						<tbody>
							<% 
							
							if( request.getSession().getAttribute("pb") !=null)
							{
								PageBean<TableBean>  pb= (PageBean<TableBean>) request.getSession().getAttribute("pb");
								for (TableBean tb :pb.getBeanList() )
								{
									out.print("<tr>");
									out.print("<td class=\"fact\">");
									out.print(tb.getFact());
									out.print("</td>");
									out.print("<td class=\"cri\">");
									out.print(tb.getCri());
									out.print("</td>");
									out.print("<td><button type=\"button\" class=\"btn btn-success edit_btn	\"> 查看信息</button></td>");
									out.print("</tr>");
								}
								
							 %>
							<% 	
							}
							%>
							
				</tbody>
			</table>
		</div>

		<div>
			<nav aria-label="Page navigation" >
				<ul class="pagination" >
				
					<li>
						<a href="./PageAction?jumppage=<%= ((PageBean<TableBean>) request.getSession().getAttribute("pb"))
						==null ? 0:
							((PageBean<TableBean>) request.getSession().getAttribute("pb")).getPageCode() - 1 %>" aria-label="Previous">
							<span aria-hidden="true">&laquo;</span>
						</a>
					</li>
					<li>
						<a href="./PageAction?jumppage=<%= ((PageBean<TableBean>) request.getSession().getAttribute("pb"))
						==null ? 0:
							((PageBean<TableBean>) request.getSession().getAttribute("pb")).getPageCode() + 1 %>" aria-label="Next">
							<span aria-hidden="true">&raquo;</span>
						</a>
					</li>


				</ul>
			</nav>
		</div>
	</div>

	<!--  pie charts -->
	<div class="col-md-6">	
		<div style="width:100%;height:450px;float:left" id="chartmain"></div>

		<script type="text/javascript">
			window.onload = function (){
		//指定图表的配置项和数据

		option = {

			title : {
				text: '系统数据分析',
				subtext: '训练数据比例图',
				x:'center'
			},
			tooltip : {
				trigger: 'item',
				formatter: "{a} <br/>{b} : {c} ({d}%)"
			},
			legend: {
				orient: 'vertical',
				left: 'left',
				data: ['诈骗','其它','故意伤害','走私','盗窃']
			},
			grid: {show:'true',borderWidth:'0'},
			series : [
			{
				name: '访问来源',
				type: 'pie',
				radius : '55%',
				center: ['50%', '60%'],
				data:[
				{value:203652, name:'诈骗'},
				{value:235222, name:'其它'},
				{value:329722, name:'故意伤害'},
				{value:205235, name:'走私'},
				{value:362113, name:'盗窃'}
				],
				itemStyle: {
					emphasis: {
						shadowBlur: 10,
						shadowOffsetX: 0,
						shadowColor: 'rgba(0, 0, 0, 0.5)'
					}
				}
			}
			]
		};

			//获取dom容器
			var myChart = echarts.init(document.getElementById('chartmain'));
			// 使用刚指定的配置项和数据显示图表。
			myChart.setOption(option);
		}
	</script>

</div>



</div>


<!-- 案件输入-->

<form action="./Deal" method="post">
 <div class="row">
  <div class="col-md-6">
  <label for="fact">案件描述信息</label>	
  <textarea type="text" class="form-control" name ="fact" id="fact" placeholder="请在此输入案件信息" rows="28">
    <%if(request.getSession().getAttribute("fact")!=null){ %>
       <%=request.getSession().getAttribute("fact") %>
        <%} %>
   </textarea>
<input type="submit" value="分析"/>
</form> 
 </div>
  <div class="col-md-6">
  <div class="row">
  <label for="place">案件发生地点</label>	
  <textarea type="text" class="form-control" id="palce"  rows="3"  readonly>
   <%if(request.getSession().getAttribute("locate")!=null){ %>
       <%=request.getSession().getAttribute("locate") %>
        <%} %>
  </textarea>
  </div>
  <div class="row">
  <label for="time">案件发生时间</label>	
  <textarea type="text" class="form-control" id="time" rows="3"   readonly> 
   <%if(request.getSession().getAttribute("time")!=null){ %>
       <%=request.getSession().getAttribute("time") %>
  		 <%} %>
  </textarea>
  </div>
  <div class="row">
  <label for="person">案件发生人物</label>	
  <textarea type="text" class="form-control" id="person"  rows="3"  readonly>
   <%if(request.getSession().getAttribute("person")!=null){ %>
       <% ArrayList <String> person  = (ArrayList <String> )request.getSession().getAttribute("person");%>
       <%= person %>
        <%  } %>
   </textarea>
  </div>
  <div class="row">
  	 <label for="keyword">案件关键句提取</label>	
  	 <textarea type="text" class="form-control" id="keyword" rows="5" readonly>
       <%if(request.getSession().getAttribute("keyword")!=null){ %>
       <%=request.getSession().getAttribute("keyword") %>
       <%} %>
  	 </textarea> 
  </div>
   <div class="row">
  	 <label for="cri">罪名预测</label>	
  	 <textarea type="text" class="form-control" id="cri"  rows="4" readonly> 
  	 <%if(request.getSession().getAttribute("cri")!=null){ %>
       <%=request.getSession().getAttribute("cri") %>
       <%} %>
  	 </textarea>
  </div>
 </div>
	
</div>
<div>
	<div class="container" id ="top" >
	<div class="row">
		<div class="col-md-4 col-md-offset-4" >
			<p  style ="font-family:TimeNewRoman">Guilin University Of Electronic Technology</p>
		</div>
		<div  class="col-md-4 col-md-offset-4">
			<p style ="font-family:TimeNewRoman">Design  By LuJun</p>
		</div>
	</div>	

</div>
</div>
</body>
</html>

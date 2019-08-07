package Servlet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.nio.charset.Charset;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.json.JSONArray;
import org.json.JSONObject;

import com.baidu.aip.nlp.AipNlp;

/**
 * Servlet implementation class Deal
 */
@WebServlet("/Deal")
public class Deal extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Deal() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setContentType("text/html");
		request.setCharacterEncoding("utf-8");
		response.setCharacterEncoding("UTF-8");
		 PrintWriter out = response.getWriter();
		 String fact =request.getParameter("fact") ;
		 request.getSession().setAttribute("fact", fact);
		 System.out.println (fact);
		 
		    String SECRET_KEY = "ByM5ylc8vhxA4BOGHZCjxhXV616idS5w";
		    
		    	try
		    	{
		        // 初始化一个AipNlp
		        AipNlp client = new AipNlp("16250548", "2NjQ8gXPjPDSY3MbbbvD8doM", "ByM5ylc8vhxA4BOGHZCjxhXV616idS5w");

		        // 可选：设置网络连接参数
		        client.setConnectionTimeoutInMillis(2000);
		        client.setSocketTimeoutInMillis(60000);

		       

		        // 调用接口
		        String text = fact;
		        JSONObject res = client.lexer(text, null);
		        
		       
		        JSONArray jslist = res.getJSONArray("items") ;
		        
		        
		        ArrayList <String> per = new ArrayList <String > () ;
		        String loc="";
		        String ti="";
		       for (int count =0 ; count < jslist.length(); count++)
		        {
		        	JSONObject t = jslist.getJSONObject(count);
		  
		        	if ("PER".equalsIgnoreCase(t.getString("ne").trim()))
		        	{
		        		boolean ex =false ;
		        		String person = t.getString("item").trim() ;
		        		for (String p : per )
		        		{
		        		if (p.equals(person))
		        		ex= true ;
		        		}
		        		if (!ex) per.add(person) ;
		        	}
		        	else if ("LOC".equalsIgnoreCase(t.getString("ne").trim()))
		        	{
		        		String locate = t.getString("item");
		        		loc += locate+" ";
		        		System.out.println (locate) ;
		        	}
		        	else if ("TIME".equalsIgnoreCase(t.getString("ne").trim()))
		        	{
		        		String time = t.getString("item" )  ;
		        		ti+=time+" ";
		        		System.out.println(time) ;
		        	}
		           
		        }
		        System.out.println(per+"\n"+loc+"\n"+ti);
		      
		        loc = loc.trim() ;
		        ti = ti.trim() ;
		        request.getSession().setAttribute("person", per);
		        request.getSession().setAttribute("locate", loc);
		        request.getSession().setAttribute("time", ti);
		       // System.out.println(res.toString(2));
		    	}
		    	catch (Exception e )
		    	{
		    		e.printStackTrace();
		    	}
		    
		
		 
		 //关键字提取
		 
	        try
	        {
	        	 String exe = "D:\\Anaconda\\envs\\tensorflow\\python.exe";
	   	       String command = "H:\\textrank_summary\\summary.py";
	   	        String[] cmdArr = new String[] {exe, command,fact};
	        Process process = Runtime.getRuntime().exec(cmdArr);
	        System.out.print(command);
	        InputStream is = process.getInputStream();
	        System.out.print(command);
	        BufferedReader dis = new BufferedReader(new InputStreamReader(process.getInputStream(), Charset.forName("GBK"))	);
	        String str ;
	        String keyword="";
	        
	        while ( (str =dis.readLine() )!=null)
	        {
	        	
	        	keyword+=str+"\n";
	        }
	    	process.waitFor();

	        System.out.println(keyword);
			 
			 request.getSession().setAttribute("keyword", keyword);
	        }
	        catch (Exception e )
	        {
	        	e.printStackTrace();
	        }
	       
	        //罪名预测
	        try
	        {
	        	 String exe = "D:\\Anaconda\\envs\\tensorflow\\python.exe";
	   	       String command = "F:\\FastTextpredict\\accpredict.py";
	   	        String[] cmdArr = new String[] {exe, command,fact};
	        Process process = Runtime.getRuntime().exec(cmdArr);
	        System.out.print(command);
	        InputStream is = process.getInputStream();
	        System.out.print(command);
	        BufferedReader dis = new BufferedReader(new InputStreamReader(process.getInputStream(), Charset.forName("GBK"))	);
	        String str ;
	        String cri="";
	        
	        while ( (str =dis.readLine() )!=null)
	        {
	        	
	        	cri+=str;
	        }
	    	process.waitFor();

	        System.out.println(cri);
			 
			 request.getSession().setAttribute("cri", cri);
	        }
	        catch (Exception e )
	        {
	        	e.printStackTrace();
	        }
	        
	       response.sendRedirect("index.jsp");
	     
	        
	     
	        

		 
		 
	}

}

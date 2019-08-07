package Servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import bean.PageBean;
import bean.TableBean;
import bean.Test;

/**
 * Servlet implementation class PageAction
 */
@WebServlet("/PageAction")
public class PageAction extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public PageAction() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setContentType("text/html");
		request.setCharacterEncoding("utf-8");
		response.setCharacterEncoding("UTF-8");
		PrintWriter out = response.getWriter();
		
		PageBean <TableBean> pb = (PageBean<TableBean>) request.getSession().getAttribute("pb") ;
		if (pb == null )
		{
			pb = new PageBean <TableBean> () ;
			pb=Test.GetPb(0, 6);
		}
		else
		{
			int jumpage=0;
			try
			{
				jumpage = Integer.parseInt(request.getParameter("jumppage"))  ;
			}
			catch (Exception e )
			{
				
			}
			pb = Test.GetPb(jumpage, 6) ;
		}

		request.getSession().setAttribute("pb",pb);
		
		   
	     response.sendRedirect("index.jsp");
	     
		
	
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
		doGet(request, response);
	}

}

package bean;


import java.sql.*;
import java.util.ArrayList;

import com.mysql.jdbc.PreparedStatement;

public class Test {

	public static void main (String args []) 
	{
		ArrayList<TableBean>  listtable = new ArrayList<TableBean> () ;
		try
		{
			String sql ="select * from caseinfo";
			Connection conn = (Connection) JdbcBean.getConn();
			PreparedStatement pst = JdbcBean.getPStm(conn, sql);
			ResultSet rs = pst.executeQuery();
			while (rs.next())
			{
				String fact = rs.getString("fact") ;
				String cri =rs.getString("accusation") ;
			    listtable.add(new TableBean (fact ,cri) ) ;
			}
			JdbcBean.close(conn);
			JdbcBean.close(pst);
			int nowpage =1;
			int pagesize =5;
			PageBean<TableBean> pb = new PageBean<TableBean> () ;
			ArrayList<TableBean>  newlist = new ArrayList<TableBean> () ;
			for (int i=nowpage*pagesize ; i< (nowpage+1)*pagesize ;i++ )
			newlist.add(listtable.get(i)) ;
			
			pb.setPageSize(5); //·ÖÒ³
			pb.setTotalRecord(listtable.size());
			
			for (TableBean tb : newlist )
			{
				System.out.println(tb.getCri()); 
			}
		}
		
		catch (Exception e )
		{
			e.printStackTrace();
		}
	}

	public static PageBean<TableBean> GetPb (int nowpage ,int pagesize ) 
	{
		ArrayList<TableBean>  listtable = new ArrayList<TableBean> () ;
		try
		{
			String sql ="select * from caseinfo";
			Connection conn = (Connection) JdbcBean.getConn();
			PreparedStatement pst = JdbcBean.getPStm(conn, sql);
			ResultSet rs = pst.executeQuery();
			while (rs.next())
			{
				String fact = rs.getString("fact") ;
				String cri =rs.getString("accusation") ;
			    listtable.add(new TableBean (fact ,cri) ) ;
			}
			JdbcBean.close(conn);
			JdbcBean.close(pst);
			
			PageBean<TableBean> pb = new PageBean<TableBean> () ;
			ArrayList<TableBean>  newlist = new ArrayList<TableBean> () ;
			for (int i=nowpage*pagesize ; i< (nowpage+1)*pagesize ;i++ )
			newlist.add(listtable.get(i)) ;
			
			pb.setPageSize(5); //·ÖÒ³
			pb.setTotalRecord(listtable.size());
			pb.setPageCode(nowpage);
			System.out.println(nowpage);
			pb.setBeanList(newlist);
			
			return pb;
		}
		
		catch (Exception e )
		{
			e.printStackTrace();
		}
		return null;
	}
}

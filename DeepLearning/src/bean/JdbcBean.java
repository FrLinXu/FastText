package bean;

import java.sql.*;
import com.mysql.jdbc.PreparedStatement;
public class JdbcBean {
     public static Connection getConn() 
     {

         Connection conn = null;
        try {
             Class.forName("com.mysql.jdbc.Driver");
             conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/data_test?autoReconnect=true&useSSL=false","root","123456");
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
         return conn;
     }
     public static Statement getStmt(Connection conn) 
     {
         Statement stmt = null;
         try {
            stmt = conn.createStatement();
        } catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
         return stmt;
     }
     public static ResultSet getResu(Statement stmt , String sql) 
     {
         ResultSet rs = null;
         try {
            rs = stmt.executeQuery(sql);
        } catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
         return rs;
     }
     public static PreparedStatement getPStm(Connection conn , String sql)
     {
         PreparedStatement pstm = null;
         try {
            pstm = (PreparedStatement)conn.prepareStatement(sql);
        } catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
         return pstm;
     }
     public static void close(Connection conn)
     {
         if(conn!=null)
         {
             try {
                conn.close();
            } catch (SQLException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
         }
     }
     public static void close(Statement stmt)
     {
         if(stmt!=null)
         {
             try {
                stmt.close();
            } catch (SQLException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
         }
     }
     public static void close(ResultSet rs)
     {
         if(rs!=null)
         {
             try {
                rs.close();
            } catch (SQLException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
         }
     }
}
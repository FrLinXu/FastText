package bean;

public class TableBean {

	String fact ;
	String cri ;
	
	public TableBean () 
	{
		
	}
	public TableBean (String fact , String cri)
	{
		this.fact =fact;
		this.cri =cri ;
		
	}
	public String getFact() {
		return fact;
	}
	public void setFact(String fact) {
		this.fact = fact;
	}
	public String getCri() {
		return cri;
	}
	public void setCri(String cri) {
		this.cri = cri;
	}
	
	
}

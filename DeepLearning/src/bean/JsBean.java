package bean;

import java.util.ArrayList;

public class JsBean {

	public class Item 
	{
		 int byte_length;
         int byte_offset;
         String formal;
         public int getByte_length() {
			return byte_length;
		}
		public void setByte_length(int byte_length) {
			this.byte_length = byte_length;
		}
		public int getByte_offset() {
			return byte_offset;
		}
		public void setByte_offset(int byte_offset) {
			this.byte_offset = byte_offset;
		}
		public String getFormal() {
			return formal;
		}
		public void setFormal(String formal) {
			this.formal = formal;
		}
		public String getItem() {
			return item;
		}
		public void setItem(String item) {
			this.item = item;
		}
		public String getNe() {
			return ne;
		}
		public void setNe(String ne) {
			this.ne = ne;
		}
		public String getPos() {
			return pos;
		}
		public void setPos(String pos) {
			this.pos = pos;
		}
		public String getUri() {
			return uri;
		}
		public void setUri(String uri) {
			this.uri = uri;
		}
		public String getLoc_details() {
			return loc_details;
		}
		public void setLoc_details(String loc_details) {
			this.loc_details = loc_details;
		}
		public String getBasic_words() {
			return basic_words;
		}
		public void setBasic_words(String basic_words) {
			this.basic_words = basic_words;
		}
		String item;
         String ne;
         String pos;
         String uri;
         String  loc_details;
         String basic_words;
	}
	public String text ;
	ArrayList <Item> items ;
	public String getText() {
		return text;
	}
	public void setText(String text) {
		this.text = text;
	}
	public ArrayList<Item> getItems() {
		return items;
	}
	public void setItems(ArrayList<Item> items) {
		this.items = items;
	}
	
	
	
}

package com;

public class Train {

	private int train_no;
	private String train_name;
	private String arrival_time;
	private String departure_time;
	private String journey_time;
	public Train() {
		super();
	}
	public Train(int train_no, String train_name, String arrival_time, String departure_time, String journey_time) {
		super();
		this.train_no = train_no;
		this.train_name = train_name;
		this.arrival_time = arrival_time;
		this.departure_time = departure_time;
		this.journey_time = journey_time;
	}
	public int getTrain_no() {
		return train_no;
	}
	public void setTrain_no(int train_no) {
		this.train_no = train_no;
	}
	public String getTrain_name() {
		return train_name;
	}
	public void setTrain_name(String train_name) {
		this.train_name = train_name;
	}
	public String getArrival_time() {
		return arrival_time;
	}
	public void setArrival_time(String arrival_time) {
		this.arrival_time = arrival_time;
	}
	public String getDeparture_time() {
		return departure_time;
	}
	public void setDeparture_time(String departure_time) {
		this.departure_time = departure_time;
	}
	public String getJourney_time() {
		return journey_time;
	}
	public void setJourney_time(String journey_time) {
		this.journey_time = journey_time;
	}
	@Override
	public String toString() {
		return "Train [train_no=" + train_no + ", train_name=" + train_name + ", arrival_time=" + arrival_time
				+ ", departure_time=" + departure_time + ", journey_time=" + journey_time + "]";
	}
	
	
}

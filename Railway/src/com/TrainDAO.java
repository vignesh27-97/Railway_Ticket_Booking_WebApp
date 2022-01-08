package com;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

public class TrainDAO {

	public ArrayList<Train> getAllTrains(String x,String y){
		ArrayList<Train> trainList = new ArrayList<Train>();
		Connection con = null;
		PreparedStatement pst = null;
		try{
		con = DBUtil.getMyDBConnection();
		String x1=x;
		String y1=y;
		pst = con.prepareStatement("select * from "+x1+"To"+y1);
		ResultSet rs = pst.executeQuery();
		while(rs.next()){
			Train s = new Train(rs.getInt(1), rs.getString(2),
								rs.getString(3),rs.getString(4),rs.getString(5));
			trainList.add(s);
		}
		}catch(Exception e){
			System.out.println(e);
		}
		return trainList;
	}
}

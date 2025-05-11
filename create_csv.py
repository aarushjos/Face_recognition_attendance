import pandas
student_list=[] #Enter names corresponding to IDS (eg if 1 is john then student_list[0]=John)
data_dict={"Students":student_list}
data_frame=pandas.DataFrame(data_dict)

data_frame.to_csv("Attendance_Records.csv",index=False)


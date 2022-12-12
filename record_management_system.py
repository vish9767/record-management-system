from tkinter import *
from tkinter import messagebox
frame=Tk()
frame.attributes("-fullscreen",True)
frame.title("Record managemnet system")
#frame.geometry("1200x600")
px=30
py=40


bt=Button(frame,text="X Close",bg="red",command=frame.destroy)
bt.place(x=1450)
he=Label(frame,text=" Welcome to Student record managment system ",font=("Arial",25))
he.pack(padx=px, pady=py)
h3=Label(frame,text=" ").pack()


#######################################################################################backgroundimage#################################################

bg=PhotoImage(file="my.png")
canvas1=Canvas(frame,width=2000,height=600)
canvas1.pack(fill="both", expand=True)


canvas1.create_image(0,0,image=bg,anchor="nw")



#####################################################################################Background Image ends###############################################

db={}
def new():
	newstd=Toplevel(frame,bg="#fff2f4")
	newstd.title(" Add new student ")
	newstd.geometry("1000x500")
	n1=Label(newstd,text=" Add new student data below ",font=("Arial",20),bg="#fff2f4").pack()
	sn=Label(newstd,text="Student First Name ",font=("Arial",15),bg="#fff2f4").pack()
	s1=Entry(newstd,font=("Arial",15))
	s1.pack()
	s4=Label(newstd,text="Student Last Name",font=("Arial",15),bg="#fff2f4").pack()
	sl=Entry(newstd,font=("Arial",15))
	sl.pack()
	sr=Label(newstd,text="Student Roll Number",font=("Arial",15),bg="#fff2f4")
	sr.pack()
	s2=Entry(newstd,font=("Arial",15))
	s2.pack()
	sc=Label(newstd,text="Student contact Number",font=("Arial",15),bg="#fff2f4")
	sc.pack()
	s3=Entry(newstd,font=("Arial",15))
	s3.pack()
	def suc():
		roll=s2.get()
		print(type(roll))
		sd={}
		if(roll in db):
			#print("roll number is already available in database")
			#err=Label(newstd,text=" This Roll numbers is already available in database ").pack()
			messagebox.showinfo(" Student Exist ",'{r} Roll already availabel in db '.format(r=roll))
		else:
			fname=sl.get()
			name=s1.get()
			contact=s3.get()
			sd['Name']=name
			sd['Roll']=roll
			sd['contact']=contact
			sd['lName']=fname
			db[roll]=sd
			s=Label(newstd,text="new student added sucessfully",font=("Arial",15),bg="#fff2f4")
			s.pack()

	s55=Label(newstd,font=("Arial",15)).pack()
	but=Button(newstd,text="submit",command=suc,font=("Arial",17),bg="#ADD8E6").pack()
def dis():
	if(len(db)!=0):
		disp=Toplevel(frame,bg="#fff2f4")
		disp.title(" Student data ")
		disp.geometry("1000x500")
		tr=Label(disp,text="*"*200,bg="#ADD8E6").pack()
		tr1=Label(disp,text="| {fname:^50} | {lname:^50} | {ro:^50} | {co:^50} |".format(fname='First Name',lname='Last Name',ro='Roll No',co='Contact'),bg="#ADD8E6").pack()
		tr2=Label(disp,text="*"*200,bg="#ADD8E6").pack()
		for i in db.values():
			d1=Label(disp,text="| {fn:^50}|{na:^50} | {ro:^50} | {co:^50}  |".format(fn=i["lName"],ro=i['Roll'],na=i['Name'],co=i['contact']),bg="#fff2f4").pack()
	else:
		messagebox.showinfo("NO Record Available",' Plz add record ')
def dell():
	if(len(db)!=0):
		de=Toplevel(frame,bg="#ffa590")
		de.title("Delete Student record")
		de.geometry("1000x500")
		f=Label(de,bg="#ffa590").pack()
		d5=Label(de,text="Enter student Roll no to Delete Student Data",font=("Arial",20),bg="#ffa590").pack()
		en=Entry(de,font=("Arial",15))
		en.pack(pady=30)
		def work():
			rol=en.get()
			if (rol in db):
				del db[rol]
				if(rol not in db):
					#print("{rol} deleted sucessfully")
					#de1=Label(de,text=" Student record Deleted sucessfully").pack()
					messagebox.showinfo("Record Deleted" ,"Record Deleted Sucessfully")
				else:
					print("student record is not deletd plz try again ")
			else:
				el=Label(de,text="Roll number is wrong",font=("Arial",20)).pack()
		bt=Button(de,text="Delete",command=work,font=("Arial",15),bg="#ff6242").pack()

	else:
		messagebox.showinfo("No Record",'Record is not available to delete')
def update():
	if(len(db)!=0):
		up=Toplevel(frame,bg="#fff2f4")
		up.geometry("1000x500")
		f=Label(up,bg="#fff2f4").pack()
		en=Label(up,text="Enter student roll no to update data",font=("Arial",20),bg="#fff2f4").pack(pady=30)
		en5=Entry(up,font=("Arial",15))
		en5.pack()
		f1=Label(up,bg="#fff2f4").pack()
		def updat():
			inp=en5.get()
			if(inp in db):
				
				last=Toplevel(up,bg="#fff2f4")
				sn=Label(last,text="Student first Name",font=("Arial",15),bg="#fff2f4").pack()
				s1=Entry(last)
				s1.pack()
				s4=Label(last,text="Student Last Name",font=("Arial",15),bg="#fff2f4").pack()
				sl=Entry(last,font=("Arial",15))
				sl.pack()
				sc=Label(last,text="Student contact Number",font=("Arial",15),bg="#fff2f4")
				sc.pack()
				s3=Entry(last,font=("Arial",15))
				s3.pack()
				
				def final():
					fname=sl.get()
					name=s1.get()
					contact=s3.get()
					#sd['Name']=name
					#sd['contact']=contact
					#sd['lName']=fname
					#db[roll]=sd
					db[inp]['Name']=name
					db[inp]['contact']=contact
					db[inp]['lName']=fname
					messagebox.showinfo("Updated","Roll No: {r} student data updated sucessfully".format(r=inp))
					#s=Label(,text="Roll No: ",inp," student data updated sucessfully",font=("Arial",20))
					#s.pack()
				butto=Button(last,text="update",command=final,font=("Arial",15),bg="#ADD8E6")
				butto.pack()
			else:
				messagebox.showinfo("Not found","Wrong Roll NO")
	
		but=Button(up,text="Submit",command=updat,font=("Arial",15)).pack()
	else:
		messagebox.showinfo("NO Record","NO Record is Available to Delete")

		

button1=Button(frame,text="Add new student",font=("Arial",20),command=new,bg="pink")
#button1.grid(row=3,column=3)
button1.place(x=300,y=200)
#button1.pack(side=LEFT,padx=30,pady=300)
button2=Button(frame,text=" Display student record ",font=("Arial",20),command=dis,bg="pink")
#button2.pack(side=RIGHT)
button2.place(x=900,y=200)
button3=Button(frame,text=" Delete student record",font=("Arial",20),command=dell,bg="red")
#button3.pack(side=LEFT,padx=30)
button3.place(x=300,y=400)
button4=Button(frame,text=" update student data",font=("Arial",20),command=update,bg="pink")
#button4.pack(side=RIGHT)
button4.place(x=900,y=400)
frame.mainloop()
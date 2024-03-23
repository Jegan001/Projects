from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

def screen_window(title,button_text,command):
    global id_entry,name_entry,mob_entry,email_entry,address_entry,gender_entry,dob_entry,screen
    screen = Toplevel()
    screen.geometry('500x610')
    screen.resizable(0,0)
    screen.title(title)
    screen.grab_set()

    # label
    id =Label(screen,text ='ID ',font=("time new roman",20,'bold'))
    id.grid(row=0,column=0,padx=20,pady=20,sticky=W)

    name =Label(screen,text ='NAME ',font=("time new roman",20,'bold'))
    name.grid(row=1,column=0,padx=20,pady=20,sticky=W)

    mobilenumber=Label(screen,text ='MOB ',font=("time new roman",20,'bold'))
    mobilenumber.grid(row=2,column=0,padx=20,pady=20,sticky=W)

    email =Label(screen,text ='EMAIL ',font=("time new roman",20,'bold'))
    email.grid(row=3,column=0,padx=20,pady=20,sticky=W)

    address =Label(screen,text ='ADDRESS ',font=("time new roman",20,'bold'))
    address.grid(row=4,column=0,padx=20,pady=20,sticky=W)

    gender =Label(screen,text ='GENDER ',font=("time new roman",20,'bold'))
    gender.grid(row=5,column=0,padx=20,pady=20,sticky=W)

    dob =Label(screen,text ='D.O.B ',font=("time new roman",20,'bold'))
    dob.grid(row=6,column=0,padx=20,pady=20,sticky=W)

    # entry
    id_entry =Entry(screen,bd=2,width=25,font=('roman',15,'bold'))
    id_entry.grid(row=0,column=1,padx=20,pady=20)
    
    name_entry =Entry(screen,bd=2,width=25,font=('roman',15,'bold'))
    name_entry.grid(row=1,column=1,padx=20,pady=20)

    mob_entry =Entry(screen,bd=2,width=25,font=('roman',15,'bold'))
    mob_entry.grid(row=2,column=1,padx=20,pady=20)

    email_entry =Entry(screen,bd=2,width=25,font=('roman',15,'bold'))
    email_entry.grid(row=3,column=1,padx=20,pady=20)

    address_entry =Entry(screen,bd=2,width=25,font=('roman',15,'bold'))
    address_entry.grid(row=4,column=1,padx=20,pady=20)

    gender_entry =Entry(screen,bd=2,width=25,font=('roman',15,'bold'))
    gender_entry.grid(row=5,column=1,padx=20,pady=20)
    
    dob_entry =Entry(screen,bd=2,width=25,font=('roman',15,'bold'))
    dob_entry.grid(row=6,column=1,padx=20,pady=20)

    # button
    submit_button =ttk.Button(screen,text= button_text,command=command)
    submit_button.grid(row=7,columnspan =2,pady=20)

    if button_text =='UPDATE STUDENT':
        index=student_table.focus()
        content=student_table.item(index)

        data=content['values']
        id_entry.insert(0,data[0])
        name_entry.insert(0,data[1])
        mob_entry.insert(0,data[2])
        email_entry.insert(0,data[3])
        address_entry.insert(0,data[4])
        gender_entry.insert(0,data[5])
        dob_entry.insert(0,data[6])


def clock():
    global current_date,current_time
    current_date =time.strftime("%d/%m/%Y")
    current_time =time.strftime("%H:%M:%S")
    datetime_label.config(text=f"   Date: {current_date}\nTime: {current_time}")
    datetime_label.after(10,clock)

count=0
l =''
s= "Student Management System"
def slide():
    global count,l
    if count == len(s):
        l=''
        count =0
    
    l += s[count]
    slide_label.config(text=l,width=60)
    count+= 1
    slide_label.after(300,slide)

def database_connection():
    def connect():
        global con,mycursor
        try:
            con=pymysql.connect(host=host_entry.get(),user=user_entry.get(),password=password_entry.get())
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=host__window)
            return
        try:
            query ='create database StudentManagementSystem'
            mycursor.execute(query)
            query = 'use StudentManagementSystem'
            mycursor.execute(query)
            query = 'create table Student(Id int not null primary key ,Name varchar(30) ,Mobile_number varchar(10) ,Email varchar(30),address varchar(35),Gender varchar(10),D_O_B varchar(10),added_Date varchar(10),added_Time varchar(10))'
            mycursor.execute(query)
        except:
            query = 'use StudentManagementSystem'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database Connection Is Successful',parent=host__window)
        host__window.destroy()
        Add_button.config(state=NORMAL)
        search_button.config(state=NORMAL)
        update_button.config(state=NORMAL)
        delete_button.config(state=NORMAL)
        show_button.config(state=NORMAL)
        exportdata_button.config(state=NORMAL)
        

    host__window =Toplevel()
    host__window.geometry("500x280+730+230")
    host__window.title("Connect Database")
    host__window.resizable(0,0)

    # labels
    host_name=Label(host__window,text="Host Name :",font=("arial",20,'bold'))
    host_name.grid(row=0,column=0,padx=20,pady=10)
    user_name=Label(host__window,text="User Name :",font=("arial",20,'bold'))
    user_name.grid(row=1,column=0,padx=20,pady=10)
    password=Label(host__window,text="Password  :",font=("arial",20,'bold'))
    password.grid(row=2,column=0,padx=20,pady=10)

    #entry
    host_entry =Entry(host__window,bd=2,width=25,font=('roman',15,'bold'))
    host_entry.grid(row=0,column=1,padx=20,pady=20)

    user_entry =Entry(host__window,bd=2,width=25,font=('roman',15,'bold'))
    user_entry.grid(row=1,column=1,padx=20,pady=20)

    password_entry =Entry(host__window,bd=2,width=25,font=('roman',15,'bold'))
    password_entry.grid(row=2,column=1,padx=20,pady=20)
    
    # button
    connect_button =ttk.Button(host__window,text="Connect",width=15,command=connect)
    connect_button.grid(row=3,padx=20,pady=20,columnspan=2)
    
    

def Add_data():
    if id_entry.get() == '' and name_entry.get() =='' and email_entry.get() =='' and address_entry.get() == '' and gender_entry.get() == '' and dob_entry.get() == '':
        messagebox.showerror('Error',"All Fields Are Required",parent=screen)
    else:
        current_date =time.strftime("%d/%m/%Y")
        current_time =time.strftime("%H:%M:%S")
        try:
            
            query ='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(id_entry.get(),name_entry.get(),mob_entry.get(),email_entry.get(),address_entry.get(),gender_entry.get(),dob_entry.get(),current_date,current_time))

            con.commit()
            result = messagebox.askyesno('Confirm','Data Added Successfully.Do You Want To Clean The Form? ',parent =screen)

            if result:
                id_entry.delete(0,END)
                name_entry.delete(0,END)
                mob_entry.delete(0,END)
                email_entry.delete(0,END) 
                address_entry.delete(0,END)
                gender_entry.delete(0,END)
                dob_entry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','Dublicate Id Not Allowed',parent=screen)
            return

        query =  'select * from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        student_table.delete(*student_table.get_children())
        for data in fetched_data:
            student_table.insert('',END,values = data)

def search_data():
    query = 'select * from student where id=%s or name=%s or mobile_number=%s or email=%s or address=%s or gender=%s or d_o_b=%s'
    mycursor.execute(query,(id_entry.get(),name_entry.get(),mob_entry.get(),email_entry.get(),address_entry.get(),gender_entry.get(),dob_entry.get()))
    student_table.delete(*student_table.get_children())
    fetch_data =mycursor.fetchall()
    for data in fetch_data:
        student_table.insert('',END,values=data)
    

def delete_details():
    index =student_table.focus()
    content =student_table.item(index)
    content_id =content['values'][0]
    query = 'delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Success',f'Id {content_id} Deleted Successfully.')

    query ='select * from student'
    mycursor.execute(query)
    fetch_data =mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetch_data:
        student_table.insert('',END,values=data)

def show_details():
    query ='select * from student'
    mycursor.execute(query)
    fetch_data =mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetch_data:
        student_table.insert('',END,values=data)

def update_data():
    query = 'update student set name=%s,mobile_number=%s,email=%s,address=%s,gender=%s,d_o_b=%s,Added_date=%s,Added_time=%s where id=%s'
    mycursor.execute(query,(name_entry.get(),mob_entry.get(),email_entry.get(),address_entry.get(),gender_entry.get(),dob_entry.get(),current_date,current_time,id_entry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {id_entry.get()} is Updated ')
    screen.destroy()
    query =  'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        student_table.insert('',END,values = data)

    
def exit_program(): 
    result=messagebox.askyesno('Confirm','Do You Want To Exit ?')
    if result:
        root.destroy()
    else:
        pass



def export_details():
    url =filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=student_table.get_children()
    list_data =[]
    for index in indexing:
        content=student_table.item(index)
        data=content['values']
        list_data.append(data)

    table = pandas.DataFrame(list_data,columns=['ID','NAME','MOBILE NUMBER','EMAILL','ADDRESS','GENDER','D.O.B','ADDED DATE','ADDED TIME'])
    table.to_csv(url,index=FALSE)
    messagebox.showinfo('Success''Successfully Saved')



root =ttkthemes.ThemedTk()
root.title("Student Management System")
root.geometry("1280x848+10+20")
root.resizable(0,0)
# theme
root.get_themes()
root.set_theme("radiance")


#date & time label
datetime_label =Label(root,font=("time new roman",'15','bold'))
datetime_label.place(x=10,y=5)
clock()

# slide_label ->student management system

slide_label =Label(root,font=("arial",'20','italic bold'))
slide_label.place(x=200,y=0)
slide()

#mysql connect button
database_connect =ttk.Button(root,text='Connect Database',command=database_connection)
database_connect.place(x=1100,y=0)

#left_frame

left_frame=Frame(root)
left_frame.place(x=50,y=80,width=300,height=650)

#left_frame logo

logo_image = PhotoImage(file='tkinter/logo_for_sme.png')
logo_label = Label(left_frame,image=logo_image)
logo_label.grid(row=0,column=0,pady=15)

#left_frame buttons

Add_button =ttk.Button(left_frame,text='Add Button',width=25,state=DISABLED,command=lambda:screen_window('Add Window','ADD STUDENT',Add_data))
Add_button.grid(row=1,column=0,pady=20)

search_button =ttk.Button(left_frame,text='Search Button',width=25,state=DISABLED,command=lambda:screen_window('Search Window','SEARCH STUDENT',search_data))
search_button.grid(row=2,column=0,pady=20)

update_button =ttk.Button(left_frame,text='Update Button',width=25,state=DISABLED,command=lambda:screen_window('Update Window','UPDATE STUDENT',update_data))
update_button.grid(row=3,column=0,pady=20)

delete_button =ttk.Button(left_frame,text='Delete Button',width=25,state=DISABLED,command = delete_details)
delete_button.grid(row=4,column=0,pady=20)

show_button =ttk.Button(left_frame,text='Show Student',width=25,state=DISABLED,command = show_details)
show_button.grid(row=5,column=0,pady=20)

exportdata_button =ttk.Button(left_frame,text='Export Data',width=25,state=DISABLED,command  =export_details)
exportdata_button.grid(row=6,column=0,pady=20)

exit_button =ttk.Button(left_frame,text='Exit',width=25,command = exit_program)
exit_button.grid(row=7,column=0,pady=20)

# right_frame

right_frame=Frame(root)
right_frame.place(x=400,y=80,width=820,height=620)

scrollbarx =Scrollbar(right_frame,orient=HORIZONTAL)
scrollbary =Scrollbar(right_frame,orient=VERTICAL)

student_table=ttk.Treeview(right_frame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)


scrollbarx.config(command=student_table.xview) 
scrollbary.config(command=student_table.yview)                                                 
scrollbarx.pack(side=BOTTOM,fill=X)
scrollbary.pack(side=RIGHT,fill=Y)

student_table.pack(fill=BOTH,expand=True)                  # pack mostly use for  up,down,left,right fixing. #fill use to fill the x and y  expand use to top to bottom.

student_table.heading('Id',text='Id')
student_table.heading('Name',text='Name')
student_table.heading('Mobile No',text='Mobile No')
student_table.heading('Email',text='Email')
student_table.heading('Address',text='Address')
student_table.heading('Gender',text='Gender')
student_table.heading('D.O.B',text='D.O.B')
student_table.heading('Added Date',text='Added Date')
student_table.heading('Added Time',text='Added Time')

student_table.column('Id',width=50,anchor=CENTER)
student_table.column('Name',width=300,anchor=CENTER)
student_table.column('Mobile No',width=200,anchor=CENTER)
student_table.column('Email',width=300,anchor=CENTER)
student_table.column('Address',width=300,anchor=CENTER)
student_table.column('Gender',width=110,anchor=CENTER)
student_table.column('D.O.B',width=150,anchor=CENTER)
student_table.column('Added Date',width=150,anchor=CENTER)
student_table.column('Added Time',width=150,anchor=CENTER)

style = ttk.Style()
style.configure('Treeview',rowheight = 40,font=('arial',12,'bold'),background='white')  #fieldbackground='skyblue'
style.configure('Treeview.Heading',font=('arial',13,'bold'),foreground='brown')
student_table.config(show='headings')


root.mainloop() 
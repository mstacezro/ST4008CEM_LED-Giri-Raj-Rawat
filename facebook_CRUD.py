'''
A Facebook database is created using SQLite3.
The title of the table is "user".
Several necessary input and output is carried out in a GUI prepared by importing "Tkinter.
The GUI allows addition, display and modification of instructions. 
'''

#import tkinter for GUI, sqlite3 for database 
from tkinter import *
from tkinter import ttk
import sqlite3

from tkinter import messagebox

#object name for the tkinter project
root=Tk()

#name/title for the project
root.title("Facebook")

#dimension, background color of project
root.geometry("540x420")
# root.resizable(0,0)     #nonresizable, for resizable (True,True)
root.config(bg='#3090C7')

#icon of facebook
##NOTE:  root.iconbitmap("*.ico") doesnot work in ubuntu
from PIL import Image, ImageTk
logo = ImageTk.PhotoImage(file='/home/mstacezro/Documents/SOFTWARICA/Programming and Algorithms--Giri Raj Rawat/CODES/S-Q-L-l-i-lt-e/data---boss/fb.png')
root.tk.call('wm', 'iconphoto', root._w, logo)

# DATABASES
#create a database or connect to one
conn=sqlite3.connect('user.db')

#create a cursor
'''
cursor class is an instance using which you can invoke methods that execute 
SQLite3 statements, fetch data from the result sets of the queries
'''
c=conn.cursor()

'''CREATE command is used to create a new SQLite database named "user. '''
# c.execute("""CREATE TABLE user(
#     first_name text,
#     last_name text,
#     age integer,
#     password text,
#     father_name text,
#     address text,
#     city text,
#     zipcode text
#     )""")
# print("Table created")

def submit():
    '''
    This function adds user details as data to the database table
    '''
    #connect to the database 
    conn=sqlite3.connect('user.db')

    #create cursor
    c=conn.cursor()

    '''INSERT INTO Statement is used to add new rows of data into a table in the database.'''
    #the values of attributes is obtained by .get() from respective entry box
    c.execute("INSERT INTO user VALUES(:f_name,:l_name,:age,:password,:father_name, :address,:city,:zipcode)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'age':age.get(),
        'password':password.get(),
        'father_name':father_name.get(),
        'address':address.get(),
        'city':city.get(),
        'zipcode':zipcode.get()
    })

    #messagebox to show when datas are added 
    messagebox.showinfo("Success","Record has been added")


    '''
    Once you are done with your changes and you want to commit the changes 
    then call .commit() method on connection object 
    '''
    #commit changes
    conn.commit()
    #close connection
    conn.close()

    #clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    age.delete(0,END)
    password.delete(0,END)
    father_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)

def query():
    '''
    SELECT statement is used to fetch the data from a SQLite database table 
    which returns data in the form of a result table. 
    These result tables are also called result sets.
    '''

    info_query=Toplevel()
    info_query.title("Datas of user")
    info_query.configure(bg='#B1FB17')

    #connect to main database
    conn=sqlite3.connect('user.db')
    c=conn.cursor()
    
    #create cursor
    c=conn.cursor()

    #select query of the database
    '''
    OID is auto-incrementing integer value,  
    that can be automatically assigned to each row of a table created WITH OIDS option.
    ID can be used as an identity (auto-increment) primary key column
    '''
    c.execute("SELECT *,oid FROM user")

    #Fetches the existing rows from a result set
    records=c.fetchall()
    print(records)
    

    #output of records in database
    #Loop through the results
    # for record in records:
    #     print_records+=str(record[0]) +' ' + str(record[1]) +" " + 2*'\t' + str(record[2])+ " " +'\t' + str(record[3])+ " " +'\t' + str(record[4])+ " " +'\t' + str(record[5])+ " " +'\t' + str(record[6])+ " " +'\t' + str(record[7]) + "\n"
    # query_label=Label(root,text=print_records, anchor="w")
    # query_label.grid(row=8,column=0,columnspan=4)

#...................

    
    
    columns = ('first_name', 'last_name', 'age','password','father_name','address','city','zipcode','Serial_No')
    

    tree = ttk.Treeview(info_query, columns=columns, show='headings')

    ##dimensions for the columns #BUG # no atomatic sizing
    # tree.column("# 1",anchor=CENTER, stretch=NO, width=30)
    # tree.column("# 2",anchor=CENTER, stretch=NO, width=100)
    tree.column("# 3",anchor=CENTER, stretch=NO, width=50)
    # tree.column("# 4",anchor=CENTER, stretch=NO, width=100)
    # tree.column("# 5",anchor=CENTER, stretch=NO, width=100)
    # tree.column("# 6",anchor=CENTER, stretch=NO, width=100)
    tree.column("# 7",anchor=CENTER, stretch=NO, width=150)
    tree.column("# 8",anchor=CENTER, stretch=NO, width=70)
    tree.column("# 9",anchor=CENTER, stretch=NO, width=30)
    

    # define headings
    tree.heading('first_name', text='First Name')
    tree.heading('last_name', text='Last Name')
    tree.heading('age', text='Age')
    tree.heading('password', text='Password')
    tree.heading('father_name', text='Father Name')
    tree.heading('address', text='Address')
    tree.heading('city', text='City')
    tree.heading('zipcode', text='Zipcode')
    tree.heading('Serial_No',text='S.N.')
    



    # query_label=Label(info_query,text=print_records, anchor="w")
    # query_label.grid(row=8,column=0,columnspan=4)

    # add data to the treeview
    for record in records:
        tree.insert('', END, values=record)

    #position of tree label
    tree.grid(row=0, column=0, sticky=NSEW)

    # vertical scrollbar
    vbar = ttk.Scrollbar(info_query, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=vbar.set)
    vbar.grid(row=0, column=1, sticky=NS)

    #horizontal scrollbar   #BUG #horizontal bar shows but doesnot work
    hbar = ttk.Scrollbar(info_query, orient=HORIZONTAL, command=tree.xview)
    tree.configure(xscrollcommand=hbar.set)
    hbar.grid(row=1, column=0, sticky=EW)
    

#......................

def delete():
    '''
    DELETE Query is used to delete the existing records from a table.
    You can use WHERE clause with DELETE query to delete the selected rows, 
    otherwise all the records would be deleted.
    '''
    #connect to database
    conn=sqlite3.connect('user.db')
    
    #create cursor
    c=conn.cursor()

    #delete the unnecessary row which is obtained using .get()
    c.execute("DELETE FROM user WHERE oid="+delete_box.get())

    #inform the user that the data row is deleted
    print("Deleted")

    #clears the delete box
    delete_box.delete(0,END)

    #commit changes
    conn.commit()
    conn.close()

def update():
    '''
    UPDATE Query is used to modify the existing records in a table. 
    You can use WHERE clause with UPDATE query to update selected rows, 
    otherwise all the rows would be updated.
    '''
    #connect to database

    conn=sqlite3.connect('user.db')
    #create cursor
    c=conn.cursor()
    
    #retrieve the row number of data to be updated by using .get() from entry box
    record_id=delete_box.get()

#update the data from the update window into facebook window
    c.execute("""Update user SET
    first_name=:first,
    last_name=:last,
    age=:age,
    password=:password,
    father_name=:father_name,
    address=:address,
    city=:city,
    zipcode=:zipcode
    WHERE oid=:oid""",
    {
        'first':f_name_editor.get(),
        'last':l_name_editor.get(),
        'age':age_editor.get(),
        'password':password_editor.get(),
        'father_name':father_name_editor.get(),
        'address':address_editor.get(),
        'city':city_editor.get(),
        'zipcode':zipcode_editor.get(),
        'oid':record_id
    })

    conn.commit()
    conn.close()

    #destroying all the data and closing window
    editor.destroy()

def edit():
    '''
    This block of function is opened when update is clicked in facebook window
    after required row is determined. 
    If row is not specified, it opens an empty window.
    '''
    #new window editor is created with specific designs,backgrounds

    #global identifier to enable modification 
    global editor

    #The toplevel widget is used when a python application needs to represent 
    # some extra information, pop-up, or the group of widgets on the new window.
    editor=Toplevel()
    editor.title("Editor")
    editor.geometry("400x300")
    editor.configure(bg='#B1FB17')

    #connect to main database
    conn=sqlite3.connect('user.db')
    c=conn.cursor()

    #SELECT retrieves all data respective to the row in given box with .get()
    record_id=delete_box.get()
    c.execute("SELECT * FROM user WHERE oid="+record_id)
    records=c.fetchall()

#global editors for modification
    global f_name_editor
    global l_name_editor
    global age_editor
    global password_editor
    global father_name_editor
    global address_editor
    global city_editor
    global zipcode_editor

    # Create labels for the update dialog box
    f_name_editor_label=Label(editor,text="First Name",width=15, anchor="w",bg='#C04000',fg='white')
    f_name_editor_label.grid(row=0,column=0,pady=(10,0))

    l_name_editor_label=Label(editor,text="Last Name",width=15, anchor="w",bg='#C04000',fg='white')
    l_name_editor_label.grid(row=1,column=0)

    age_editor_label=Label(editor,text="Age",width=15, anchor="w",bg='#C04000',fg='white')
    age_editor_label.grid(row=2,column=0)

    password_editor_label=Label(editor,text="Password",width=15, anchor="w",bg='#C04000',fg='white')
    password_editor_label.grid(row=3,column=0)

    father_name_editor_label=Label(editor,text="Father Name",width=15, anchor="w",bg='#C04000',fg='white')
    father_name_editor_label.grid(row=4,column=0)

    address_editor_label=Label(editor,text="Address",width=15, anchor="w",bg='#C04000',fg='white')
    address_editor_label.grid(row=5,column=0)

    city_editor_label=Label(editor,text="City",width=15, anchor="w",bg='#C04000',fg='white')
    city_editor_label.grid(row=6,column=0)

    zipcode_editor_label=Label(editor,text="zipcode",width=15, anchor="w",bg='#C04000',fg='white')
    zipcode_editor_label.grid(row=7,column=0)


    # Create text boxes for updating new data in a new window
    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))

    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1,padx=20)

    age_editor=Entry(editor,width=30)
    age_editor.grid(row=2,column=1,padx=20)

    password_editor=Entry(editor,width=30,show="*")
    password_editor.grid(row=3,column=1,padx=20)

    father_name_editor=Entry(editor,width=30)
    father_name_editor.grid(row=4,column=1,padx=20)

    address_editor=Entry(editor,width=30)
    address_editor.grid(row=5,column=1,padx=20)

    city_editor=Entry(editor,width=30)
    city_editor.grid(row=6,column=1,padx=20)

    zipcode_editor=Entry(editor,width=30)
    zipcode_editor.grid(row=7,column=1,padx=20)

    #the data to be updated are recorded in 
    # respective attribute noted by index numbers in  database
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        age_editor.insert(0,record[2])
        password_editor.insert(0,record[3])
        father_name_editor.insert(0,record[4])
        address_editor.insert(0,record[5])
        city_editor.insert(0,record[6])
        zipcode_editor.insert(0,record[7])

    #update button for the update dialog box
    edit_btn=Button(editor,text="Update",bg='#046307',fg='white',command=update)
    edit_btn.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

# Create text entries
f_name=Entry(root,width=30,bg='white')
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

age=Entry(root,width=30)
age.grid(row=2,column=1)

password=Entry(root,width=30,show="*")
password.grid(row=3,column=1)

father_name=Entry(root,width=30)
father_name.grid(row=4,column=1)

address=Entry(root,width=30)
address.grid(row=5,column=1)

city=Entry(root,width=30)
city.grid(row=6,column=1)

zipcode=Entry(root,width=30)
zipcode.grid(row=7,column=1)

delete_box=Entry(root,width=30,bg='grey',fg='white')
delete_box.grid(row=11,column=1,pady=5)

# Create textbox labels
f_name_label=Label(root,text="First Name",width=25, anchor="w",bg='#C04000',fg='white')
f_name_label.grid(row=0,column=0,padx=20)

l_name_label=Label(root,text="Last Name",width=25, anchor="w",bg='#C04000',fg='white')
l_name_label.grid(row=1,column=0)

age_label=Label(root,text="Age",width=25, anchor="w",bg='#C04000',fg='white')
age_label.grid(row=2,column=0)

password_label=Label(root,text="Password",width=25, anchor="w",bg='#C04000',fg='white')
password_label.grid(row=3,column=0)

father_name_label=Label(root,text="Father Name",width=25, anchor="w",bg='#C04000',fg='white')
father_name_label.grid(row=4,column=0)

address_label=Label(root,text="Address",width=25, anchor="w",bg='#C04000',fg='white')
address_label.grid(row=5,column=0)

city_label=Label(root,text="City",width=25, anchor="w",bg='#C04000',fg='white')
city_label.grid(row=6,column=0)

zipcode_label=Label(root,text="zipcode",width=25, anchor="w",bg='#C04000',fg='white')
zipcode_label.grid(row=7,column=0)

delete_box_label=Label(root,text="Select ID to delete / update",width=25, anchor="w",bg="red",fg='black')
delete_box_label.grid(row=11,column=0,pady=5)

# Create submit button    
submit_btn=Button(root,text="Submit",bg='#046307',fg='white',command=submit)
submit_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=120)

# Create query button
query_btn=Button(root,text="Query",bg='#046307',fg='white',command=query)
query_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=120)

# Create delete button
delete_box_btn=Button(root,text="Delete",bg='red',command=delete)
delete_box_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=120)

# Create update button
edit_box_btn=Button(root,text="Update",bg='#046307',fg='white',command=edit)
edit_box_btn.grid(row=13,column=0,columnspan=2,pady=10,padx=10,ipadx=120)

# commit change
conn.commit()

# # close connection
conn.close()

#running the project till it is closed
mainloop()
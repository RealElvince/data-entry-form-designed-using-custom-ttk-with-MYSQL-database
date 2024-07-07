# import tkinter and customtkinter
import tkinter

import customtkinter
import mysql.connector
from tkinter import messagebox


def storeInfo():
    # create a connection
    mydb = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
    employee_name = employNameEntry.get()
    gender = genderVar.get()
    if gender == 1:
        gender = "Male"
    elif gender == 0:
        gender ="Female"
    else:
        gender = None
    employee_contact = contactEntry.get()
    employee_department = departOption.get()
    employee_designation = designationEntry.get()
    employee_salary = salaryEntry.get()
    if employee_name and gender and employee_contact and employee_department and employee_designation and employee_salary:

        insert_query = "INSERT INTO manhattan.employees VALUES('{}','{}','{}','{}','{}','{}')".format(employee_name,
                                                                                                      gender,
                                                                                                      employee_contact,
                                                                                                      employee_department,
                                                                                                      employee_designation,
                                                                                                      employee_salary)
        myCursor = mydb.cursor()
        myCursor.execute(insert_query)
        mydb.commit()

        mydb.close()

        # Clear the entry fields after successful submission
        employNameEntry.delete(0, customtkinter.END)
        genderVar.set(-1)
        contactEntry.delete(0, customtkinter.END)
        departOption.set("")
        salaryEntry.delete(0, customtkinter.END)
        designationEntry.delete(0, customtkinter.END)
    else:
        error_message = "The following fields are required and cannot be empty:\n"
        if not employee_name:
            error_message += "-Employee Name\n"
        if gender is not None:
            error_message += "Please select a valid gender\n"

        if not employee_contact:
            error_message += "-Employee Contact\n"
        if not employee_department:
            error_message += "-Employee Department\n"
        if not employee_designation:
            error_message += "-Employee Designation\n"
        if not employee_salary:
            error_message += "-Employee Salary\n"
        tkinter.messagebox.showwarning(title="Error!", message=error_message)


# layout set up
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

# create app window
app = customtkinter.CTk()
app.geometry("600x480")
app.title("Employee Management System")

# define placement variable
placement = 60
# company label
companyName = customtkinter.CTkLabel(master=app, text="Manhattan Moi Avenue INC")
companyName.configure(font=("ariel", 40))
companyName.place(x=200, y=5)

# Employee label
employeeName = customtkinter.CTkLabel(master=app, text="Employee Name")
employeeName.configure(font=("ariel", 20))
employeeName.place(x=20, y=placement + 40)
employNameEntry = customtkinter.CTkEntry(master=app)
employNameEntry.place(x=200, y=placement + 40)

# Gender Label
genderVar = customtkinter.IntVar()
employeeGender = customtkinter.CTkLabel(master=app, text="Gender")
employeeGender.configure(font=("ariel", 20))
employeeGender.place(x=20, y=placement + 80)
Male = customtkinter.CTkRadioButton(master=app, text="Male", variable=genderVar, value=1)
Male.place(x=200, y=placement + 80)
Female = customtkinter.CTkRadioButton(master=app, text="Female", variable=genderVar, value=0)
Female.place(x=300, y=placement + 80)

# Contact Label
employeeContact = customtkinter.CTkLabel(master=app, text="Contact")
employeeContact.configure(font=("ariel", 20))
employeeContact.place(x=20, y=placement + 120)
contactEntry = customtkinter.CTkEntry(master=app)
contactEntry.place(x=200, y=placement + 120)

# Department Label
employeeDepart = customtkinter.CTkLabel(master=app, text="Department")
employeeDepart.configure(font=("ariel", 20))
employeeDepart.place(x=20, y=placement + 160)

# option list
departList = ["", "HR", "Sales", "ICT", "Procurement", "Software Development"]
departOption = customtkinter.CTkOptionMenu(master=app, values=departList)
departOption.place(x=200, y=placement + 160)

# Designation Label
employeeRole = customtkinter.CTkLabel(master=app, text="Designation")
employeeRole.configure(font=("ariel", 20))
employeeRole.place(x=20, y=placement + 240)
designationEntry = customtkinter.CTkEntry(master=app)
designationEntry.place(x=200, y=placement + 240)

# Salary Label
employeeSalary = customtkinter.CTkLabel(master=app, text="Salary")
employeeSalary.configure(font=("ariel", 20))
employeeSalary.place(x=20, y=placement + 280)
salaryEntry = customtkinter.CTkEntry(master=app)
salaryEntry.place(x=200, y=placement + 280)

submit_btn = customtkinter.CTkButton(master=app, text="Submit info", command=storeInfo)
submit_btn.place(x=200, y=420)

app.mainloop()

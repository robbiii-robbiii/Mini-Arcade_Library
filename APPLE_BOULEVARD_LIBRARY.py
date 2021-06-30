# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:48:07 2020

@author: Robbins Aby
"""
#SQL_CONNECTION() SETS A BRIDGE BETWEEN FRONT END AND BACK END.
def sql_connection():
    try:
        con = sq3.connect('Apple_Boulevard_Library.db')
        return con
    except Error:
        print(Error)
#USER_ACC_TABLE() CREATES A TABLE OF YOUR FAVOUR WITH PROPER SQLITE3 QUERY.
def user_acc_table(con):
    cursorObj.execute("CREATE TABLE IF NOT EXISTS User_Accounts(EMAILID text,PHONE_NUMBER text,FIRST_NAME text,LAST_NAME text,PASSWORD text,SECURITY_QUESTION text,SECURITY_ANSWER text,AUTHENTICATION integer,PRIMARY KEY (EMAILID,PHONE_NUMBER))")
    con.commit()
#USER_ACC_INSERT() LETS YOU INSERT DATA INTO THE RESEPCTIVE TABLE.
def user_acc_insert(con,info):
    cursorObj.execute("INSERT INTO User_Accounts(EMAILID,PHONE_NUMBER,FIRST_NAME,LAST_NAME,PASSWORD,SECURITY_QUESTION,SECURITY_ANSWER,AUTHENTICATION) VALUES(?,?,?,?,?,?,?,?)",info)
    con.commit()
#RESET() IS USED TO DELETE FRAMES ON A WINDOW.
def reset(frame):
    frame.destroy()
#STU_HOME LETS YOU INTO A WINDOW WHICH DISPLAYS YOU ACCOUNT INFO UPON SUCCESSFUL SIGN-IN.
def stu_home(siframe,username,si_reset):
    
    def ho_back(opframe):
        reset(opframe)
        ho_home()
    
    def ho_acc_info(hoframe):
        reset(hoframe)
        root.geometry('500x300')
        root.configure(bg="White")
        accinfoframe = tk.Frame(root)
        accinfoframe.pack()
        temp7 = (username,username)
        cursorObj.execute('SELECT FIRST_NAME,LAST_NAME,EMAILID,PHONE_NUMBER,SECURITY_QUESTION,SECURITY_ANSWER FROM User_Accounts WHERE EMAILID = ? OR PHONE_NUMBER = ?',temp7)
        data = cursorObj.fetchall()
        for row in data:
            first_name,last_name,emailid,pho_number,security_question,security_answer = row[0],row[1],row[2],row[3],row[4],row[5]
            name = first_name+" "+last_name
        
        accinfot = tk.Label(accinfoframe,text = "ACCOUNT DETAILS\n",font = "Arial 14 italic bold underline").grid(row=0,columnspan=2,pady=5)
        accinfoname = tk.Label(accinfoframe,text = "Name",font="Arial 10 bold").grid(row=3,column=0,padx=10,sticky='W')
        accinfoname1 = tk.Label(accinfoframe,text = name,font="Arial 10").grid(row=3,column=1,padx=10,sticky='W')
        accinfoemail = tk.Label(accinfoframe,text = "Email-Id",font="Arial 10 bold").grid(row=4,column=0,padx=10,sticky='W')
        accinfoemail1 = tk.Label(accinfoframe,text = emailid,font="Arial 10").grid(row=4,column=1,padx=10,sticky='W')
        accinfophonum = tk.Label(accinfoframe,text = "Phone Number",font="Arial 10 bold").grid(row=5,column=0,padx=10,sticky='W')
        accinfophonum1 = tk.Label(accinfoframe,text = pho_number,font="Arial 10").grid(row=5,column=1,padx=10,sticky='W')
        accinfoscrtyqst = tk.Label(accinfoframe,text = "Security Question",font="Arial 10 bold").grid(row=6,column=0,padx=10,sticky='W')
        accinfoscrtyqst1 = tk.Label(accinfoframe,text = security_question,font="Arial 10").grid(row=6,column=1,padx=10,sticky='W')
        accinfonscrtyans = tk.Label(accinfoframe,text = "Security Answer",font="Arial 10 bold").grid(row=7,column=0,padx=10,sticky='W')
        accinfonscrtyans1 = tk.Label(accinfoframe,text = security_answer,font="Arial 10").grid(row=7,column=1,padx=10,sticky='W')
        accinfobtn1 = tk.Button(accinfoframe,text = "DONE",bg = "Blue",fg = "White",font="Arial 10 bold",command = lambda: ho_back(accinfoframe)).grid(row=8,columnspan=2,pady=20)

    def ho_calculator(hoframe):
        global expression
        
        def set_expression(num):
            global expression
            expression = expression+str(num)
            value.set(expression)
        
        def calculator():
            try:
                global expression
                answer = str(eval(expression))
                value.set(answer)
                expression = answer
            except:
                value.set("Enter correct expression")
                expression = ""
        
        def clear():
            global expression
            expression = ""
            value.set(expression)
            value.set("0")
        
        def cal_exit():
            global expression
            expression = ""
            value.set(expression)
            ho_back(calframe)
            
        reset(hoframe)
        root.geometry('600x650')
        root.configure(bg="White")
        calframe = tk.Frame(root)
        calframe.pack()
        value = tk.StringVar(value="0")
        expression = ""
        calt = tk.Label(calframe,text = "REGULAR CALCULATOR\n",font = "Arial 14 italic bold underline").grid(row=0,columnspan=4,pady=5)
        calval = tk.Entry(calframe,textvariable = value,font = "Verdana 15",bg="Black",fg="White",justify="right").grid(row=1,column=0,columnspan=4,ipadx=53,ipady=5)
        
        calbtn1 = tk.Button(calframe,text = "AC",bg="Grey",fg="Black",font = "Verdana 15",command = clear,height=3,width=21).grid(row=2,column=0,columnspan=3)
        calbtn2 = tk.Button(calframe,text="7",fg="Black",font = "Verdana 15",command=lambda: set_expression("7"),height=3,width=6).grid(row=3,column=0)
        calbtn3 = tk.Button(calframe,text="4",fg="Black",font = "Verdana 15",command=lambda: set_expression("4"),height=3,width=6).grid(row=4,column=0)
        calbtn4 = tk.Button(calframe,text="1",fg="Black",font = "Verdana 15",command=lambda: set_expression("1"),height=3,width=6).grid(row=5,column=0)
        calbtn5 = tk.Button(calframe,text="0",fg="Black",font = "Verdana 15",command=lambda: set_expression("0"),height=3,width=14).grid(row=6,column=0,columnspan=2)
        calbtn6 = tk.Button(calframe,text="8",fg="Black",font = "Verdana 15",command=lambda: set_expression("8"),height=3,width=6).grid(row=3,column=1)
        calbtn7 = tk.Button(calframe,text="5",fg="Black",font = "Verdana 15",command=lambda: set_expression("5"),height=3,width=6).grid(row=4,column=1)
        calbtn8 = tk.Button(calframe,text="2",fg="Black",font = "Verdana 15",command=lambda: set_expression("2"),height=3,width=6).grid(row=5,column=1)
        calbtn9 = tk.Button(calframe,text="9",fg="Black",font = "Verdana 15",command=lambda: set_expression("9"),height=3,width=6).grid(row=3,column=2)
        calbtn10 = tk.Button(calframe,text="6",fg="Black",font = "Verdana 15",command=lambda: set_expression("6"),height=3,width=6).grid(row=4,column=2)
        calbtn11 = tk.Button(calframe,text="3",fg="Black",font = "Verdana 15",command=lambda: set_expression("3"),height=3,width=6).grid(row=5,column=2)
        calbtn12 = tk.Button(calframe,text=".",fg="Black",font = "Verdana 15",command=lambda: set_expression("."),height=3,width=6).grid(row=6,column=2)
        calbtn13 = tk.Button(calframe,text="/",bg="Orange",fg="White",font = "Verdana 15",command=lambda: set_expression("/"),height=3,width=6).grid(row=2,column=3)
        calbtn14 = tk.Button(calframe,text="X",bg="Orange",fg="White",font = "Verdana 15",command=lambda: set_expression("*"),height=3,width=6).grid(row=3,column=3)
        calbtn15 = tk.Button(calframe,text="-",bg="Orange",fg="White",font = "Verdana 15",command=lambda: set_expression("-"),height=3,width=6).grid(row=4,column=3)
        calbtn16 = tk.Button(calframe,text="+",bg="Orange",fg="White",font = "Verdana 15",command=lambda: set_expression("+"),height=3,width=6).grid(row=5,column=3)
        calbtn17 = tk.Button(calframe,text="=",bg="Orange",fg="White",font = "Verdana 15",command=calculator,height=3,width=6).grid(row=6,column=3)
        calbtn18 = tk.Button(calframe,text = "DONE",bg = "Blue",fg = "White",font = "Arial 10 bold",command = lambda: cal_exit()).grid(row=7,columnspan=4,pady=20)
    
    def ho_covid19(hoframe):
        reset(hoframe)
        root.geometry('400x250')
        root.configure(bg="White")
        covframe = tk.Frame(root)
        covframe.pack()
        corona = COVID19Py.COVID19()
        latest = corona.getLatest()
        for i in latest:
            if i == 'confirmed':
                confirmed = str(latest[i])
            elif i == 'deaths':
                deaths = str(latest[i])
            else:pass
        
        covt = tk.Label(covframe,text = "COVID-19 UPDATES",font = "Arial 14 italic bold underline").grid(row=0,columnspan=2,pady=5)
        covt1 = tk.Label(covframe,text = "LATEST NEWS\n",font = "Arial 11 bold underline").grid(row=1,columnspan=2,pady=5)
        covcon = tk.Label(covframe,text = "Total Number of Confirmed Cases",font="Arial 10 bold").grid(row=2,column=0,padx=10,sticky='W')
        covcon1 = tk.Label(covframe,text = confirmed,fg="Grey",font = "Verdana 15 bold").grid(row=2,column=1,padx=10,sticky='W')
        covdea = tk.Label(covframe,text = "Total Number of Death Cases",font="Arial 10 bold").grid(row=3,column=0,padx=10,sticky='W')
        covdea1 = tk.Label(covframe,text = deaths,fg="Red",font = "Verdana 15 bold").grid(row=3,column=1,padx=10,sticky='W')
        covbtn1 = tk.Button(covframe,text = "DONE",bg = "Blue",fg = "White",font = "Arial 10 bold",command = lambda: ho_back(covframe)).grid(row=4,columnspan=2,pady=20)
      
    def ho_flashgame(hoframe):
        global tot_chance
        global temp
        global you_point
        global comp_point
        global null
        temp = tot_chance
        you_point = null
        comp_point = null
        
        def fg_flush(num):
            global tot_chance
            global temp
            global you_point
            global comp_point
            global null
            temp = tot_chance
            you_point = null
            comp_point = null
            fgl4.config(text=you_point)
            fgl6.config(text=comp_point)
            
            if num == 0:
                pass
            else:
                ho_back(fgframe)
            return 1 
        
        def stay_or_exit():
            if tk.messagebox.askyesno("Flash Game","Would you like to play again?"):
                return True
            else:
                return False
        
        def get_results(you,comp):
            if you > comp:
                tk.messagebox.showinfo("Game Results","Congratulations, You won playing against computer.\nYou Scored : "+str(you)+"\nComputer Scored : "+str(comp))
            elif you == comp:
                tk.messagebox.showinfo("Game Results","The game was draw.\nYou Scored : "+str(you)+"\nComputer Scored : "+str(comp))
            else:
                tk.messagebox.showinfo("Game Results","Oops, You lost playing against computer.\nYou Scored : "+str(you)+"\nComputer Scored : "+str(comp))
        
        def get_winner(call):
            global temp
            global you_point
            global comp_point
            
            if ((you_point==0) and (comp_point==0)):
                you = 0
                comp = 0
            else:
                you = you_point
                comp = comp_point
            
            if random.random()<=(1/3):
                throw = "rock"
            elif (1/3)<random.random()<=(2/3):
                throw = "scissors"
            else:
                throw = "paper"
            
            if (throw=="rock" and call=="paper") or (throw=="paper" and call=="scissors") or (throw=="scissors" and call=="rock"):
                result = "You won!"
                you += 1
            elif throw == call:
                result = "It's a draw"
            else:
                result = "You lost!"
                comp += 1
            
            fgl2.config(text="Computer threw : "+throw+"\n"+result)
            fgl4.config(text=you)
            fgl6.config(text=comp)
            temp -= 1
            if temp == 0:
                you_point = 0
                comp_point = 0
                get_results(you,comp)
                if not stay_or_exit():
                    fg_flush(0)
                    ho_back(fgframe)
                else:
                    fg_flush(0)
            else:
                you_point = you
                comp_point = comp
        
        reset(hoframe)
        root.geometry('550x350')
        root.configure(bg="White")
        fgframe = tk.Frame(root)
        fgframe.pack()
        
        fgt = tk.Label(fgframe,text = "ROCK/PAPER/SCISSORS\nGAME\n",font = "Arial 14 italic bold underline").grid(row=0,columnspan=3,pady=5)
        fgbtn1 = tk.Button(fgframe,text="ROCK",bg="#80ff80",padx=10,command = lambda: get_winner("rock"),width=20).grid(row=1,column=0,pady=5)
        fgbtn2 = tk.Button(fgframe,text="PAPER",bg="#3399ff",padx=10,command = lambda: get_winner("paper"),width=20).grid(row=1,column=1,pady=5)
        fgbtn3 = tk.Button(fgframe,text="SCISSORS",bg="#ff9999",padx=10,command = lambda: get_winner("scissors"),width=20).grid(row=1,column=2,pady=5)
        fgl1 = tk.Label(fgframe,text="Game Stats",font="Arial 10 bold").grid(row=2,column=0,pady=5,sticky="w")
        fgl2 = tk.Label(fgframe,fg="red",bg="Grey",text="Start Game!!!",font="Arial 10 bold")
        fgl2.grid(row=2,column=1,columnspan=2,pady=5)
        fgl3 = tk.Label(fgframe,text="Total Points Gained by You",font="Arial 10 bold").grid(row=3,column=0,columnspan=2,pady=5,sticky="w")
        fgl4 = tk.Label(fgframe,text="0",bg="Grey",fg="Orange",font="Arial 10 bold")
        fgl4.grid(row=3,column=1,columnspan=2,pady=5)
        fgl5 = tk.Label(fgframe,text="Total Points Gained by Computer",font="Arial 10 bold").grid(row=4,column=0,columnspan=2,pady=5,sticky="w")
        fgl6 = tk.Label(fgframe,text="0",bg="Grey",fg="Orange",font="Arial 10 bold")
        fgl6.grid(row=4,column=1,columnspan=2,pady=5)
        fgbtn4 = tk.Button(fgframe,text = "DONE",bg = "Blue",fg = "White",font = "Arial 10 bold",command = lambda: fg_flush(1)).grid(row=5,columnspan=3,pady=20)
        
    #HO_DELETE() LETS YOU DELETE YOUR ACCOUNT.
    def ho_delete(hoframe):
        temp7 = (username,username)
        if tk.messagebox.askyesno("Account Deletion Confirmation","Are you sure you want to delete your account?\nYour entire data will be erased on deleting of your account."):
            cursorObj.execute('DELETE FROM User_Accounts WHERE EMAILID = ? OR PHONE_NUMBER = ?',temp7)
            con.commit()
            tk.messagebox.showinfo("Account Deletion Successful","You have successfully deleted your account.\nKindly sign-up if you would like to join us back.")
            root.configure(bg="White")
            reset(hoframe)
            stu_signin()
        else:
            pass
    #HO_SIGNOUT() LETS YOU SIGN-OUT OF YOUR ACCOUNT.
    def ho_signout(hoframe):
        tk.messagebox.showinfo("Sign-Out Successful","You have successfully signed out.\nHave a wonderful day.")
        root.configure(bg="White")
        reset(hoframe)
        stu_signin()
    
    def ho_home():
        root.geometry('500x450')
        root.configure(bg="Black")
        hoframe = tk.Frame(root)
        hoframe.pack()
        hoframe.configure(bg="Black")
        hot = tk.Label(hoframe,text = "APPLE BOULEVARD LIBRARY\nARCADE",fg="White",bg="Black",font = "Arial 14 italic bold underline").grid(row=0,columnspan=2,pady=5)
        hobtn1 = tk.Button(hoframe,text = "ACCOUNT INFO",bg = "Orange",fg = "Black",font = "Arial 10 bold",command = lambda: ho_acc_info(hoframe),height="4",width="15").grid(row=1,column=0,pady=20)
        hobtn2 = tk.Button(hoframe,text = "CALCULATOR",bg = "Orange",fg = "Black",font = "Arial 10 bold",command = lambda: ho_calculator(hoframe),height="4",width="15").grid(row=1,column=1,pady=20)
        hobtn3 = tk.Button(hoframe,text = "COVID-19 UPDATES",bg = "Orange",fg = "Black",font = "Arial 10 bold",command = lambda: ho_covid19(hoframe),height="4",width="15").grid(row=2,column=0,pady=20)
        hobtn4 = tk.Button(hoframe,text = "FLASH GAME",bg = "Orange",fg = "Black",font = "Arial 10 bold",command = lambda: ho_flashgame(hoframe),height="4",width="15").grid(row=2,column=1,pady=20)
        hobtn5 = tk.Button(hoframe,text = "DELETE ACCOUNT",bg = "Red",fg = "White",font = "Arial 10 bold",command = lambda: ho_delete(hoframe),height="4",width="15").grid(row=3,column=0,pady=20)
        hobtn6 = tk.Button(hoframe,text = "SIGN OUT",bg = "Blue",fg = "White",font = "Arial 10 bold",command = lambda: ho_signout(hoframe),height="4",width="15").grid(row=3,column=1,pady=20)
    #HOME WINDOW DESIGN.
    reset(siframe)
    ho_home()
#STU_SIGNIN() LETS YOU SIGN-IN UPON SUCCESSFUL VERIFICATION.
def stu_signin():
    #SI_RESET() CLEARS DATA IN THE INPUT WIDGETS.
    def si_reset():
        siusername1.delete(0,"end")
        sipassword1.delete(0,"end")
    #SI_VERIFY() AUTHENTICATES THE DETAILS WITH THE BACK END.
    def si_verify():
        temp5 = (siusrnme.get(),siusrnme.get())
        cursorObj.execute('SELECT AUTHENTICATION FROM User_Accounts WHERE EMAILID = ? OR PHONE_NUMBER = ?',temp5)
        auth_number = cursorObj.fetchall()
        for row in auth_number:
            si_authen_flag = row[0]
        
        if si_authen_flag==3:
            tk.messagebox.showerror("Sign-In Errorr","Staff assistance required for manual override.\nIt seems like your account is blocked from signing in.")
            si_reset()
        if not si_authen_flag==3:
            temp6 = (siusrnme.get(),siusrnme.get())
            cursorObj.execute('SELECT PASSWORD FROM User_Accounts WHERE EMAILID = ? OR PHONE_NUMBER = ?',temp6)
            row_pass = cursorObj.fetchall()
            for row in row_pass:
                password = row[0]
            
            if sipass.get()==password:
                stu_home(siframe,siusrnme.get(),si_reset())
            else:
                tk.messagebox.showerror("Authentication Error","You have failed to authenticate your identity inorder to sign-in to your account.\nKindly try again with correct credentials or reset your password.")
                sipassword1.delete(0,"end")        
    #SI_VALIDATION VALIDATES THE DATA INPUTTED.
    def si_validation():
        validity = True
        #ACCOUNT_VALIDATION() CHECKS IF THE USER ACCOUNT DO EXIST IN THE DATABASE.
        def account_validation(con):
            cursorObj.execute('SELECT EMAILID,PHONE_NUMBER FROM User_Accounts')
            rows = cursorObj.fetchall()
            flag=0
            for row in rows:
                eid,pn = row[0],row[1]
                if (siusrnme.get()==eid or siusrnme.get()==pn):
                    flag=0
                    break
                else:
                    flag=1
                    continue
            if flag==1:
                return False
            else:
                return True
        #OTHER_ENTRIES_VALIDATION() CHECKS IF ALL THE DATA INPUT WIDGETS ARE NOT EMPTY.
        def other_entries_validation():
            if (len(siusrnme.get())==0 or len(sipass.get())==0):
                return False
            else:
                return True
        #RUNNING VALIDATION COURSE.
        if other_entries_validation():
            if account_validation(con):
                validity = True
            else:
                tk.messagebox.showerror("Validation Error","Invalid Emailid/Phone No.\nKindly sign-up if you are a new user.")
                si_reset()                                        
                validity = False
        else:
            tk.messagebox.showerror("Validation Error","Invalid Entries\nFill the sign-in page completely.")
            validity = False
        #NEXT STEP TO BE FOLLOWED UPON SUCCESSFUL VALIDATION.
        if validity:
            si_verify()
    #SIGN-IN WINDOW DESIGN.
    root.geometry('350x350')
    siframe = tk.Frame(root)
    siframe.pack()
    sit = tk.Label(siframe,text = "APPLE BOULEVARD LIBRARY",font = "Arial 14 italic bold underline").grid(row=0,columnspan=2,pady=5)
    sit = tk.Label(siframe,text = "SIGN-IN",font = "Arial 11 bold underline").grid(row=1,columnspan=2,pady=15)
    siusername = tk.Label(siframe,text = "Email/Phone No.").grid(row=2,column=0,padx=10)
    siusername1 = tk.Entry(siframe,textvariable = siusrnme)
    siusername1.grid(row=2,column=1)
    sipassword = tk.Label(siframe,text = "Password").grid(row=3,column=0,padx=10,pady=10)
    sipassword1 = tk.Entry(siframe,textvariable = sipass,show = "*")
    sipassword1.grid(row=3,column=1)
    sibtn1 = tk.Button(siframe,text = "RESET",bg = "Red",fg = "Black",relief = "sunken",command = lambda: si_reset()).grid(row=4,column=0,pady=20)
    sibtn2 = tk.Button(siframe,text = "SIGN IN",bg = "Blue",fg = "White",command = lambda: si_validation()).grid(row=4,column=1,pady=20)
    sibtn3 = tk.Button(siframe,text = "Forgot Password?",relief = "flat",fg = "Blue",font = "Arial 9 underline",command = lambda: stu_forgotpass(siframe)).grid(row=5,columnspan=2)
    sibtn4 = tk.Button(siframe,text = "New Member? Sign-Up",relief = "flat",fg = "Blue",font = "Arial 9 underline",command = lambda: stu_signup(siframe)).grid(row=6,columnspan=2)
#STU_SIGNUP() IS USED TO CREATE A NEW ACCOUNT FOR A NEW USER TO JOIN.
def stu_signup(siframe):
    #ADD_DATA() IS USED TO DATA INTO DATABASE UPON SUCCESSFUL VALIDATION PROCEDURE.
    def add_data():
        info = (suemlid.get(),suphno.get(),sufstnme.get(),sulstnme.get(),suconpass.get(),suscrtyqst.get(),suscrtyans.get(),0)
        user_acc_insert(con,info)
        tk.messagebox.showinfo("Sign-Up Successful","You have successfully signed up.\nKindly sign-in with your credentials.")
    #SU_BACK() LETS YOU GO BACK TO YOUR OLD WINDOW.
    def su_back():
        su_reset()
        reset(suframe)
        stu_signin()
    #SU_RESET() CLEARS ALL DATA IN THE INPUT WIDGETS.
    def su_reset():
        sufirstname1.delete(0,"end")
        sulastname1.delete(0,"end")
        suemailid1.delete(0,"end")
        suphonenumber1.delete(0,"end")
        supassword1.delete(0,"end")
        suconfirmpassword1.delete(0,"end")
        suscrtyqst.set('')
        susecurityquestion2.delete(0,"end")
    #SU_VALIDATION() IS USED TO PERFORM VALIDATION COURSE FOR THE INPUT DATA.
    def su_validation():
        validity = True
        #OTHER_ENTRIES_VALIDATION() CHECKS IF ALL THE DATA INPUT WIDGETS ARE NOT EMPTY.
        def other_entries_validation():
            if (len(sufstnme.get())==0 or len(sulstnme.get())==0 or len(suemlid.get())==0 or len(suphno.get())==0 or len(supass.get())==0 or len(suconpass.get())==0 or len(suscrtyqst.get())==0 or len(suscrtyans.get())==0):
                return False
            else:
                return True
        #EMAILID_VALIDATION() CHECKS IF THE EMAILID ENTERED IS VALID.
        def emailid_validation():
            emailid_format = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
            if re.match(emailid_format,suemlid.get()):
                return True
            else:
                return False
        #PHNO_VALIDATION() CHECKS IF THE ENTERED PHONE NUMBER IS VALID.
        def phno_validation():
            phno_format = '\d{10}'
            if re.match(phno_format,suphno.get()):
                return True
            else:
                return False
        #PASS_VALIDATION() CHECKS IF USER INPUTS A GENUINE PASSWORD.
        def pass_validation():
            if not len(supass.get())>=8:
                return False
            elif not re.search("[a-z]",supass.get()):
                return False
            elif not re.search("[A-Z]",supass.get()):
                return False
            elif not re.search("[0-9]",supass.get()):
                return False
            elif not re.search("[!@#$%^&*-+|]",supass.get()):
                return False
            elif re.search("\s",supass.get()):
                return False
            else:
                return True
        #PASS_MATCH_VALIDATION() CHECKS IF THE CONFIRMED PASSWORD IS EQIVALENT TO THE ORIGINAL PASSWORD.
        def pass_match_validation():
            if supass.get() == suconpass.get():
                return True
            else:
                return False
        #ACCOUNT_VALIDATION() CHECKS IF THE USER ACCOUNT DO EXIST IN THE DATABASE.
        def account_validation(con):
            cursorObj.execute('SELECT EMAILID,PHONE_NUMBER FROM User_Accounts')
            rows = cursorObj.fetchall()
            flag=0
            for row in rows:
                eid,pn = row[0],row[1]
                if (suemlid.get()==eid or suphno.get()==pn):
                    flag=1
                    break
                else:
                    continue
            if flag == 1:
                return False
            else:
                return True
        #RUNNING VALIDATION COURSE.
        if other_entries_validation():
            if emailid_validation():
                if phno_validation():
                    if pass_validation():
                        if pass_match_validation():
                            if account_validation(con):
                                validity = True
                            else:
                                tk.messagebox.showerror("Validation Error","Failed to Sign-Up\nAccount already exists.")
                                su_reset()
                                validity = False
                        else:
                            tk.messagebox.showerror("Validation Error","Password Confirmation Failed\nRe-Enter the password correctly.")
                            suconfirmpassword1.delete(0,"end")
                            validity = False
                    else:
                        tk.messagebox.showerror("Validation Error","1.Password should contain a minimum of 8 characters.\n2.Password should have atleast one lowercase and uppercase letter.\n3.Password should have atleast one digit and special character.\n4.Password shouldn't have any spaces in between.")
                        supassword1.delete(0,"end")
                        suconfirmpassword1.delete(0,"end")
                        validity = False
                else:
                    tk.messagebox.showerror("Validation Error","Invalid Phone Number!!!\nEnter 10 digit phone number.")
                    suphonenumber1.delete(0,"end")
                    validity = False
            else:
                tk.messagebox.showerror("Validation Error","Invalid Email-Id\nEnter email-id of the form example@.com.")
                suemailid1.delete(0,"end")
                validity = False
        else:
            tk.messagebox.showerror("Validation Error","Invalid Entries\nFill the sign-up page completely.")
            validity = False
        #NEXT STEP TO BE FOLLOWED UPON SUCCESSFUL VALIDATION.
        if validity:
            add_data()
            su_reset()
            reset(suframe)
            stu_signin()
    #SIGN-UP WINDOW DESIGN.
    reset(siframe)
    root.geometry('700x450')
    suframe = tk.Frame(root)
    suframe.pack()
    sut = tk.Label(suframe,text = "SIGN-UP",font = "Arial 11 bold underline").grid(row=0,columnspan=2,pady=10)
    sufirstname = tk.Label(suframe,text = "First Name").grid(row=1,column=0,padx=60,sticky='W')
    sufirstname1 = tk.Entry(suframe,textvariable = sufstnme)
    sufirstname1.grid(row=1,column=1)
    sulastname = tk.Label(suframe,text = "Last Name").grid(row=2,column=0,padx=60,pady=10,sticky='W')
    sulastname1 = tk.Entry(suframe,textvariable = sulstnme)
    sulastname1.grid(row=2,column=1)
    suemailid = tk.Label(suframe,text = "E-mail").grid(row=3,column=0,padx=60,sticky='W')
    suemailid1 = tk.Entry(suframe,textvariable = suemlid)
    suemailid1.grid(row=3,column=1)
    suphonenumber = tk.Label(suframe,text = "Phone Number").grid(row=4,column=0,padx=60,pady=10,sticky='W')
    suphonenumber1 = tk.Entry(suframe,textvariable = suphno)
    suphonenumber1.grid(row=4,column=1)
    supassword = tk.Label(suframe,text = "Password").grid(row=5,column=0,padx=60,sticky='W')
    supassword1 = tk.Entry(suframe,textvariable = supass)
    supassword1.grid(row=5,column=1)
    suconfirmpassword = tk.Label(suframe,text = "Confirm Password").grid(row=6,column=0,padx=60,pady=10,sticky='W')
    suconfirmpassword1 = tk.Entry(suframe,textvariable = suconpass)
    suconfirmpassword1.grid(row=6,column=1)
    susecurityquestion = tk.Label(suframe,text = "Security Question").grid(row=7,rowspan=2,column=0,padx=60,sticky='W')
    susecurityquestion1 = tk.OptionMenu(suframe,suscrtyqst,"What was the last name of your third-grade teacher?","What was the name of your second pet?","What was your first phone number?","What was the name of your first teacher?","What was the name of your first crush?")
    susecurityquestion1.grid(row=7,column=1,sticky='W')
    susecurityquestion2 = tk.Entry(suframe,textvariable = suscrtyans)
    susecurityquestion2.grid(row=8,column=1,pady=5)
    subtn1 = tk.Button(suframe,text = "BACK",bg = "Green",fg = "White",relief = "sunken",command = lambda: su_back()).grid(row=9,column=0,pady=10)
    subtn2 = tk.Button(suframe,text = "RESET",bg = "Red",fg = "Black",relief = "sunken",command = lambda: su_reset()).grid(row=9,column=1,pady=10)
    subtn3 = tk.Button(suframe,text = "SUBMIT",bg = "Blue",fg = "White",command = lambda: su_validation()).grid(row=10,columnspan=2,pady=5)
#STU_FORGOTPASS() METHOD LETS YOU TO RESET YOUR PASSWORD UPON CERTAIN AUTHENTICATION PROCEDURE.
def stu_forgotpass(siframe):
    #UPDATE_PASS METHOD IS USED TO UPDATE THE PASSWORD ON SUCCESSFUL AUTHENTICATION.
    def update_pass(fp_authen_flag):
        fp_authen_flag=0
        temp3 = (fpconpass.get(),fpidntty.get(),fpidntty.get())
        temp4 = (fp_authen_flag,fpidntty.get(),fpidntty.get())
        cursorObj.execute('UPDATE User_Accounts SET PASSWORD = ? WHERE EMAILID = ? OR PHONE_NUMBER = ?',temp3)
        cursorObj.execute('UPDATE User_Accounts SET AUTHENTICATION = ? WHERE EMAILID = ? OR PHONE_NUMBER = ?',temp4)
        con.commit()
        tk.messagebox.showinfo("Password Change Successful","You have successfully changed your password.\nKindly sign-in with your updated credentials.")
        fp_reset()
        reset(fpframe)
        stu_signin()
    #FP_BACK() IS USED TO GO ONE STEP BACK FROM YOUR CURRENT WINDOW.
    def fp_back():
        fp_reset()
        reset(fpframe)
        stu_signin()
    #FP_RESET IS USED TO RESET ALL THE DATA INPUT WIDGETS.
    def fp_reset():
        fpidentity1.delete(0,"end")
        fppassword1.delete(0,"end")
        fpconfirmpassword1.delete(0,"end")
        fpscrtyqst.set('')
        fpsecurityquestion2.delete(0,"end")
    #FP_VERIFY IS USED TO AUTHENTICATE IF A USER IS ELIGIBLE TO RESET PASSWORD.
    def fp_verify():
        temp = (fpidntty.get(),fpidntty.get())
        cursorObj.execute('SELECT AUTHENTICATION FROM User_Accounts WHERE EMAILID = ? OR PHONE_NUMBER = ?',temp)
        auth_number = cursorObj.fetchall()
        for row in auth_number:
            fp_authen_flag = int(row[0])
        
        temp1 = (fpidntty.get(),fpidntty.get())
        cursorObj.execute('SELECT SECURITY_QUESTION,SECURITY_ANSWER FROM User_Accounts WHERE EMAILID = ? OR PHONE_NUMBER = ?',temp1)
        auth_rows = cursorObj.fetchall()
        for row in auth_rows:
            scrtqst,scrtans = row[0],row[1]
        if fp_authen_flag==3:
            tk.messagebox.showerror("Verification Error","Staff assistance required for manual override.\nYou have failed to verify yourself in all the 3 chances.")
            fp_reset()
        else:
            if (scrtqst==fpscrtyqst.get() and scrtans==fpscrtyans.get()):
                update_pass(fp_authen_flag)
            else:
                fp_authen_flag += 1
                if fp_authen_flag==3:
                    tk.messagebox.showerror("Verification Error","Staff assistance required for manual override.\nYou have failed to verify yourself in all the 3 chances.")
                    temp8 = (fp_authen_flag,fpidntty.get(),fpidntty.get())
                    cursorObj.execute('UPDATE User_Accounts SET AUTHENTICATION = ? WHERE EMAILID = ? OR PHONE_NUMBER = ?',temp8)
                    con.commit()
                    fp_reset()
                if not fp_authen_flag==3:
                    if fp_authen_flag==1:
                        chance=2
                    elif fp_authen_flag==2:
                        chance=1
                    tk.messagebox.showerror("Verification Error","You have failed to authenticate your identity inorder to change the password.\nKindly try again. You have a total of "+str(chance)+" more of chance to verify yourself before you get locked out.")
                    temp2 = (fp_authen_flag,fpidntty.get(),fpidntty.get())
                    cursorObj.execute('UPDATE User_Accounts SET AUTHENTICATION = ? WHERE EMAILID = ? OR PHONE_NUMBER = ?',temp2)
                    con.commit()
                    fpscrtyqst.set('')
                    fpsecurityquestion2.delete(0,"end")
    #FP_VALIDATION() IS USED VALIDATE THE DATA INPUTTED BY THE USER.
    def fp_validation():
        validity = True
        #OTHER_ENTRIES_VALIDATION() CHECKS IF ALL THE DATA INPUT WIDGETS ARE NOT EMPTY.
        def other_entries_validation():
            if (len(fpidntty.get())==0 or len(fppass.get())==0 or len(fpconpass.get())==0 or len(fpscrtyqst.get())==0 or len(fpscrtyans.get())==0):
                return False
            else:
                return True
        #PASS_VALIDATION() CHECKS IF USER INPUTS A GENUINE PASSWORD.
        def pass_validation():
            if not len(fppass.get())>=8:
                return False
            elif not re.search("[a-z]",fppass.get()):
                return False
            elif not re.search("[A-Z]",fppass.get()):
                return False
            elif not re.search("[0-9]",fppass.get()):
                return False
            elif not re.search("[!@#$%^&*-+|]",fppass.get()):
                return False
            elif re.search("\s",fppass.get()):
                return False
            else:
                return True
        #PASS_MATCH_VALIDATION() CHECKS IF THE CONFIRMED PASSWORD IS EQIVALENT TO THE ORIGINAL PASSWORD.
        def pass_match_validation():
            if fppass.get() == fpconpass.get():
                return True
            else:
                return False
        #ACCOUNT_VALIDATION() CHECKS IF THE USER ACCOUNT DO EXIST IN THE DATABASE.
        def account_validation(con):
            cursorObj.execute('SELECT EMAILID,PHONE_NUMBER,SECURITY_QUESTION,SECURITY_ANSWER FROM User_Accounts')
            rows = cursorObj.fetchall()
            flag=0
            for row in rows:
                eid,pn = row[0],row[1]
                if (fpidntty.get()==eid or fpidntty.get()==pn):
                    flag=0
                    break
                else:
                    flag=1
                    continue
            if flag==1:
                return False
            else:
                return True
        #RUNNING THE COMPLETE VALIDATION PROCEDURE.
        if other_entries_validation():
            if pass_validation():
                if pass_match_validation():
                    if account_validation(con):
                        validity = True
                    else:
                        tk.messagebox.showerror("Validation Error","Account Doesn't Exist\nYou are not an existing user. Kindly sign-up inorder to sign-in.")
                        fp_reset()
                        validity = False
                else:
                    tk.messagebox.showerror("Validation Error","Password Confirmation Failed\nRe-Enter the new password correctly.")
                    fpconfirmpassword1.delete(0,"end")
                    validity = False
            else:
                tk.messagebox.showerror("Validation Error","1.Password should contain a minimum of 8 characters.\n2.Password should have atleast one lowercase and uppercase letter.\n3.Password should have atleast one digit and special character.\n4.Password shouldn't have any spaces in between.")
                fppassword1.delete(0,"end")
                fpconfirmpassword1.delete(0,"end")
                validity = False
        else:
            tk.messagebox.showerror("Validation Error","Invalid Entries\nFill the forgot password page completely.")
            validity = False
        #NEXT STEP IF THE VALIDITY IS COMPROMISED.
        if validity:
            fp_verify()
    #DESIGN OF FORGOT PASSWORD WINDOW.
    reset(siframe)
    root.geometry('650x350')
    fpframe = tk.Frame(root)
    fpframe.pack()
    fpt = tk.Label(fpframe,text = "FORGOT PASSWORD",font = "Arial 11 bold underline").grid(row=0,columnspan=2,pady=10)
    fpidentity = tk.Label(fpframe,text = "Email/Phone No.").grid(row=1,column=0,padx=60,sticky='W')
    fpidentity1 = tk.Entry(fpframe,textvariable = fpidntty)
    fpidentity1.grid(row=1,column=1)
    fppassword = tk.Label(fpframe,text = "New Password").grid(row=2,column=0,padx=60,sticky='W')
    fppassword1 = tk.Entry(fpframe,textvariable = fppass)
    fppassword1.grid(row=2,column=1)
    fpconfirmpassword = tk.Label(fpframe,text = "Confirm New Password").grid(row=3,column=0,padx=60,pady=10,sticky='W')
    fpconfirmpassword1 = tk.Entry(fpframe,textvariable = fpconpass)
    fpconfirmpassword1.grid(row=3,column=1)
    fpsecurityquestion = tk.Label(fpframe,text = "Authentication Question").grid(row=4,rowspan=2,column=0,padx=60,sticky='W')
    fpsecurityquestion1 = tk.OptionMenu(fpframe,fpscrtyqst,"What was the name of your third-grade teacher?","What was the name of your second pet?","What was your first phone number?","What was the name of your first teacher?","What was the name of your first crush?")
    fpsecurityquestion1.grid(row=4,column=1,sticky='W')
    fpsecurityquestion2 = tk.Entry(fpframe,textvariable = fpscrtyans)
    fpsecurityquestion2.grid(row=5,column=1,pady=5)
    fpbtn1 = tk.Button(fpframe,text = "BACK",bg = "Green",fg = "White",relief = "sunken",command = lambda: fp_back()).grid(row=6,column=0,pady=10)
    fpbtn2 = tk.Button(fpframe,text = "RESET",bg = "Red",fg = "Black",relief = "sunken",command = lambda: fp_reset()).grid(row=6,column=1,pady=10)
    fpbtn3 = tk.Button(fpframe,text = "SUBMIT",bg = "Blue",fg = "White",command = lambda: fp_validation()).grid(row=7,columnspan=2,pady=5)

#IMPORTING ALL MODULES REQUIRED FOR THIS PROGRAM CODE.
import tkinter as tk#TKINTER MODULE IS USED TO BUILD THE GUI AND IT ACT AS OUR FRONT END.
import re#REGULAR EXPRESSION MODULE IS USED FOR VALIDATION PURPOSES.
import sqlite3 as sq3#SQLITE3 MODULE IS USED TO STORE DATA INTO A DATABASE AND IT ACT AS OUR BACK END.
from sqlite3 import Error
import COVID19Py
import random

#BUILDING THE MAIN WINDOW.
root = tk.Tk()
root.title("Apple Boulevard Library")#TITLE FOR OUR MAIN WINDOW.
#VARIOUS TEXTVARIABLES INORDER TO RETRIEVE VALUES AND THEY ARE DECLARED AS STRINGVAR() TYPES.
siusrnme = tk.StringVar()
sipass = tk.StringVar()
sufstnme = tk.StringVar()
sulstnme = tk.StringVar()
suemlid = tk.StringVar()
suphno = tk.StringVar()
supass = tk.StringVar()
suconpass = tk.StringVar()
suscrtyqst = tk.StringVar()
suscrtyans = tk.StringVar()
fpidntty = tk.StringVar()
fppass = tk.StringVar()
fpconpass = tk.StringVar()
fpscrtyqst = tk.StringVar()
fpscrtyans = tk.StringVar()

con = sql_connection()#SQL_CONNECTION CREATES A BRIDGE BETWEEN FRONT END AND BACK END.
cursorObj = con.cursor()#CURSOR() LETS YOU USE SQLITE3 IN PYTHON ENVIORNMENT.
user_acc_table(con)#METHOD TO CREATE A TABLE TO STORE DATA.
#INITIALLY OUR PROGRAM CODE STARTS WITH STU_SIGNIN() METHOD.

tot_chance = 5
temp = tot_chance
null = 0
you_point = null
comp_point = null

expression = ""

stu_signin()
tk.mainloop()
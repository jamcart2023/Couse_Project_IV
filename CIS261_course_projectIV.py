# James Carter CIS261 Course Project IV

from datetime import datetime

def CreateUsers():
    print("##### Create users, passwords, and roles #####")
    UserFile = open("Users.txt", "a+")
    while True:
        username = GetUserName()
        if (username.upper() == "END"):
            break 
        userpwd = GetUserPassword()
        userrole = GetUserRole()

        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)

        UserFile.close()
        printuserinfo()

def GetUserName():
    username = input("Enter a username or 'End' to quit: ")
    return username

def GetUserPassword():
    pwd = input("Enter Password: ")
    return pwd

def GetUserRole():
    userrole = input("Enter a role (Admin or User): ")
    while True:
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return userrole
    else:
        userrole = input("Enter a user role (Admin or User): ")

def printuserinfo():
    UserFile = open("Users.txt", "r")
    while True:
        UserDetail =  UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "") 
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpassword = UserList[1]
        userrole = UserList[2] 
        print("User Name: ", username, "Password: ", userpassword, "Role: ", userrole)
        
# This is the end of creating users. now def login and while statements for flow

def Login():
    UserFile = open("Users.txt", "r")
    UserList = []
    UserName = input("Enter your user name: ")
    UserRole = "None" 
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
           return UserRole, UserName
        UserDetail = UserDetail.replace("\n", "") 

        UserList = UserDetail.split("|")
        if UserName == UserList[0]:
            UserRole = UserList[2]
    return UserRole, UserName

# The remaining code consists of phase 3
# second part of project starts here

def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetDatesWorked():
    fromdate = input("Please enter start date in the following format MM/DD/YYYY: ")
    todate = input("Please enter end date in the following format MM/DD/YYYY: ")
    return fromdate, todate 

def GetHoursWorked():
    hours = float(input("Enter hours: "))
    return hours

def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printInfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00 
    TotTax = 0.00
    TotNetPay = 0.00
    EmpFile = open("Employees.txt", "r")
    while True: 
        rundate = input("Enter the date you want to run the report (MM/DD/YYYY) or All for all data in file: ")
        if (rundate.upper() == 'ALL'):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break       
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue
        while True:
            EmpDetail = EmpFile.realine()
            if not EmpDetail:
                break
            EmpDetail = EmpDetail.replace("\n", "")

            EmpList = EmpDetail.split("|")
            fromdate = EmpList[0]
            if (str(rundate).upper() != "ALL"):
                checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
                if (checkdate < rundate):
                    continue
                todate = EmpList[1]
                empname = EmpList[2]
                hours = float(EmpList[3])
                hourlyrate = float(EmpList[4])
                taxrate = float(EmpList[5])
                grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)




                EmpDetailList.append(EmpList)
                break



    for EmpList in EmpDetailList:
        fromdate =EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]

        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        
        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
       
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        EmpTotals['TotEmp'] = TotEmployees
        EmpTotals['TotHrs'] = TotHours
        EmpTotals['TotGrossPay'] = TotGrossPay
        EmpTotals['TotTax'] = TotTax
        EmpTotals['TotNetPay'] = TotNetPay
        EmpDetailList = True
    if (EmpDetailList):
        printTotals(EmpTotals)
    else:
        print("No Employee Details to print")   

def printTotals(EmpTotals):
    print()
    print(f"Total Number of Employees: {EmpTotals['TotEmp']}")
    print(f"total hours of the Employees: {EmpTotals['TotHrs']}")
    print(f"Total Gross Pay of Employees: {EmpTotals['TotGrossPay']:,.2f}")
    print(f"Total tax of Employees: {EmpTotals['TotTax']:,.1%}")       
    print(f"Total Net Pay of Employees: {EmpTotals['TotNetPay']:,.2f}")  

if __name__ == "__main__":
    ###########################################
    CreateUsers()
    print()
    print("##### Login #####")
    UserRole, UserName = Login()
    EmpDetailList = False
    EmpTotals = {}
    if (UserRole.upper() == "NONE"):
        print(UserName, "is not a valid user")  
    else:

        if {UserRole.upper() == "ADMIN"}:
            ####################################
            EmpFile = open("employeeinfo.txt", "a+")
            while True:
                empname = GetEmpName()
                if (empname.upper() == "END"):
                    break
                fromdate, todate = GetDatesWorked()
                hours = GetHoursWorked()    
                hourlyrate = GetHourlyRate()
                taxrate = GetTaxRate()  
                EmpDetail = fromdate + "|" + todate + "|" + empname + "|" + str(hours) + "|" + str(hourlyrate) + "|" + str(taxrate) + "\n"  
                EmpFile.write(EmpDetail)

            EmpFile.close()
            printInfo(EmpDetailList)

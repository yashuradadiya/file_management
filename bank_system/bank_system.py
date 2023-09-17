class operation:
    # ============================== SPLIT FILE IN ARRAY ==============================
    def split(s):
        file = open('bank_system.txt','r')
        r = file.read()
        k = r.split('\n\n-----------------------------------------------------\n\n')
        s.f=[]
        for i in range(len(k)):
            s.f.append(k[i].split('\n'))
        for i in range(len(s.f)):
            l = []
            for j in range(len(s.f[i])):
                l.append(s.f[i][j].split(' = '))
            s.f[i]=l
    # ============================== JOIN ARRAY ==============================
    def join(s):
        j1 = []
        for i in range(len(s.f)):
            k1 = []
            for j in range(len(s.f[i])):
                k1.append(' = '.join(s.f[i][j]))
            j1.append('\n'.join(k1))
        i1 = "\n\n-----------------------------------------------------\n\n".join(j1)
        file = open('bank_system.txt','w')
        file.write(i1)
        file.close()
class bank(operation):
    # ============================== CREATE ACCOUNT ==============================
    def create_acc(s):
        print(' ------------ CREATE ACCOUNT ------------ ')
        name = input("Enter Name : ")
        ch = 0
        while ch!=2:
            acc_no = int(input("Enter Account Number : "))
            s.split()
            for i in range(len(s.f)-1):
                if int(s.f[i][1][1])==acc_no:
                    ch=1
                    break
            if ch==1:
                print("Enter Another Account Number")
                ch = 0
            else:
                ch = 2
        ch = 3
        while ch<1 or ch>2:
            print("1 -> Saving Account    2-> Current Account ")
            ch = int(input("Enter Your Account Choice : "))
        if ch==1:
            account = 'Saving'
            balance = 10000
        else:
            account = 'Current'
            balance = 5000
        r = "Name = "+name+"\nAccount_No = "+str(acc_no)+"\nAccount = "+account+"\nBalance = "+str(balance)+"\n\n-----------------------------------------------------\n\n"
        file = open('bank_system.txt','a')
        file.write(r)
        file.close()
        s.login()
    # ============================== Login ==============================
    def login(s):
        print(' ------------ LOGIN ACCOUNT ------------ ')
        ch = 0
        while ch!=1:
            acc_check = int(input("Enter Account Number : "))
            s.split()
            for i in range(len(s.f)-1):
                if int(s.f[i][1][1])==acc_check:
                    s.acc = i
                    ch=1
            if ch==0:
                print("Enter Valid Account Number")
class calculation(bank):
    # ============================== DEPOSITE ==============================
    def diposite(s):
        print(' ------------ DEPOSITE MONEY ------------ ')
        bal = int(s.f[s.acc][3][1])
        add = int(input("Enter Amount To Deposite : "))
        bal += add
        s.f[s.acc][3][1] = str(bal)
        s.join()
    # ============================== WITHDRAW ==============================
    def withdraw(s):
        print(' ------------ WITHDRAW MONEY ------------ ')
        ch=0
        while ch!=1:
            bal = int(s.f[s.acc][3][1])
            add = int(input("Enter Amount To Withdraw : "))
            bal -= add
            if bal >=0:
                s.f[s.acc][3][1] = str(bal)
                ch=1
            else:
                print("Not saficiant Balance")
        s.join()
    # ============================== Show Details ==============================
    def show_detils(s):
        i1 = []
        for i in range(len(s.f[s.acc])):
            i1.append(' = '.join(s.f[s.acc][i]))
        j = '\n'.join(i1)
        print(" ------------ ACCOUNT DETAIL ------------ ")
        print(j)
# ============================================ MAIN ============================================
ch = 5
i = 1
obj = calculation()
while ch>2 or ch<0:
    print("1 -> create account    2 -> Login account    0 -> Exit")
    ch = int(input("Enter Your Choice : "))
    if ch==1:
        obj.create_acc()
    elif ch==2:
        obj.login()
    elif ch==0:
        print("--------------Thank You------------------")
        i=0
    else:
        print("Enter Valid choice")

while i!=0:
    print('1.->Deposite    2.->withdraw   3.->Check Account   0.-> Exit')
    i = int(input('Enter Your Choice : '))
    if i==1:
        obj.diposite()
    elif i==2:
        obj.withdraw()
    elif i==3:
        obj.show_detils()
    elif i==0:
        print('--------------Thank You------------------')
    else :
        print("Enter Valid Choice")
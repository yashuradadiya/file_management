class operation:
    # ============================== SPLIT CUSTOMER FILE IN ARRAY ==============================
    def split_customer(s):
        file = open('customer.txt','r')
        r = file.read()
        k = r.split('\n\n-----------------------------------------------------\n\n')
        s.f=[]
        for i in range(len(k)-1):
            s.f.append(k[i].split('\n'))
        for i in range(len(s.f)):
            l = []
            for j in range(len(s.f[i])):
                l.append(s.f[i][j].split(' = '))
            s.f[i]=l
    # ============================== SPLIT CATEGORY FILE IN ARRAY ==============================
    def split_category(s):
        file = open('category.txt','r')
        r = file.read()
        k = r.split('\n\n---------------------------------\n\n')
        s.h=[]
        for i in range(len(k)-1):
            s.h.append(k[i].split('\n'))
        for i in range(len(s.h)):
            l = []
            for j in range(len(s.h[i])):
                l.append(s.h[i][j].split(' = '))
            s.h[i]=l
class customer(operation):
    # ============================== CREATE ACCOUNT ==============================
    def create_acc(s):
        print(' ------------ CREATE ACCOUNT ------------ ')
        name = input("Enter Name : ")
        ch = 0
        while ch!=2:
            id = int(input("Enter Register Number : "))
            s.split_customer()
            for i in range(len(s.f)):
                if int(s.f[i][0][1])==id:
                    ch=1
                    break
            if ch==1:
                print("Enter Another Register Number")
                ch = 0
            else:
                ch = 2
        password = input("Enter Password : ")
        txt = 'Id = '+id+'\nName = '+name+'\nPassword = '+password+'\n\n-----------------------------------------------------\n\n'
        file = open('customer.txt','a')
        file.write(txt)
        file.close
        s.login()
    # ============================== Login ==============================
    def login(s):
        print(' ------------ LOGIN ACCOUNT ------------ ')
        ch = 0
        while ch!=1:
            r_id  = int(input("Enter Register Number : "))
            pass_w = input("ENter PassWord : ")
            s.split_customer()
            for i in range(len(s.f)-1):
                if int(s.f[i][0][1])==r_id and s.f[i][2][1]==pass_w:
                    s.acc = i
                    ch=1
            if ch==0:
                print("Enter Valid Id or Password")
class category(customer):
    # ============================== CATEGORIES ==============================
    def categories(s):
        print(' ------------ CATEGORIES ------------ ')
        ch=8
        while ch!=0:
            print('1.-> Create Category     2.-> View Category    3.-> Delete Ctegory    0.-> Exit')
            ch = int(input("Enter your choice : "))
            if ch==1:
                s.add_category()
            elif ch==2:
                print(' ------------ VIEW  CATEGORIES ------------ ')
                s.view_category()
            elif ch==3:
                s.delete_category()
            elif ch==0:
                print('--------------Thank You------------------')
            else:
                print("Enter Valid Choice")
    # ============================== ADD CATEGORIES ==============================
    def add_category(s):
        print(' ------------ ADD  CATEGORIES ------------ ')
        name = input("Enter Name of Category : ")
        txt = 'Name = '+name+'\nUser_Id = '+str(s.acc)+'\n\n---------------------------------\n\n'
        file = open('category.txt','a')
        file.write(txt)
        file.close()
    # ============================== VIEW CATEGORIES ==============================
    def view_category(s):
        s.split_category()
        j=1
        for i in range(len(s.h)):
            if int(s.h[i][1][1]) == s.acc:
                print(j,'. ',s.h[i][0][1])
                j+=1
    # ============================== DELETE CATEGORIES ==============================
    def delete_category(s):
        s.split_category()
        j=1
        k=[]
        for i in range(len(s.h)):
            if int(s.h[i][1][1]) == s.acc:
                print(j,'. ',s.h[i][0][1])
                k.append(s.h[i])
                j+=1
        ch = int(input('Enter Number of Category : '))
        print(k[ch-1])
        k = 1

# ============================================ MAIN ============================================
ch = 5
i = 1
obj = category()
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
    print('1.->Category    2.->Products   0.-> Exit')
    i = int(input('Enter Your Choice : '))
    if i==1:
        obj.categories()
    elif i==2:
        obj.withdraw()
    elif i==3:
        obj.show_detils()
    elif i==0:
        print('--------------Thank You------------------')
    else :
        print("Enter Valid Choice")
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
    # ============================== SPLIT PRODUCT FILE IN ARRAY ==============================
    def split_product(s):
        file = open('products.txt','r')
        r = file.read()
        k = r.split('\n\n-------------------------------------------------------------\n\n')
        s.p=[]
        for i in range(len(k)-1):
            s.p.append(k[i].split('\n'))
        for i in range(len(s.p)):
            l = []
            for j in range(len(s.p[i])):
                l.append(s.p[i][j].split(' = '))
            s.p[i]=l
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
        txt = 'Id = '+str(id)+'\nName = '+name+'\nPassword = '+password+'\n\n-----------------------------------------------------\n\n'
        file = open('customer.txt','a')
        file.write(txt)
        file.close()
        s.login()
    # ============================== Login ==============================
    def login(s):
        print(' ------------ LOGIN ACCOUNT ------------ ')
        ch = 0
        while ch!=1:
            r_id  = int(input("Enter Register Number : "))
            pass_w = input("ENter PassWord : ")
            s.split_customer()
            for i in range(len(s.f)):
                if int(s.f[i][0][1])==r_id and s.f[i][2][1]==pass_w:
                    s.acc = r_id
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
        print(' ------------ VIEW  CATEGORIES ------------ ')
        j=1
        t = []
        for i in range(len(s.h)):
            temp = []
            if int(s.h[i][1][1]) == s.acc:
                temp.append(j)
                temp.append(s.h[i][0][1])
                j+=1
                t.append(temp)
        from tabulate import tabulate
        head = ["No.","Category"]
        print(tabulate(t, headers=head, tablefmt="fancy_outline"))
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
        ch=0
        while ch>=j or ch<=0:
            ch = int(input('Enter Number of Category : '))

        for i in range(len(s.h)):
            if s.h[i][1][1]==k[ch-1][1][1] and s.h[i][0][1]==k[ch-1][0][1]:
                s.del_id = i
        s.delete_category_product()
        for i in range(s.del_id,len(s.h)-1):
            s.h[i] = s.h[i+1]
        j1 = []
        for i in range(len(s.h)-1):
            k1 = []
            for j in range(len(s.h[i])):
                k1.append(' = '.join(s.h[i][j]))
            j1.append('\n'.join(k1))
        j1.append('')
        i1 = "\n\n---------------------------------\n\n".join(j1)
        file = open('category.txt','w')
        file.write(i1)
        file.close()
    def delete_category_product(s):
        s.split_product()
        arr = s.p
        n = len(arr)
        i=0
        while i<n:
            if arr[i][1][1]==s.h[s.del_id][0][1]:
                for j in range(i,n-1):
                    arr[j]=arr[j+1]
                arr[n-1] = ''
                n-=1
                i-=1
            i+=1
        s.p = []
        for i in range(len(arr)):
            if arr[i]!='':
                s.p.append(arr[i])
        j1=[]
        for i in range(len(s.p)):
            k1 = []
            for j in range(len(s.p[i])):
                k1.append(' = '.join(s.p[i][j]))
            j1.append('\n'.join(k1))
        j1.append('')
        i1 = "\n\n-------------------------------------------------------------\n\n".join(j1)
        file = open('products.txt','w')
        file.write(i1)
        file.close()

    # ============================== PRODUCTS ==============================
class product(category):
    def products(s):
        print(' ------------ PRODUCTS ------------ ')
        ch=8
        while ch!=0:
            print('1.-> Add Product     2.-> View Product   3.-> Quntity of Product    4.-> Delete Product    0.-> Exit')
            ch = int(input("Enter your choice : "))
            if ch==1:
                s.add_product()
            elif ch==2:
                s.view_products()
            elif ch==3:
                s.quntity_products()
            elif ch==4:
                s.delete_products()
            elif ch==0:
                print('--------------Thank You------------------')
            else:
                print("Enter Valid Choice")
    # ============================== ADD PRODUCTS ==============================
    def add_product(s):
        print(' ------------ ADD  PRODUCTS ------------ ')
        name = input("Enter Product Name : ")
        s.split_category()
        j=1
        k=[]
        for i in range(len(s.h)):
            if int(s.h[i][1][1]) == s.acc:
                print(j,'. ',s.h[i][0][1])
                k.append(s.h[i])
                j+=1
        ch=0
        while ch>=j or ch<=0:
            ch = int(input('Enter Number of Category : '))
        for i in range(len(s.h)):
            if s.h[i][1][1]==k[ch-1][1][1] and s.h[i][0][1]==k[ch-1][0][1]:
                cat_id = i
        category_name = s.h[cat_id][0][1]
        quntity = int(input("Enter Quntity Of Products : "))
        user_id = s.acc
        txt = "Name = "+name+"\nCategory = "+category_name+"\nQuntiry = "+str(quntity)+"\nUser_id = "+str(user_id)+"\n\n-------------------------------------------------------------\n\n"
        file = open('products.txt','a')
        file.write(txt)
        file.close()
    # ============================== VIEW PRODUCTS ==============================
    def view_products(s):
        print(' ------------ VIEW  PRODUCTS ------------ ')
        s.split_product()
        k=1
        t = []
        for i in range(len(s.p)):
            temp = []
            if int(s.p[i][3][1])==s.acc:
                temp.append(k)
                for j in range(len(s.p[i])-1):
                    temp.append(s.p[i][j][1])
                k+=1
                t.append(temp)
        from tabulate import tabulate
        head = ["No.","Product Name","Category","Quntity"]
        print(tabulate(t, headers=head, tablefmt="mixed_grid"))
    # ============================== QUNTITY OF PRODUCTS ==============================
    def quntity_products(s):
        s.split_product()
        ch = 0
        upd = []
        j = 1
        while ch<=0 or ch>=3:
            print("1. -> ADD      2. -> Minus")
            ch = int(input("Enter Your Choice : "))
            if ch==1:
                print(' ------------ ADD QUNTITY PRODUCTS ------------ ')
                for i in range(len(s.p)):
                    if int(s.p[i][3][1])==s.acc:
                        print(j,".  ->  ",s.p[i][0][1])
                        upd.append(s.p[i])
                        j+=1
                ch = int(input("In Which Product You Want To ADD : "))
                qun = int(input("Enter Quntity To ADD : "))
                for i in range(len(s.p)):
                    if s.p[i][0][1]==upd[ch-1][0][1] and s.p[i][3][1]==upd[ch-1][3][1]:
                        upd_id = i
                qunt_prd = int(s.p[upd_id][2][1])
                qunt_prd += qun
            elif ch==2:
                print(' ------------ MINUS QUNTITY PRODUCTS ------------ ')
                for i in range(len(s.p)):
                    if int(s.p[i][3][1])==s.acc:
                        print(j,".  ->  ",s.p[i][0][1])
                        upd.append(s.p[i])
                        j+=1
                ch = int(input("In Which Product You Want To Minus : "))
                for i in range(len(s.p)):
                    if s.p[i][0][1]==upd[ch-1][0][1] and s.p[i][3][1]==upd[ch-1][3][1]:
                        upd_id = i
                qunt_prd=-1
                while qunt_prd<0:
                    qun = int(input("Enter Quntity To ADD : "))
                    qunt_prd = int(s.p[upd_id][2][1])
                    qunt_prd -= qun
                    if qunt_prd<0:
                        print("Not saficiant Quntity")
        s.p[upd_id][2][1] = str(qunt_prd)
        j1 = []
        for i in range(len(s.p)):
            k1 = []
            for j in range(len(s.p[i])):
                k1.append(' = '.join(s.p[i][j]))
            j1.append('\n'.join(k1))
        j1.append('')
        i1 = "\n\n-------------------------------------------------------------\n\n".join(j1)
        file = open('products.txt','w')
        file.write(i1)
        file.close()
    # ============================== DELETE PRODUCTS ==============================
    def delete_products(s):
        s.split_product()
        j=1
        k=[]
        for i in range(len(s.p)):
            if int(s.p[i][3][1]) == s.acc:
                print(j,'. ',s.p[i][0][1])
                k.append(s.p[i])
                j+=1
        ch=0
        while ch>=j-1 or ch<=0:
            ch = int(input('Enter Number of Product : '))

        for i in range(len(s.p)):
            if s.p[i][3][1]==k[ch-1][3][1] and s.p[i][0][1]==k[ch-1][0][1]:
                del_id = i
        for i in range(del_id,len(s.p)-1):
            s.p[i] = s.p[i+1]
        j1 = []
        for i in range(len(s.p)-1):
            k1 = []
            for j in range(len(s.p[i])):
                k1.append(' = '.join(s.p[i][j]))
            j1.append('\n'.join(k1))
        j1.append('')
        i1 = "\n\n-------------------------------------------------------------\n\n".join(j1)
        file = open('products.txt','w')
        file.write(i1)
        file.close()

# ============================================ MAIN ============================================
ch = 5
i = 1
obj = product()
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
        obj.products()
    elif i==0:
        print('--------------Thank You------------------')
    else :
        print("Enter Valid Choice")
ch = 1
m=[]
total = 0
cnt=0
while ch!=0:
    print("1. insert")
    print("2. Update")
    print("3. View")
    print("4. Delete")
    print("0. Exit")
    ch = int(input("Enter tour choice : "))
    if ch == 1 :
        print('insert')
        f = open("student_result.txt",'w')
        name = input("Enter Name : ")
        for i in range(5):
            m.append(int(input("Enter Marks of Sub "+str(i+1)+" : ")))
            total = total+m[i]
            if m[i]<=35:
                cnt+=1
        if cnt==0:
            per = total/5
            result = 'PASS'
        elif cnt<=2:
            per = 0
            result = 'AY-KT'
        else:
            per=0
            result = 'FAIL'
    
        min = min(m)
        max = max(m)
        
        if per>=80:
            grade = 'first class'
        elif per>=60:
            grade = 'second class'
        elif per>=35:
            grade = 'third class'
        else:
            grade = '-'

        f.write("Name = "+name+"\nsub1 = "+str(m[0])+"\nsub2 = "+str(m[1])+"\nsub3 = "+str(m[2])+"\nsub4 = "+str(m[3])+"\nsub5 = "+str(m[4])+"\n\nTotal = "+str(total)+"\nPer = "+str(per)+"\nMin = "+str(min)+"\nMax = "+str(max)+"\nResult = "+result+"\nGrade = "+grade)
        f.close()
    elif ch == 2:
       
        f = open('student_result.txt','r')

        r = f.read()
        s = r.split("\n")
        print("1. Name")
        print("2. Marks")
        ch = int(input("choice : "))
        if ch==1:
            n = s[0].split(" = ")
            n[1] = input("Enter Name : ")
            k = ' = '.join(n)
            s[0] = k
        elif ch==2:
            p = int(input("Which sub u want to change : "))
            num=[]
            for i in range(1,6):
                num.append(s[i].split(" = "))
            num[p-1][1] = input("Enter sub "+str(p)+" : ")
            k = ' = '.join(num[p-1])
            s[p] = k
            cnt = 0
            total = 0
            min = int(num[0][1])
            max = int(num[0][1])
            for i in range(5):
                print(num[i])
                total = total + int(num[i][1])
                if min>int(num[i][1]):
                    min = int(num[i][1])
                if max<int(num[i][1]):
                    max = int(num[i][1])
                if int(num[i][1])<=35:
                    cnt+=1
            if cnt==0:
                per = total/5
                result = 'PASS'
            elif cnt<=2:
                per = 0
                result = 'AY-KT'
            else:
                per=0
                result = 'FAIL'
                
            if per>=80:
                grade = 'first class'
            elif per>=60:
                grade = 'second class'
            elif per>=35:
                grade = 'third class'
            else:
                grade = '-'
            s[7] = "Total = "+str(total)
            s[8] = "Per  = "+str(per)
            s[9] = "Min = "+str(min)
            s[10] = "Max = "+str(max)
            s[11] = "Result = "+str(result)
            s[12] = "Grade = "+str(grade)
        m=''
        for i in s:
            m += (i+"\n")
        f.close()
        f = open('student_result.txt','w')
        f.write(m)
        f.close()
    elif ch==3:
        f = open('student_result.txt','r')
        print(f.read())
        f.close()
    elif ch ==4:
        f = open('student_result.txt','w')
        f.write('')
        f.close()
    elif ch == 0 :
        print("Thank you")
    else :
        print("Enter valid choice")
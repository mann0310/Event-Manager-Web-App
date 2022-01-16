import re
main_list=[]
name_list=[]


def present_contacts():
     n=[]
     n.append("FERNANDO ALONSO")
     name_list.append("FERNANDO ALONSO")
     m_list=[]
     m_list.append("9876574675")
     n.append(m_list)
     main_list.append(n)
     n=[]
     n.append("LEWIS HAMILTON")
     name_list.append("LEWIS HAMILTON")
     m_list=[]
     m_list.append("4358345675")
     m_list.append("6547567483")
     n.append(m_list)
     main_list.append(n)
     n=[]
     n.append("SEBESTIAN VETTEL")
     name_list.append("SEBESTIAN VETTEL")
     m_list=[]
     m_list.append("8348785656")
     m_list.append("4377568764")
     m_list.append("8577589836")
     n.append(m_list)
     main_list.append(n)
     name_list.sort()
     main_list.sort()

def insert():
     print("*****Add New Contact*****")
     name=str.upper(input("Enter Name: "))
     n=[]
     n.append(name)
     name_list.append(name)
     i=str("y")
     i.lower()
     m_list=[]
     while i==str("y"):
          number=input("Enter Mobile Number: ")
          m_list.append(number)
          i=str.lower(input("Do you want to add another number(yes/no) : (Y/N) ? "))
          
     n.append(m_list)
     main_list.append(n)
     print("\n*****CONTACT ADDED!*****")
     name_list.sort()
     main_list.sort()
     print("\n")

def add_to_existing():
     print("*****Add Number to Existing Contact*****")
     subs=str.upper(input("Enter keyword(s) to search in contacts: "))
     try:
          res=[x for x in name_list if re.search(subs,x)]
          i=0
          if(len(res)>1):
               for r in res:
                    i+=1
                    print(str(i)+" : "+r)
               j=int(input("Please select name from above mentioned contact names: "))
               k=name_list.index(res[j-1])
               print("Name: "+main_list[k][0])
               number=input("Enter Moile Number to be added: ")
               main_list[k][1].append(number)
               print("*****NEW NUMBER ADDED!*****\n")
               print("Name: "+main_list[k][0])
               length=len(main_list[k][1])
               i=1
               while i<=length:
                    print("Contact Number "+str(i)+": "+main_list[k][1][i-1])
                    i+=1
               print("\n")
          else:
               k=name_list.index(res[0])
               print("Contact Found-> Name: "+main_list[k][0])
               number=input("Enter Mobile Number to be added: ")
               main_list[k][1].append(number)
               print("\n*****NEW NUMBER ADDED!*****\n")
               print("Name: "+main_list[k][0])
               length=len(main_list[k][1])
               i=1
               while i<length:
                    print("Contact Number "+str(i)+": "+main_list[k][1][i-1])
                    i+=1
               print("New Contact Number: "+main_list[k][1][i-1])
               print("\n")
     except:
          print("None of the Contacts match with given keyword(s).")

def search():
     print("*****Search in Contacts*****")
     subs=str.upper(input("Enter keyword(s) to search in contacts: "))
     try:
          res=[x for x in name_list if re.search(subs,x)]
          i=0
          if(len(res)>1):
               for r in res:
                    i+=1
                    print(str(i)+" : "+r)
               j=int(input("Please select name from above mentioned contact names: "))
               k=name_list.index(res[j-1])
               print("\n*****CONTACT FOUND!*****\n")
               print("Name: "+main_list[k][0])
               length=len(main_list[k][1])
               i=1
               while i<=length:
                    print("Contact Number "+str(i)+": "+main_list[k][1][i-1])
                    i+=1
               print("\n")
          else:
               k=name_list.index(res[0])
               print("\n*****CONTACT FOUND!*****\n")
               print("Name: "+main_list[k][0])
               length=len(main_list[k][1])
               i=1
               while i<=length:
                    print("Contact Number "+str(i)+": "+main_list[k][1][i-1])
                    i+=1
               print("\n")
     except:
          print("None of the Contacts match with given keyword(s).")

def display():
     print("*****All Contacts*****\n")
     for i in main_list:
          print("Name: "+i[0])
          length=len(i[1])
          l=1
          while l<=length:
               print("Contact Number "+str(l)+": "+i[1][l-1])
               l+=1
          print("\n")

print("\n")
print("******* Welcome to Contact Keeper *******\n\n")
print("How can I help you? Sir/Madam \n")
present_contacts()
c=1
while c in (1,2,3,4):
     print("*****Contact Keeper Services*****")
     print("1: Add New Contact")
     print("2: Add number to Existing Contact")
     print("3: Search Contact")
     print("4: Display all Contacts")
     print("0: Exit\n\n")
     c=int(input("Enter your choice: "))
     print("\n")
     if c==1:
          insert()
     elif c==2:
          add_to_existing()
     elif c==3:
          search()
     elif c==4:
          display()
     elif c==0:
          print("THANK YOU! HAVE A NICE DAY.\n")
     else:
          print("Invalid Choice! Please select a proper choice.\n")
          c=1
     
import pandas as pd
df=pd.read_excel('./data/my_data.xlsx')

#print(df.columns.tolist())
#print(df[["EMP_ID"]])
#if( 111 in df['EMP_ID'].to_list() ):
    # print("true")

#print("hi")

while  True :
    
    print("Please Select Any of Below Option:")
    print("1.View all records of excel")
    print("2.Add new rows through command line program")
    print("3.Update any existing entry through commandline ")
    print("4.Delete any existing entry through commandline")
    print("5.Exit")
    my_var=int(input("Please enter any of above option: ") or 1000)
    if(my_var==1):
        print(df)
        input("Please press enter to continue")
    elif(my_var==2):
        row_add=[]
        try:
           Emp_new=int(input("Enter the employee ID to be added: "))
        except ValueError:
            print("ERROR:Please enter valid integer value")
            continue

        if (Emp_new in df["EMP_ID"].to_list()):
            print("Empployee ID already exits.Could you please try new one.")
            continue
        row_add.append(Emp_new)
        row_add.append(str(input("Enter the employee Name to be added: ")))
        try:
          row_add.append(int(input("Enter the Employee Joining Year to be added: ")))
        except ValueError:
            print("ERROR:Please enter valid integer value")
            continue
        df.loc[len(df.index)]=row_add
        writer = pd.ExcelWriter('./data/my_data.xlsx')
        df.to_excel(writer,sheet_name='Sheet1',index=False)
        writer.save()
        input("We have updated changes please enter to continue")
    elif(my_var==3):
        row_update=[]
        try:
          Emp_update=int(input("Enter the employee ID of employee to be updated:  "))
        except ValueError:
            print("ERROR:Please enter valid integer value")
            continue
        if (not (Emp_update in df["EMP_ID"].to_list())):
            print("Empployee ID is not correct.")
            continue
        old_val=df.iloc[df[df['EMP_ID']==Emp_update].index].to_string(header=None,index=False)
        try:
          Emp_id_update=int(input("Enter the updated employee ID of employee to be updated or enter for defaults %r :  " %(old_val)) or df.loc[df[df['EMP_ID']==Emp_update].index]["EMP_ID"].item() )
        except ValueError:
            print("ERROR:Please enter valid integer value")
            continue
        if ((Emp_id_update in df["EMP_ID"].to_list()) and (Emp_update !=Emp_id_update)):
            print("Empployee ID already exits.Could you please try new one.")
            continue 
        row_update.append(Emp_id_update)      
        row_update.append(str(input("Enter the update employee Name of employee to be updated or enter for defaults %r: " %(old_val) ) or df.loc[df[df['EMP_ID']==Emp_update].index]["NAME"].item()))
        try:
          row_update.append(int(input("Enter the update employee joining of employee to be updated or enter for defaults %r:" %(old_val)) or df.loc[df[df['EMP_ID']==Emp_update].index]["YEAR"].item() ))
        except ValueError:
            print("ERROR:Please enter valid integer value")
            continue
        df.iloc[df.EMP_ID==Emp_update]=row_update
        writer = pd.ExcelWriter('./data/my_data.xlsx')
        df.to_excel(writer,sheet_name='Sheet1',index=False)
        writer.save()
        input("We have updated changes please enter to continue")
    elif(my_var==4):
        try:
        
         Emp_row_del=int(input("Enter the employee ID of employee to be deleted:  "))
        except ValueError:
            print("ERROR:Please enter valid integer value")
            continue
        if (not (Emp_row_del in df["EMP_ID"].to_list())):
            print("Empployee ID is not correct.")
            continue

        df.drop(df[df['EMP_ID']==Emp_row_del].index,inplace=True)
        writer = pd.ExcelWriter('./data/my_data.xlsx')

        df.to_excel(writer,sheet_name='Sheet1',index=False)
        writer.save()
        input("We have updated changes please enter to continue")
    elif(my_var==5):
        break



    
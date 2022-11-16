# importing packages
import csv
import datetime


def update_expiry(file_path="D://programming//python//files//subscription.csv"):
    
    f = open(file_path,'r') #opening the csv file

    dt = csv.DictReader(f) #converting to DictReader object
    dt =list(dt) #converting the csv columns as list of dictionaries with column headers as key 

    for i in dt:
        i["expiry_date"] = datetime.datetime.strptime(i["expiry_date"],"%Y-%m-%d").date() #the column "expiry_date" is in string format we 
                                                                                          #need it in date object type 
        i["payment"]=int(i["payment"]) #the column payment is in string format so converting to int 
    

    new=[]

    for i in dt:

        row = {}
        # checking the payment column an adding the extra expiry date
        if i["payment"] == 300:
            date = i["expiry_date"] + datetime.timedelta(days=28)

        elif i["payment"] == 600:
            date = i["expiry_date"] + datetime.timedelta(days=84)
        
        elif i["payment"] == 1000:
            date = i["expiry_date"] + datetime.timedelta(days=336)
        else:
            pass

        #adding the updated value in to new dictionary(row) and appending each row into new list
        row["user"] = i["user"]
        row["expiry_date"] = str(date)
        new.append(row)

    #creating the new output csv file with updated data
    f=open("D://programming//python//files//updted_subscription.csv","w",newline='')
    headers=['user','expiry_date']
    data = csv.DictWriter(f,delimiter=',',fieldnames=headers)
    data.writerow(dict((heads,heads) for heads in headers))
    data.writerows(new)
    f.close()



update_expiry()

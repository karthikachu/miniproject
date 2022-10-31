date=(input("enter today date:"))
place=(input("enter the place:"))
name=(input("enter your name:"))
departmentname=(input("enter your departmentname:"))
section=(input("enter your section:"))
collegename=(input("enter your collegename:"))
principalname=(input("enter your  principalname:"))
subject=(input("enter the subject:"))
reason=(input("enter the reason for leave:"))
noofleavedays=(input("enter no of leave days:"))
dateofleave=(input("enter the date of leave:"))
leaveletter=f'''
                 
                                     Requestingletter

                                                                                       Date:{date} 

To
        {principalname}
        {departmentname}{section}
        {collegename}
        {place}

Respected Sir/Madam  
             sub:{subject}
                      I am {name} from {departmentname} {section}. Due to {reason} am unable to attending the classes   
 on from {noofleavedays} days {dateofleave}.So I kindly request you to give me a permission for my absence and grant me a leave.
                            
                              Thankyou
                                                                         your's faithfully
                                                                             {name}                                                                         
'''
print(leaveletter)


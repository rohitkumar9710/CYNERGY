# CYNERGY
A service dev

Link of Google Drive containing the PPT including the video:
https://drive.google.com/drive/folders/1GH9Olh49CurlLMasK5Dk0MdTdBShA6yc?usp=sharing

###Guide to the website

![]()



**Table of Contents**

[TOCM]

[TOC]

#Sign Up
##FlowChart of Signing In

```flow
st=>start: Enter into website
su=>condition: Subject 1 (customer)?
si1=>condition: Signed In? 
si2=>condition: Signed In? 
csu=>operation:  Customer Sign Up 
ssu=>operation:  Serviceman Sign Up
clo=>operation:  Customer Log In 
slo=>operation:  Service Log In 

st->su
su(yes)->si1(yes)->clo
su(yes)->si1(no)->csu->clo
su(no)->si2(yes)->slo
su(no)->si2(no)->ssu->slo


```
                    

1.	When you first land on our website you will see two options which include, sign in or sign up. If you already have an account you may select sign in and fill in the details of your existing account. On the other hand, if you don't have an account you may select sign up and create a new account by filling in the required details.
2.	After fillings in the details, you will receive an OTP on your registered email ID. Please carefully fill the OTP and we advise you to not share it with anyone.
3.	Upon successfully logging in to your existing account or creating a new account you will be redirected to our home page.

#Sequence Diagram
                    
```seq
Note left of Customer: Searches for the right serviceman 
Customer->Serviceman: Requests for service 
Note right of Serviceman: Serviceman thinks\nabout it 
Serviceman-->Customer: Accepts the service 
Serviceman-->Customer: Contact him/her
Note left of Customer: Recieves the service
Customer->>Serviceman: Gives feedback
```



#Customers
Customers enters into his homepage and gets the list of services.
He may search for more clarity to what he/she needs by reading the prospectus below which details the fields.
  ##Customer Profile
  Here the customer gets to edit his/her profile to what is correct. He/she may review his/her profile as well. 
  ##Selecting a service
  The customer gets to choose one of those options, and they may proceed by either of the two options available.
  ###Custom Search
  Here the customer gets to search the serviceman/woman of his/her own choice on the basis of his/her experience, avg. ratings and all. And after fixing a deadline may proceed to request the serviceman/woman for the service.
  ###Random Search
  Here the customer gets more personal with us by believing on what we decide is best for the customer. He may just ellaborate what he/she needs as a service. We will choose the serviceman/woman from our side.
  ##Notifications
  Here the customer recieves all his notifications, about his/her request and the option to canacel the same, whether the serviceman accepted his/her request.
  ###Feedback
  This can be taken as a confirmation of whether the work was done or not. And with how much efficacy.
  ##History
  All the past details of services recieved gets stored here.
  ##Donate Us
  The customer has an option to donate us if he/she feels like doing for the support and better involvement of the service people. There will nothing be stored for us.
  ##Log out
 #Servicemen
 Customers enters into his homepage and gets the list of services.
He may search for more clarity to what he/she is good at by reading the prospectus below which details the fields.
  ##Serviceman Profile
    Here the customer gets to edit his/her profile to what is correct. He/she may review his/her profile as well. 
  ##Being ready for a service
  Now the serviceman/woman can mark themselves for any one or more of these services available. Not available marks them absent for being requested for that obviously.
  And they submit what they selected.
  ##Notifications
   Here the serviceman/woman recieves all his notifications, about his/her being requested and the option to accept or reject the same.
  ##History
  All the past details of services he/she delivered gets stored here.
  ##Log out

                


###End
   

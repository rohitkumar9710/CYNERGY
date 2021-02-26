# CYNERGY
![Flow chart sign up](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/logo%20redueced.png)

A service dev

Link of Google Drive containing the PPT including the video:
https://drive.google.com/drive/folders/1GH9Olh49CurlLMasK5Dk0MdTdBShA6yc?usp=sharing

### Guide to the website

# Sign Up
#### Note: The OTP is 1234 for now.

## FlowChart of Signing In

```flow
st=>start: Enter into website
su=>condition: Customer or
serviceman?
si1=>condition: Signed In? 
si2=>condition: Signed In? 
csu=>operation:  Customer Sign Up 
ssu=>operation:  Serviceman Sign Up
clo=>operation:  Customer Log In 
slo=>operation:  Service Log In 
st->su
su(yes@customer)->si1(yes)->clo
su(yes@customer)->si1(no)->csu->clo
su(no@serviceman)->si2(yes)->slo
su(no@serviceman)->si2(no)->ssu->slo
```
![Flow chart sign up](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/flowchart.JPG)

![Flow chart sign up](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Sign%20Up.jpeg)
### Customer Sign Up
![Flow chart sign up](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Sign%20up%20Form%20Customer.jpeg)
### Serviceman Sign Up
![Flow chart sign up](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Sign%20up%20Form%20Serviceman.jpeg)
### Logging In
![Flow chart sign up](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Signing%20In.jpeg)




                    

1.	When you first land on our website you will see two options which include, sign in or sign up. If you already have an account you may select sign in and fill in the details of your existing account. On the other hand, if you don't have an account you may select sign up and create a new account by filling in the required details.
2.	After fillings in the details, you will receive an OTP on your registered email ID. Please carefully fill the OTP and we advise you to not share it with anyone.
3.	Upon successfully logging in to your existing account or creating a new account you will be redirected to our home page.

# Sequence Diagram
                    
```seq
Note left of Customer: Searches for the right serviceman 
Customer->Serviceman: Requests for service 
Note right of Serviceman: Serviceman thinks\nabout it 
Serviceman-->Customer: Accepts the service 
Serviceman-->Customer: Contact him/her
Note left of Customer: Recieves the service
Customer->>Serviceman: Gives feedback
```
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/sequence.JPG)
# About Us
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/About%20Us%201.jpeg)
## What It is
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/About%20Us%20What%20It%20Is.jpeg)
## How It Works
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/About%20us%20How%20it%20works.jpeg)



# Customers
Customers enters into his homepage and gets the list of services.
He may search for more clarity to what he/she needs by reading the prospectus below which details the fields.
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Customer%20homepage.jpeg)

## Customer Profile
Here the customer gets to edit his/her profile to what is correct. He/she may review his/her profile as well. 
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Customer%20profile%20edit.jpeg)
## Selecting a service
The customer gets to choose one of those options, and they may proceed by either of the two options available.
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Customer%20homepage%202.jpeg)
### Custom Search
Here the customer gets to search the serviceman/woman of his/her own choice on the basis of his/her experience, avg. ratings and all. And after fixing a deadline may proceed to request the serviceman/woman for the service.
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Custom%20Search.jpeg)
### Random Search
  
Here the customer gets more personal with us by believing on what we decide is best for the customer. He may just ellaborate what he/she needs as a service. We will choose the serviceman/woman from our side.
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Random%20Search.jpeg)
## Notifications
  
Here the customer recieves all his notifications, about his/her request and the option to canacel the same, whether the serviceman accepted his/her request.
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Customer%20notification.jpeg)
  
### Feedback
  
This can be taken as a confirmation of whether the work was done or not. And with how much efficacy.
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Customer%20feedback.jpeg)
  
## History
All the past details of services recieved gets stored here.
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Customer%20History.jpeg)
  
## Donate Us
  
The customer has an option to donate us if he/she feels like doing for the support and better involvement of the service people. There will nothing be stored for us.
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Donate%20Us.jpeg)
  
## Log out
  
# Servicemen

Customers enters into his homepage and gets the list of services.
He may search for more clarity to what he/she is good at by reading the prospectus below which details the fields.
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Service%20Homepage%201.jpeg)

## Serviceman Profile
  
Here the customer gets to edit his/her profile to what is correct. He/she may review his/her profile as well.
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Serviceman%20profile.jpeg)
    
## Being ready for a service
  
Now the serviceman/woman can mark themselves for any one or more of these services available. Not available marks them absent for being requested for that obviously.
And they submit what they selected.
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Service%20Homepage%202.jpeg)
## Notifications
  
Here the serviceman/woman recieves all his notifications, about his/her being requested and the option to accept or reject the same.
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/ServiceNotification.png)
## History
  
All the past details of services he/she delivered gets stored here.
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Service%20History.jpeg)
## Log out
# Our Team
![Sequence](https://github.com/rohitkumar9710/CYNERGY/blob/main/media/readme/Our%20Team.jpeg)


                


### End
   

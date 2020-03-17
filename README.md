# kris_cindle
Kris kindle application that was made for an extended family and emails recipients with the name of who they got. 

## Why
- I was asked to do a draw for Kris cindle within my extended family. The rules were that immediate family members could not get eachother, and obviously everyone must give one person a gift and recieve one gift. If I did this by hand, I would know who would get me, so I decided to do this quickly in Python. 

## How does it work?
- This application is simple. Fill *names.json* with the information for all people involved in the Kris kindle. The information required is surname, first name and email. *matchmake.py* takes two arguments, the surname and first name of the giver. It then returns the surname and firstname of the recipient. The recipient is determined by creating a list of all possible candidates that exist in all families, except their own (`if surname == family_name`). A random name from the list is then returned and deleted from the *names.json* file. 
- The user must input their own email and password credentials to *send.py*. 

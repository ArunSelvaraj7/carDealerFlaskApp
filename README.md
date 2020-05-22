# carDealerFlaskApp

A Simple flask web application used for two major purposes as described below,
1. The application can be used by the unregistered customers to search for the stocks and the respective details available with the dealer.
2. The owner of the application can sign in with admin credentials to add new stocks, modify/delete existing stocks, search for a particular vehicle with a unique registration number, search a specific customer with a given mobile number (The stocks sold to that particular customer will be displayed along with his/her details). 


The application is embedded with postgreSql, where all the stock details are stored. Additional security is incorporated with flask-bcrypt. The application is also used as a store house to retrieve the details about the purchaser of a particular vehicle. The database is maintained forever which allows the owner of the app to search for particular customer or vehicle as and when required. The web app is deployed on heroku for testing purpose...


Run Instruction:
1. Clone/Download the repo
2. pip install -r requirements.txt  #To install the required dependecies
3. python run.py

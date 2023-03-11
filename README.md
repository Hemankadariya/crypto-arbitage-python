# crypto-arbitage-python
checks the price of a token in several exchanges and sends an email notification if there is a price difference greater than 5% between any of the exchanges

To run this code, you'll need to make sure you have Python installed on your computer. You can download and install Python from the official website: https://www.python.org/downloads/

Once you have Python installed, you'll need to open a text editor (like Notepad or Sublime Text) and paste the code into a new file.

Next, you'll need to modify the code to add in your own email address and email password. Look for the lines that say:

makefile
Copy code
# Replace with your email address and password
``sender_email = "YOUR_EMAIL_ADDRESS"
sender_password = "YOUR_EMAIL_PASSWORD"
Replace "YOUR_EMAIL_ADDRESS" with your own email address, and "YOUR_EMAIL_PASSWORD"`` with your email password.

Save the file with a .py extension (e.g. token_price_checker.py), and then open a terminal or command prompt and navigate to the directory where you saved the file.

Type the command python token_price_checker.py to run the script. If there are any big differences in price, the script will send an email to your specified email address.

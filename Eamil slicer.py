##===============================================#
#take input from user#
email = input("print Your Email:").strip()

#variables

# get the username part (everything before "@")
username = email[:email.index("@")]

# get the domain part (everything after "@")
domain = email[:email.index("@") +1 :]

#get the length of the username and print it
print(f"Your User Name Is {username} & Your Domain Is {domain}")


# Imports
from asyncio import *
from asyncore import loop
from cgi import print_arguments
#################################################################################################################################################################

class color:
    BOLD = '\033[1m'

class topic:
    MAIN = "(Services, Refund, Contact) \n\n"
    # MochiSquare Services
    SERVICES = "Server Hosting, Web Hosting, Game Server Hosting, Web Design"
    # MochiSquare Refund Policy
    REFUND = "Please refer to this link " + "https://mochisquare.com/" + " for more information about our refund policy."
    # Contact Information
    CONTACT = "Please contact us at https://mochisquare.com/contact-me/"
    # Custom Exit Message
    EXITS = "Thank you for your time with Mochisquare. Hope to see you again!"

# cinput stands for custom inputs
class cinput:
    GETNAME = input("May I get your name? \n\n")
    CUSTOMER_QUESTION = input("How may I help you today " + GETNAME + "\n\n" + color.BOLD + "\n").lower()

print(cinput.CUSTOMER_QUESTION)
print("Hello " + cinput.GETNAME + ",welcome to MochiSquare! \n\n")

for i in cinput.GETNAME:

    if cinput.GETNAME == ("services"):
        input("\n" + topic.SERVICES + "\n\n")
    elif cinput.GETNAME == ("refund"):
        print(topic.REFUND)
    elif cinput.GETNAME == ("contact"):
        print(topic.CONTACT)
    elif cinput.GETNAME == ("exit"):
        print(topic.EXITS)
    else:
        loop

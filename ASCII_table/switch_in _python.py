# Example printing week day basis of it number
 
def week(num):
    switch_case = {
        0:'sunday',
        1:'monday',
        2:'tuesday',
        3:'wednesday',
        4:'thursday',
        5:'friday',
        6:'saturday'
    }
    print(switch_case.get(num,'invalid day'))
    
week(4)   
# hotel menus or any menu

def menu():
    choice = int(input('Welcome to Star Travels. Thank you for calling us. Please Select from the menu\n1.Home\n2.Booking\n3.Enquiry\n4.Complaints\n5.Exit\n'))
    switch_case = {
        1:'Home',2:'Booking',3:'Enquiry',4:'Complaints',5:'Exit'
    }
    
    print('Taking you to ..')
    print(switch_case.get(choice,"Please enter a valid choice"))


menu()

from  registration import Registration

class moneyCreditWithdrawlSystem:
    # Constructor method __init__ for initializing the object
    def __init__ (self):
        pass
    
    
    # Method for handling the entrance process
    def entrance_process_init(self):
        if self.entrance_retry < 3:
            print('''Please select your options in below
                1.Enter 1 for Registration
                2.Enter 2 for Login
                ''') 
            
            try:
               self.enter_process = int(input())
            except Exception as e:
                self.entrance_retry += 1
                if self.entrance_retry != 3:
                    print(f"Please enter only numeric values. Your input {str(e).split()[-1]} is not valid")   
                self.entrance_process_init()                  
                return True
            if self.enter_process == 1:
                print("Navigating to Registration")
                registration_obj = Registration()
                registration_obj.collecting_registration_inputs()
                
            elif self.enter_process == 2:
                print("Navigating to Login")
            else :
                self.entrance_retry += 1
                if self.entrance_retry != 3:
                    print("Please enter correct entrance process number as 1 or 2")
                self.entrance_process_init()
                ##
        else : 
            print("Entrance process retries exceeded over 3 times. Unfortunately we can't process your request due to incorrect input")        
            
            
# Defining a main Function.
# The project process starts from here
if __name__ == '__main__':
    # Printing Welcome messages to user 
    print('Hi,Welcome to Money Credit Witdral System')
    print('I am assesting for credit and withdrawl money from your bank account')

    # Creating a object for "moneyCreditWithdrawlSystem" class
    main_object = moneyCreditWithdrawlSystem()
    # Assigning a "entrance_retry" variable to control  wrong information from user at entrance process
    main_object.entrance_retry = 0
    # Call the entrance process method to start the interaction with the user
    main_object.entrance_process_init()

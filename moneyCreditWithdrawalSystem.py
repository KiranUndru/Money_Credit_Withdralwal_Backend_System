class moneyCreditWithdrawlSystem:
    # pass
    def __init__ (self):
        pass

    def entrance_process_init(self):
        if self.entrance_retry < 3:
            print('''Please select your options in below
                1.Enter 1 for Registration
                2.Enter 2 for Login
                ''')
            self.enter_process = int(input()) 
            print(self.enter_process)
            if self.enter_process == 1:
                print("Navigating to Registration")
            elif self.enter_process == 2:
                print("Navigating to Login")
            else :
                print("Please enter correct entrance process number as 1 or 2")
                self.entrance_process_init()
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
    #
    main_object.entrance_process_init()
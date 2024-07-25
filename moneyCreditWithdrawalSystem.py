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


if __name__ == '__main__':
    print('Hi,Welcome to Money Credit Witdral System')
    print('I am assesting for credit and withdrawl money from your bank account')

    main_object = moneyCreditWithdrawlSystem()
    main_object.entrance_retry = 0
    main_object.entrance_process_init()
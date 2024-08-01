import data_validation

class Registration:
    def __init__(self):
        pass
    
    def collecting_registration_inputs(self):
        first_name=input("Please enter your first name: ")
        data_validation.validation_name(first_name)
        last_name=input("Please enter your last name: ")
        data_validation.validation_name(last_name)
        print(first_name, last_name)
        
        try :
                age = input("Please enter your age: ")
                data_validation.validate_age(age)
                
        except data_validation.ValidationError as e:
                print(f"""Error: {e}. Please try again. 
                      Age must be a numeric value. 
                      and it should be positive value 
                      and above 18 and below 100.""")
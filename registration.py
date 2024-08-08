import data_validation

class Registration:
    def __init__(self):
        self.registration_details=dict()
    
    def collecting_registration_input(self):
        name_pattern = r'^[a-zA-Z]+$'
        allowed_domains = ["gmail", "yahoo"]
        # Regex pattern to check for a valid email structure
        email_pattern =r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Collect a valid First name 
        while True:
            try:
                first_name  = input('Please enter your first name: \n')
                is_valid = data_validation.validate_name(first_name,name_pattern)
                if is_valid:
                    self.registration_details['first_name'] = first_name
                    break
                else:
                    print("First name is invalid. Please try again.")
            except ValueError as ve:
                print(f"Error: {ve}. Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")
        
        # Collect a valid Last name
        while True:
            try:
                last_name  = input('Please enter your last name: \n')
                is_valid = data_validation.validate_name(last_name,name_pattern)
                if is_valid:
                    self.registration_details['last_name'] = last_name
                    break
                else:
                    print("Last name is invalid. Please try again.")
            except ValueError as ve:
                print(f"Error: {ve}. Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")
                
        # collect a valid Age
        while True:
            try:
                age  = input('Please enter your age: \n')
                is_valid = data_validation.validate_age(age)
                if is_valid:
                    self.registration_details['age'] = age
                    break
                else:
                    print("Age is invalid. Please try again.")
            except ValueError as ve:
                print(f"Error: {ve}. Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")
                
        # Collect a valid Email address
        while True:
            try:
                email = input('Please enter a valid email address: \n')
                is_valid = data_validation.validate_email(email,allowed_domains,email_pattern)
                if is_valid:
                    self.registration_details['email'] = email
                    break
                else:
                    print("Invalid email. Please try again.")
            except ValueError as ve:
                print(f"Error: {ve}. Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")
        
        # Collect a valid date of birth
        while True:
            try:
                dob = input('Please enter your date of birth (dd/mm/yyyy): \n')
                is_valid=data_validation.validate_dob(dob)  # This will raise an error if invalid
                # print("Date of birth is validated.")
                if is_valid:
                    self.registration_details['dob'] = dob
                    break
            except ValueError as ve:
                print(f"Error: {ve}. Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")
        
        # Collect a valid password
        while True:
            try:
                password = input('Please enter a password: \n')
                password = data_validation.validate_password(password)
                self.registration_details['password'] = password
                break
            except ValueError as ve:
                print(f"Error: {ve}. Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")
        
         # Confirm password
        while True:
            try:
                confirm_password = input('Please confirm your password: \n')
                data_validation.confirm_password(confirm_password,password)
                self.registration_details['confirm_password'] = confirm_password
                break
            except ValueError as ve:
                print(f"Error: {ve}. Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")
        
         # Collect a valid phone number
        while True:
            try:
                phone_number = input('Please enter your phone number (10 digits): \n')
                data_validation.validate_phone_number(phone_number)
                self.registration_details['phone_number'] = phone_number
                break
            except ValueError as ve:
                print(f"Error: {ve}. Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")
    
                
        print(f"""
            First Name: {first_name}
            Last Name: {last_name}
            Age:{age}
            Email Address: {email}
            Date of Birth: {dob}
            Password: {password}
            """)
        
    
    
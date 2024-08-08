
import data_validation

class Login:
    def __init__(self):
        pass

    def login_with_credentials(self):
            allowed_domains = ["gmail", "yahoo"]
            # Regex pattern to check for a valid email structure
            email_pattern =r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            
            try:
                email = input('Please enter user id: \n')
                password = input('Please enter user password: \n')
                isEmailValid = data_validation.validate_email(email,allowed_domains,email_pattern)
                isPassValid = data_validation.validate_password(password)
                if isEmailValid and isPassValid:
                    print(f"user logged in successfully..")
            except ValueError as ve:
                    print(f"Error: user id and pasword incorrect.")
            except Exception as e:
                    print(f"Error: user id and pasword incorrect.")
        
        

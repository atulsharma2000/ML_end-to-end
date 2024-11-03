import sys
# custom exception hangling

def error_message_details(error,error_details:sys): #error details is present in sys
    _ ,_ , exc_tb = error_details.exc_info()
    # we are only intrested in exc_tb (not the starting two)   --> it will  give us the last error details (on which file , on which line  etc)
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno,str(error)) 
    
    return error_message


# when error raises this function will be called

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_message_details(error_message,error_details=error_detail)
    
    def __str__(self):
        return self.error_message

    
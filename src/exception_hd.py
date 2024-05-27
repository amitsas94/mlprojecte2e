import sys
from src.logger_hd import logging


def error_message_info(error, error_info:sys):
    _,_,exc_traceback=error_info.exc_info()
    file_name=exc_traceback.tb_frame.f_code.co_filename
    error_info_message = "Error occured in python script name [{0}] at line number [{1}] with error message [{2}]".format(
    file_name,exc_traceback.tb_lineno,str(error)
    )
    return error_info_message


class CustomExceptionhd(Exception):
    def __init__(self, error_info_message, error_info:sys):
        super().__init__(error_info_message)
        self.error_info_message=error_message_info(error_info_message,error_info=error_info)

    def __str__(self):
        return self.error_info_message
    

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomExceptionhd(e,sys)
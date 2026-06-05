#Task 1:
import logging 
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if args: 
            pos_params = list(args)
        else:
            pos_params = "none"
        
        if kwargs:
            kw_params = dict(kwargs)
        else: 
            kw_params = "none"
        
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {pos_params}")
        logger.log(logging.INFO, f"keyword parameters: {kw_params}")
        logger.log(logging.INFO, f"return: {result}")
        logger.log(logging.INFO, f"----")
        return result 
    
    return wrapper 

def no_parameters():
    print("Hello, World!")

def positional_argument(*args):
    return True

def keyword_argument(**kwargs):
    return logger_decorator 

if __name__ == "__main__":
    no_parameters()
    positional_argument(1, 2, 3, "apple")
    keyword_argument(a= 10, b= 20, name= "Nallely")
#Task 2:
def type_converter(type_of_output):
    def decorator(func):
        def wrapper():
            value = func()
            try: 
                return type_of_output(value)
            except ValueError:
                raise ValueError(f"Can't convert {value!r} to {type_of_output.__name__}")
        return wrapper
    return decorator 

@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return "not a number"

#Mainline of program
if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)
    
    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer")
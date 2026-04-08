#Task 1: Hello
def hello():
    return "Hello!" 
print(hello())

#Task 2: Greet w a formatted String
def greet(name):
    return f"Hello, {name}!"
print(greet("Lisa"))

#Task 3: Calculator
def calc(a, b, operation = "multiply"):
    if operation == "add":
        return a+b
    elif operation == "subtract":
        return a-b 
    elif operation == "multiply":
        return a*b
    elif operation == "divide":
        return a/b if b != 0 else "You can't divide by 0!"
    elif operation == "modulo":
        return a%b if b != 0 else "You can't divide by 0!"
    elif operation == "int_divide":
        return a//b if b != 0 else "You can't divide by 0!"
    elif operation == "power":
        return a**b 
    else:
        return "Invalid operations cannot be Multiplied!"
print(calc(2, 5, "multiply"))

#Task 4: Data Type Conversion 
def data_type_conversion(value, type_requested):
    try:
        if type_requested == "float":
            return float(value)
        elif type_requested == "str":
            return str(value)
        elif type_requested == "int":
            return int(value)
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {type_requested}."
print(data_type_conversion("27", "float"))

#Task 5: Grading System 
def grade(*scores):
    if not scores:
        return "Invalid data was provided."
    average = sum(scores)/len(scores)
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= "70":
        return "C"
    elif average >= "60":
        return "D"
    else:
        return "F"
print(grade(75, 85, 95))

#Task 6: Use a For Loop w/ a Range
def repeat(string, count):
    repeat_string = " "
    for _ in range(count): 
        repeat_string += string
    return repeat_string
print(repeat("up ", 4))

#Task 7: Student Scores (**Kwargs)
def student_scores(position_type, **kwargs):
    if not kwargs:
        return None
    if position_type == "best":
        return max(kwargs, key=kwargs.get)
    elif position_type == "mean":
        scores = kwargs.values()
        return sum(scores)/len(scores)
    else: 
        return ValueError("position_type not available.")
    

#Task 8: Titleize
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()

    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words)-1:
            result.append(word.capitalize())
        elif word.lower() in little_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())
    return " ".join(result)
print(titleize("after on"))
#print(titleize("green eggs and ham"))

#Task 9: Hangman
def hangman(secret, guess): 
    result = " "
    for letter in secret: 
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result
print(hangman("difficulty", "ic"))

#Task 10: Pig Latin 
def pig_latin(a_sentence):
    words = a_sentence.split()
    new_words = []
    vowels = "aeiou"
    
    for word in words:
        if word[0] in vowels: 
            new_words.append(word + "ay")
        else:
            new_words.append(word[1:] + word[0] + "ay")
    return " ".join(new_words)
print(pig_latin("apple"))

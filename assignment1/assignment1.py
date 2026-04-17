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
    try:
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
            return "Invalid operations cannot be multiplied!"
    except TypeError:
        return "You can't multiply those values!"
#print(calc(2, 5, "multiply"))
print(calc("first", "second", "multiply"))



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
    try:
        if not scores:
            return "No scores provided."
        average = sum(scores)/len(scores)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."
print(grade(75, 85, 95))


#Task 6: Use a For Loop w/ a Range
def repeat(string, count):
    repeat_string = ""
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
#print(student_scores("mean", Tom=75, Dick=89, Angela=91))
print(student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50))
    


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
    result = ""
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
        #rule 1 string starts w/ vowel add "ay" to end 
        if word[0] in vowels: 
            new_words.append(word + "ay")

            #rule 2 sting is a special word "qu"  
        elif word.startswith("qu"):
            new_words.append(word[2:] + "quay")

        else:
            # rule 3 one or several consonants move to end and add "ay" to end
            consonant_string = ""
            entire_word = word

            for i, letter in enumerate(word):
                if letter in vowels or (i > 0 and letter == 'y'):
                    entire_word = word[i:]
                    break
                elif i > 0 and letter == 'u' and consonant_string.endswith('q'):
                    consonant_string += letter
                    entire_word = word[i+1:]
                    break
                else: 
                    consonant_string += letter

            new_words.append(entire_word + consonant_string + "ay")
    return " ".join(new_words)

#print(pig_latin("apple"))
print(pig_latin("the quick brown fox"))
#print(pig_latin("quiet"))


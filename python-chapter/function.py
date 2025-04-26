
#######
def greet(name):
    return f"Hello, {name}"
print(greet("Karthi"))



########
def celsius_to_fahrenheit(celsius):
    return (celsius* 9/5) + 32

print(f"Fahrenheit: {celsius_to_fahrenheit(18)}")


####
def greets (name = "Guest"):
    return f"Hello, {name}!"

print(greets())
print(greets("Karthi"))



#### *args lets you pass a variable number of positional arguments to a function.
def sum_all(*arg):
    return sum(arg)

print(f"Sum: {sum_all(1, 2, 3, 4)}") 


### Using **kwargs (keyword arguments)
def print_person(**kwargs):
    for key, value in kwargs.items():
        print(f"person: {key}:{value}")
print_person(name="Karthi", age=30, city="Chennai")


### Create a formatted message
def format_message(**kwargs):
    return f"{kwargs.get('greeting', 'Hi')} {kwargs.get('name', 'there')}!"

print(format_message(greeting="Hello", name="Sam"))
print(format_message(greeting="Hello"))
print(format_message(name="Lily"))

### Using both *args and **kwargs together   
# Logger

def log_event(event_type, *args, **kwargs):
    print(f"[{event_type.upper()}]")

    if args:
        print("Positional info:", args)

    if kwargs:
        print("Extra data:")
        for key, value in kwargs.items():
            print(f"  {key} = {value}")

log_event(
    "error", 
   "File not found", 
    "/path/to/file", 
    code=404, 
    user="admin"
)


### Passing *args and **kwargs to another function
def base_func(*args, **kwargs):
    print("Base Function")
    print("Args:", args)
    print("Kwargs:", kwargs)

def wrapper_func(*args, **kwargs):
    print("Wrapper Function")
    base_func(*args, **kwargs)

wrapper_func(1, 2, name="Test", value=42)
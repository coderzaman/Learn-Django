from django import template

register = template.Library()

# def my_filter(value):
#     return "Added Text " + value

# receive argumnet in filter 
def my_filter(value, arg):
    return  arg + value

register.filter('custom_filter', my_filter)

# Make a file __init__.py in this folder for make it as library 

#  We can make it using decorators imporve readable
    # # my_filter.py
    # from django import template

    # # Register the template library
    # register = template.Library()

    # # Custom filter without arguments
    # @register.filter(name='custom_filter')
    # def my_filter(value):
    #     return "Added Text " + value

    # # Custom filter with an argument
    # @register.filter(name='custom_filter_with_arg')
    # def my_filter_with_arg(value, arg):
    #     return arg + value

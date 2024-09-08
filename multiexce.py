try:
    pass
except SyntaxError:
    print("Please check your syntax!")
except ValueError:
    print("please check your value!")
except NameError:
    print("please check your variable!")
except TypeError:
    print("please check your typing!")
except ZeroDivisionError:
    print("You can't devide by zero!")

from ast import Index


def error_handler (a) ->str:
    try:
        print(a)
    except ValueError:
        print ('You made a black hole!')
    except ZeroDivisionError:
        print ( "You shouldn't be here" )
    except  IndexError:
        print ("<class 'UnicodeError'>: That is not a valid character!")
    except TypeError:
        print ('No errors :)')
        return ValueError 
def error_handler (a:function) ->str:
    try:
        print(a())
        return ('No errors :)')
    except ZeroDivisionError:
        return ('You made a black hole!')
    except IndexError:
        return ( "You shouldn't be here" )
    except Exception as e:
        return (f"{type (e)}: {str(e)}")

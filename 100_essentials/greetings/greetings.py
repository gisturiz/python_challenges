def greetings(name, *args, msg = "Hello", punctuation = "!", **kwargs):
    # if kwargs
    if kwargs:
         # create an empty string to store all strings in kwargs
        strDescK = ""
        # iterate through each kwargs keys and values
        for key, value in kwargs.items():
            # add each kwarg key and value with the specified string format
            strDescK += (" " + key + " says " + '"' + value + '"' + ".")
        # print the string with other arguments
        return f"{msg}, {name}{punctuation}{strDescK}"

    # if args are present, do this      
    elif args:
        # create an empty string to store all strings in args
        strDesc = ""
        # iterate through each arg
        for i in args:
            # add each arg with the specified string format
            strDesc += (", the " + i)
        # print the string with other arguments
        return f"{msg}, {name}{strDesc}{punctuation}"
    else:
        # if no args are present, just print the present arguments
        return f"{msg}, {name}{punctuation}"


greetings('Bob', 'builder', 'tinker', 'tailor', 'soldier', 'spy', msg='Hi', punctuation='.')
greetings('Dave', msg='Hi', punctuation='!', Mark='Howdy', Jim='You owe me money')

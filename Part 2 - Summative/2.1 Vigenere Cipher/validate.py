def validate_input(func):
    """
    The decorator that validates the inputs for both the encode and decode functions.
    :param func: the function to have inputs validated
    :return wrapper function:
    """
    def validate_string(string):
        """
        removes special characters and numbers from string
        :param string: the string to be validated
        :return new_string = a edited string without special characters and numbers
        """
        string = string.upper()
        new_string = ""
        for i in string:
            if ord(i) in range(65,91):
                new_string = new_string + i
        return new_string

    def wrapper(*args, **kwargs):
        """
        THe wrapper function
        :param args:
        :param kwargs:
        :return:
        """
        text = args[0]
        text = validate_string(text)
        codebet = args[1]
        return func(text, codebet)
    return wrapper
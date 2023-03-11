import re
def removeSpecialCharacters(str):
    return re.sub('[^A-Za-z0-9]+', '', str)

def comma_join(arr):
    return ','.join(arr)

def specifier_join(arr):
    return ', '.join([f'{i} = %s' for i in arr])
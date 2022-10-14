
def checkEmptyValue(text:str):
    return bool(text)

def clearEmptyString(input:list):
    return list(filter(checkEmptyValue, input))
import re

test_cases = [
    "2100 Аптека", # Case#1 = one number and text
    "Это с учётом отложенных на окревус и солумедрол?" # Case#2 = no number
# Case#3 = more than 1 number
# Cawe#4 = number with k or K, 10k, 10K
# Case#5 = number with space 10 000
]




def return_number(text): 
    pattern = re.compile(r'\d+')
    match = pattern.search(text)
    if match != None:
        value = match.group() 
        return value
    else:
        return 0
        
#debug
def testing():
    for test in test_cases:
        print(return_number(test))

testing()



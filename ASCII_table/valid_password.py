# Valid Password : Write a function that determines whethere a string makes for a valid password
# it must be atleast 6 characters long & at most 12 characters long
# it also must have atleast one letter & one digit 
# and one character from '$@#'

def valid_passwd(passwd):
    p = list(passwd)
    a = []
    if len(p)<6 or len(p)>12: 
        return False
    if not(any(i.isdigit() for i in p)):  # 
        return False
    if 
    
print(valid_passwd('ello5jhjh'))
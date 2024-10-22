def check_len(password):
    if len(password) >= 8:
        return True
    else:
        return False


def check(password):
    check = [0, 0, 0, 0]
    for char in password:
        if char.islower():
            check[0] = 1
        elif char.isupper():
            check[1] = 1
        elif char.isdigit():
            check[2] = 1
        if not (char.isalpha() | char.isdigit() | char.isspace() ):
            check[3] = 1
    if sum(check) == 4:
        return True
    else:
        return False


def check_rep(password):
    n = len(password)
    for i in range(n-4):
        str1 = password[i:i+4]
        str2 = password[i+1::]
        if str1 in str2:
            return False
    return True


if __name__ == '__main__':
    while True:
        password = input("Enter password: ")
        vcheck1 = check_len(password)
        if not vcheck1:
            print("Password should be at least 8 characters long")
            continue
        vcheck2 = check(password)
        if not vcheck2:
            print("Password should contain at least one lowercase letter, one uppercase letter, one digit and one special character")
            continue
        vcheck3 = check_rep(password)
        if not vcheck3:
            print("Password should not contain any repeated characters")
            continue
        print("Password is valid")
        break

import re


def check_if_username_isalpha(login):
    return login.isalpha()


def check_username_length(login):
    return len(login) < 16


def check_if_login_match_email(login, email):
    return bool(re.match(login, email))


def check_if_email_match_pattern(email, pattern):
    # pattern = r'@ubs.com$'
    # pattern = "_"
    # pattern = r'\s')
    return re.search(pattern, email)


validated = False
while not validated:
    user_name = input("user_name: ").strip().lower()
    email = input("email: ").strip().lower()

    is_alpha = check_if_username_isalpha(user_name)
    is_length_valid = check_username_length(user_name)
    is_login_match_email = check_if_login_match_email(user_name, email)
    is_email_ends_with_ubs = check_if_email_match_pattern(email, pattern=r'@ubs.com$')
    is_email_contains_underscore = check_if_email_match_pattern(email, pattern="_")
    has_whitespace = check_if_email_match_pattern(email, pattern=r'\s')

    if not is_alpha:
        print("User name can’t include any numeric characters (digits)")
    if not is_length_valid:
        print("User name can’t exceed 15 characters")
    if not is_login_match_email:
        print("Email address must start with user name")
    if not is_email_ends_with_ubs:
        print("Email address must end with `@ubs.com`")
    if not is_email_contains_underscore:
        print("Email address must contain '_'")
    if has_whitespace:
        print("There are whitespaces in email address")

    if is_alpha and is_length_valid and is_login_match_email and is_email_contains_underscore and not has_whitespace:
        print("Success")
        validated = True
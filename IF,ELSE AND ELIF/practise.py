#creating password authentication

email = input('Please enter your email here: ')
if len(email) >= 5:
    if ('@' in email) and ('.' in email):
        if (email[-3] == '.') or (email[-4] == '.'):
            print('Good email')
        else:
            print('wrong email address')




    
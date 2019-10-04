ques1 = input( 'Is it raining?: ' ).lower()

if ques1 == 'yes':
    ques2 = input( 'Is it windy?: ' ).lower()
    if ques2 == 'yes':
        print( 'It is too windy for an umbrella.' )
    else:
        print( 'Take an umbrella.' )
else:
    print( 'Enjoy your day.' )

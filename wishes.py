import datetime
hour= datetime.datetime.now().hour
if 5<=hour<12:
    print('Good Morning!')
elif 12<=hour<=16:
    print('Good Afternoon!')
elif 16<=hour<=19:
    print('Good Evening!')
else:
    print('Good Night!')

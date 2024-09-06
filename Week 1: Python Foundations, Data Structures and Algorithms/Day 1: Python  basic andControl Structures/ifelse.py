number = int(input('Enter a number: '))

for i in range(number):
    d = input("Please enter a day of the week: ")
    day = d.lower()

    if day == 'sunday':
        print(f"{i+1}: It's Sunday!")
    elif day == 'monday':
        print(f"{i+1}: It's Monday!")
    elif day == 'tuesday':
        print(f"{i+1}: It's Tuesday!")
    elif day == 'wednesday':
        print(f"{i+1}: It's Wednesday!")
    elif day == 'thursday':
        print(f"{i+1}: It's Thursday!")
    elif day == 'friday':
        print(f"{i+1}: It's Friday!")
    elif day == 'saturday':
        print(f"{i+1}: It's Saturday!")
    else:
        print(f"{i+1}: It's not a day name.")

from config import converter

unit = input('What do you want to convert? lbs / stone / fl oz / pint ')
amount = float(input('How many %ss to convert? ' % unit))
result = converter.convert(amount, unit)(amount, unit)
print(result)
"""main.py"""
from modules import converter # converter module loaded into memory

unit = input('What do you want to convert? lbs / stone / fl oz / pint ')
amount = float(input('How many %s to convert? ' % unit))
result = converter.convert(amount, unit)
metric = 'kg' if unit in ['lbs', 'stone'] else 'ml'

print('%s %s is %s %s' % (amount, unit, result, metric))

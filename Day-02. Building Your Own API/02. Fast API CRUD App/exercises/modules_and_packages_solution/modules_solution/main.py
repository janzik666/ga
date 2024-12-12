# approach # 1
import converter # converter module loaded into memory

unit = input('What do you want to convert? lbs / stone / fl oz / pint ')
amount = float(input('How many %s to convert? ' % unit))
result = converter.convert(amount, unit)
metric = 'kg' if unit in ['lbs', 'stone'] else 'ml'

print('%s %s is %s %s' % (amount, unit, result, metric))


# approach # 2
from converter import convert  # <--- Changed this line

unit = input('What do you want to convert? lbs / stone / fl oz / pint ')
amount = float(input('How many %ss to convert? ' % unit))
result = convert(amount, unit)  # <--- And this line
print(result)
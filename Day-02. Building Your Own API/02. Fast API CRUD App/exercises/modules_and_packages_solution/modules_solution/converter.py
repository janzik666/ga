ratios = {
  'lbs': 0.453592,
  'stone': 6.35029,
  'fl oz': 28.4131,
  'pint': 568.261
}

def convert(amount, unit):
  return amount * ratios.get(unit, 1)
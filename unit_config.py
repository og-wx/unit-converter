from typing import Dict

from quantity import Quantity
from unit import Unit

unit_config: Dict[str, Quantity] = {
    'Mass': Quantity(
        std_unit = 'Kilograms',
        units = {
            'Kilograms': Unit(abbrev= 'kg', value_in_std_units = 1),
            'Grams': Unit(abbrev = 'g', value_in_std_units = 0.001),
            'Pounds': Unit(abbrev = 'lb', value_in_std_units = 0.453592),
            'Ounces': Unit(abbrev = 'oz', value_in_std_units = 0.0283495), 
        }
    ),
    'Length': Quantity(
        std_unit = 'Meters',
        units = {
            'Meters': Unit(abbrev = 'm', value_in_std_units = 1),
            'Centimeters': Unit(abbrev = 'cm', value_in_std_units = 0.01),
            'Inches': Unit(abbrev = 'in', value_in_std_units = 0.0254),
            'Feet': Unit(abbrev = 'ft', value_in_std_units = 0.3048), 
        }
    ),
    'Time': Quantity(
        std_unit = 'Seconds',
        units = {
            'Seconds': Unit(abbrev = 's', value_in_std_units = 1),
            'Minutes': Unit(abbrev = 'min', value_in_std_units = 60),
            'Hours': Unit(abbrev = 'hr', value_in_std_units = 3600),
            'Days': Unit(abbrev = 'd', value_in_std_units = 86400),
        }
    ),
    'Temperature': Quantity(
        std_unit = 'Celsius',
        units = {
            'Celsius': Unit(abbrev = f'{chr(176)}C', value_in_std_units = 0),
            'Fahrenheit': Unit(abbrev = f'{chr(176)}F', value_in_std_units= 32),
            'Kelvin': Unit(abbrev = f'{chr(176)}K', value_in_std_units = 273.15) 
        }
    ),
    'Atmospheric Pressure': Quantity(
        std_unit = 'Pascals',
        units = {
            'Pascals': Unit(abbrev = 'Pa', value_in_std_units = 1),
            'HectoPascals': Unit(abbrev = 'hPa', value_in_std_units = 10),
            'KiloPascals': Unit(abbrev = 'kPa', value_in_std_units = 1000),
            'Atmosphere': Unit(abbrev = 'atm', value_in_std_units = 101325),
            'Inches of Mercury': Unit(abbrev = 'inHg', value_in_std_units = 3386.389),
            'Pounds per Square Inch': Unit(abbrev = 'psi', value_in_std_units = 6.894757)
        }
    )
}
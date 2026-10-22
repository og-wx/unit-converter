from unit_config import unit_config
from result import Result
from typing import List

def list_quantities() -> List[str]:
    return list(unit_config.keys())

def list_units(quantity_name) -> List[str]:
    return list(unit_config[quantity_name].units.keys())

def convert_value(quantity_name: str,
                  from_unit_name: str,
                  to_unit_name: str,
                  value: float) -> Result:
    quantity = unit_config[quantity_name]
    from_unit = quantity.units[from_unit_name]
    to_unit = quantity.units[to_unit_name]

    match quantity_name:
        case 'Mass' | 'Length' | 'Time' | 'Atmospheric Pressure':
            value_in_to_units = (value *
                                 from_unit.value_in_std_units /
                                 to_unit.value_in_std_units)
        case 'Temperature':
            if from_unit_name == 'Celsius' and to_unit_name == 'Fahrenheit':
                value_in_to_units = ((1.8 * value) + 
                                     to_unit.value_in_std_units)
            elif from_unit_name == 'Celsius' and to_unit_name == 'Kelvin':
                value_in_to_units = (value +
                                     to_unit.value_in_std_units)
            elif from_unit_name == 'Fahrenheit' and to_unit_name == 'Celsius':
                value_in_to_units = (5/9) * (value - 
                                             from_unit.value_in_std_units)
            elif from_unit_name == 'Fahrenheit' and to_unit_name == 'Kelvin':
                value_in_to_units = (((value + 32)*(5/9)) + 
                                     to_unit.value_in_std_units)
            elif from_unit_name == 'Kelvin' and to_unit_name == 'Celsius':
                value_in_to_units = (value - 
                                     from_unit.value_in_std_units)
            elif from_unit_name == 'Kelvin' and to_unit_name == 'Fahrenheit':
                value_in_to_units = (((value - 
                                       from_unit.value_in_std_units) * (9/5)) +
                                       to_unit.value_in_std_units)
            else:
                value_in_to_units = value

    return Result(from_unit, to_unit, value, value_in_to_units)

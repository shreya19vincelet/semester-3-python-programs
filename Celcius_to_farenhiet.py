def temperature_convertor(celcius):
    farenhiet=(celcius*(9/5))+  32
    return farenhiet
celcius_temperature=float(input("enter the celcius temperature"))
farenhiet_temperature=temperature_convertor(celcius_temperature)
print("temperature in farenhiet is",farenhiet_temperature)
def cel_to_fahr(c):
    """
    This function to convert celcius temp to fahrenheit temp.
    :param c: float
    :return:float
   >>> cel_to_fahr(16)
    69.8
    """
    fahr = c * 1.8 + 32.0
    return fahr


cal = float(input("enter number to be converted"))
print(f"{cel_to_fahr(cal):.1f}")

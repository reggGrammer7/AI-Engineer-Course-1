# Tuples --> immutable sequences of values in parentheses
masala_dosa = ("cardmom", "cinnamon", "cloves", "pepper")
(spice1, spice2, spice3, spice4) = masala_dosa
print(f"Spice 1: {spice1}, Spice 2: {spice2}, Spice 3: {spice3}, Spice 4: {spice4}")

ginger_ratio, cardmon_ratio = 2,1 
print(f"Ratio is G:{ginger_ratio} and C:{cardmon_ratio}")
ginger_ratio, cardmon_ratio = cardmon_ratio, ginger_ratio
print(f"After swapping, Ratio is G:{ginger_ratio} and C:{cardmon_ratio}")

# Membership test
print(f"Is ginger in masala spices? {'ginger' in masala_dosa}")
print(f"Is cinnamon in masala spices? {'cinnamon' in masala_dosa}")

















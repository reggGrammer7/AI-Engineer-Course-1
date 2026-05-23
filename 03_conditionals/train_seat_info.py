# Build a train seat information system
# using the match case statement in python
seat_type = input("Enter your seat type (sleeper/AC/General/Luxury): ").lower()
match seat_type:
    case "sleeper":
        print("Sleeper class: Basic amenities, non-AC, affordable.")
    case "ac":
        print("AC class: Air-conditioned, comfortable, higher price.")
    case "general":
        print("General class: Basic seating, non-AC, budget-friendly.")
    case "luxury":
        print("Luxury class: Premium amenities, spacious, highest price.")
    case _:
        print("Unknown seat type. Please choose from sleeper, AC, general, or luxury.")








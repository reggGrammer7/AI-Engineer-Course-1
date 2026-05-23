def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai ....")
        if flavor == "unknown":
            raise ValueError (" We don't have that flavor")
    except ValueError as e:
        print("Error: ",e)
    else:
        print(f"{flavor} is served")
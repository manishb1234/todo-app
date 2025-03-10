def parse(value):
    parts = value.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {feet: feet, inches:inches}

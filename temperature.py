def main():
    while True:
        try:
            temperature = str(input("Enter temperature (C) or (F) ")).upper().strip()

            if temperature.endswith("C"):
                value = float(temperature[:-1])
                print(f"{round(C_to_F(value))}F")
                break

            elif temperature.endswith("F"):
                value = float(temperature[:-1])
                print(f"{round(F_to_C(value))}C")
                break

            else:
                error_message
                
        except ValueError:
            error_message

def C_to_F(c):
    return (c * 9/5) + 32

def F_to_C(f):
    return (f - 32) * 5/9

def error_message():
    print("Please enter a valid number followed by 'C' or 'F'")

if __name__ == "__main__":
    main()
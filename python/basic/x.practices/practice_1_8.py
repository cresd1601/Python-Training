def isPalindrome(number):
    """Check if a given number (as a string) is palindromic."""
    return str(number) == str(number)[::-1]

def findOdometerReading():
    """Find the odometer reading that satisfies the given conditions."""
    for odometer in range(100000, 1000000):  # Iterate through all six-digit numbers
        last_four = str(odometer)[-4:]  # Last 4 digits
        last_five = str(odometer + 1)[-5:]  # Last 5 digits one mile later
        middle_four = str(odometer + 2)[1:5]  # Middle 4 digits two miles later
        all_six = str(odometer + 3)  # All 6 digits three miles later
        
        if (isPalindrome(last_four) and
            isPalindrome(last_five) and
            isPalindrome(middle_four) and
            isPalindrome(all_six)):
            return odometer  # Return the odometer reading that meets all conditions

if __name__ == "__main__":
    odometer_reading = findOdometerReading()
    if odometer_reading:
        print(f"The odometer reading when first looked was: {odometer_reading}")
    else:
        print("No odometer reading satisfied the conditions.")

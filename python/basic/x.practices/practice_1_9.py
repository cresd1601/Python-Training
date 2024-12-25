def isReversible(child_age, mom_age):
    """Check if the two-digit ages are reversible."""
    return str(child_age).zfill(2) == str(mom_age).zfill(2)[::-1]

def findReversibleAges():
    """Find all child ages that satisfy the conditions, including the mom's age."""
    valid_ages = []
    
    for child_age in range(1, 100):  # Iterate through possible ages for the child
        for years_ago in range(0, child_age):  # Check the age history
            mom_age = child_age + years_ago + 18  # Ensure mom is at least 18 years older
            if isReversible(child_age - years_ago, mom_age):
                valid_ages.append((child_age - years_ago, mom_age))
    
    # Sort the list by child age
    return sorted(valid_ages, key=lambda x: x[0])

if __name__ == "__main__":
    valid_ages = findReversibleAges()
    if valid_ages:
        for child_age, mom_age in valid_ages:
            print(f"Child age: {str(child_age).zfill(2)}, Mom age: {str(mom_age).zfill(2)}")
    else:
        print("No valid ages found.")

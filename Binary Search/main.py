# Binary Search Function
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle element
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is smaller than mid, narrow the search to the left half
        elif arr[mid] > target:
            high = mid - 1
        # If target is greater than mid, narrow the search to the right half
        else:
            low = mid + 1
    
    return -1  # Target not found

# Main function to get user input and run the search
def main():
    # Take a sorted array from the user
    arr_input = input("Enter a sorted array (comma-separated): ")
    
    try:
        arr = list(map(int, arr_input.split(',')))  # Convert input to list of integers
    except ValueError:
        print("Invalid input. Please enter a list of numbers separated by commas.")
        return

    # Take the target element from the user
    target = int(input("Enter the element to search for: "))
    
    # Perform binary search
    result = binary_search(arr, target)
    
    # Output the result
    if result != -1:
        print(f"Element {target} found at index {result}. 🎉")
    else:
        print(f"Element {target} not found. ❌")

# Run the program
if __name__ == "__main__":
    main()

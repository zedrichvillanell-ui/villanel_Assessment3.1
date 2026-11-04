def main():
    print("=== 1. ARRAY DATA STRUCTURE ALGORITHM ===")

    # Initialize an array (Python list) and capacity
    capacity = 8
    name_array = []
    size = 0

    # Letters to add
    letters = ['V', 'i', 'l', 'l', 'a', 'n', 'e', 'l']

    print("\n--- Add Phase ---")
    for letter in letters:
        if size < capacity:
            name_array.append(letter)
            size += 1
            print(f"Added '{letter}' at index {size - 1} | Current Array: {name_array} | Size: {size}")
        else:
            print("Array is full!")
            break

    print("\n--- Remove Phase ---")
    while size > 0:
        index = size - 1
        removed_item = name_array.pop(index)
        size -= 1
        print(f"Removed '{removed_item}' from index {index} | Current Array: {name_array} | Size: {size}")

    # Verify array is empty
    if size == 0:
        print("\nVerification: Array is empty (size == 0).")


if __name__ == "__main__":
    main()
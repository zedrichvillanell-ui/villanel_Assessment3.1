def main():
    print("=== 3. STACK DATA STRUCTURE ALGORITHM (LIFO) ===")

    capacity = 8
    letter_stack = []
    top = -1
    letters = ['V', 'i', 'l', 'l', 'a', 'n', 'e', 'l']

    print("\n--- Add Phase (Push) ---")
    for letter in letters:
        if top < capacity - 1:
            letter_stack.append(letter)
            top += 1
            print(f"Pushed '{letter}' onto stack -> top = {top} | Stack: {letter_stack}")
        else:
            print("Stack Overflow!")
            break

    print("\n--- Remove Phase (Pop) ---")
    while top >= 0:
        popped_item = letter_stack.pop()
        print(f"Popped '{popped_item}' from stack -> top was {top}")
        top -= 1
        print(f"Current Stack: {letter_stack} | top = {top}")

    # Verify stack is empty
    if top == -1:
        print("\nVerification: Stack is empty (top == -1).")


if __name__ == "__main__":
    main()
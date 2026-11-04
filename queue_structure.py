def main():
    print("=== 4. QUEUE DATA STRUCTURE ALGORITHM (FIFO) ===")

    capacity = 8
    letter_queue = []
    front = 0
    rear = -1
    letters = ['V', 'i', 'l', 'l', 'a', 'n', 'e', 'l']

    print("\n--- Add Phase (Enqueue) ---")
    for letter in letters:
        if rear < capacity - 1:
            letter_queue.append(letter)
            rear += 1
            print(f"Enqueued '{letter}' -> rear = {rear}, front = {front} | Queue: {letter_queue}")
        else:
            print("Queue Overflow!")
            break

    print("\n--- Remove Phase (Dequeue) ---")
    while front <= rear:
        dequeued_item = letter_queue[front]
        print(f"Dequeued '{dequeued_item}' from front (index {front})")
        # In Python lists, we can pop the front or simulate the pointer shift:
        # To strictly match front pointer increments:
        front += 1
        current_queue = letter_queue[front:rear + 1]
        print(f"Current Queue elements: {current_queue} | front = {front}, rear = {rear}")

    # Verify queue is empty
    if front > rear:
        print("\nVerification: Queue is empty (front > rear).")


if __name__ == "__main__":
    main()
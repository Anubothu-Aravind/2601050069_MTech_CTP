# Stack and Queue using Type Hints and Dataclasses

## Objective

Develop reusable Python implementations of Stack and Queue using:
- Type hints
- Dataclasses
- Generic types

## Algorithm

### Stack - Push
1. Start.
2. Add the element to the top of the stack.
3. Stop.

### Stack - Pop
1. Start.
2. Remove the top element.
3. Return the removed element.
4. Stop.

### Stack - Peek
1. Start.
2. Return the top element without removing it.
3. Stop.

### Queue - Enqueue
1. Start.
2. Add the element to the rear of the queue.
3. Stop.

### Queue - Dequeue
1. Start.
2. Remove the front element.
3. Return the removed element.
4. Stop.

### Queue - Peek
1. Start.
2. Return the front element without removing it.
3. Stop.

## Concepts Used

- **Stack:** Follows LIFO (Last In, First Out).
- **Queue:** Follows FIFO (First In, First Out).
- **Dataclass:** `@dataclass` provides automatic class initialization.
- **Type hints:** `Generic[T]` allows the structures to work with different data types.
- **deque:** Provides efficient insertion and deletion at both ends.

## Expected Output

```text
Stack: [10, 20, 30]
Pop: 30
Peek: 20

Queue: ['A', 'B', 'C']
Dequeue: A
Peek: B
```

## Time Complexity

| Operation | Stack | Queue |
|---|---:|---:|
| Insert | O(1) | O(1) |
| Delete | O(1) | O(1) |
| Peek | O(1) | O(1) |

## Space Complexity

Both Stack and Queue require **O(n)** space for storing `n` elements.

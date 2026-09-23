# Student/Employee Data Model using Dataclasses

## Objective

Implement Student and Employee data models using Python dataclasses and compare them with a traditional class implementation.

## Algorithm

1. Start.
2. Create a traditional `Student` class using `__init__()`.
3. Create a `StudentData` class using `@dataclass`.
4. Create an `Employee` class using `@dataclass`.
5. Define ID, name, marks, and salary attributes.
6. Create objects from each class.
7. Display the objects.
8. Compare the two approaches.
9. Stop.

## Program

The complete Python program is available in:

`Student_Employee_Dataclass_Comparison.ipynb`

## Sample Output

```text
Traditional Class:
{'id': 101, 'name': 'Teja', 'marks': 85.5}

Dataclass Student:
StudentData(id=102, name='Ravi', marks=90.0)

Dataclass Employee:
Employee(id=201, name='Kiran', salary=50000.0)
```

## Comparison

| Feature | Traditional Class | Dataclass |
|---|---|---|
| Constructor | Written manually | Generated automatically |
| `__repr__()` | Manual if required | Generated automatically |
| `__eq__()` | Manual if required | Generated automatically |
| Code length | More | Less |
| Readability | More boilerplate | Cleaner |
| Type hints | Optional | Commonly used |

## Advantages of Dataclasses

- Less boilerplate code.
- Automatic constructor.
- Automatic readable representation.
- Automatic equality comparison.
- Easy to use for data-focused models.

## Conclusion

Dataclasses provide a shorter and cleaner way to implement classes that mainly store data. Traditional classes are still useful when more customized behavior is required.

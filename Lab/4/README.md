# List-Based vs Generator-Based Processing

## Objective

Compare list-based and generator-based processing for a large dataset in terms of execution time and memory usage.

## Algorithm

### List-Based Processing

1. Create a large list containing the dataset.
2. Process all elements and store the results in another list.
3. Measure execution time.
4. Measure peak memory usage.

### Generator-Based Processing

1. Create a generator that produces one value at a time.
2. Process values as they are generated.
3. Measure execution time.
4. Measure peak memory usage.
5. Compare the results with list-based processing.

## Program

The Python implementation is provided in:

`List_vs_Generator_Processing.ipynb`

## Comparison

| Feature | List | Generator |
|---|---|---|
| Data storage | Stores all elements | Produces elements one at a time |
| Memory usage | High | Low |
| Processing | Eager | Lazy |
| Random access | Supported | Not directly supported |
| Large datasets | Requires more memory | Memory efficient |

## Complexity

For `N` elements:

### List-Based Processing

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

### Generator-Based Processing

- Time Complexity: **O(N)**
- Extra Space Complexity: **O(1)**

## Expected Observation

The exact execution time and memory usage depend on the computer running the program.

Generally:

- List-based processing uses significantly more memory because the data and results are stored in memory.
- Generator-based processing uses much less memory because values are produced one at a time.
- Generator processing can have some execution overhead, but it is very useful for large datasets.

## Conclusion

Lists are useful when the complete dataset must be stored and accessed multiple times. Generators are more memory efficient and are suitable for processing large datasets sequentially or streaming data.

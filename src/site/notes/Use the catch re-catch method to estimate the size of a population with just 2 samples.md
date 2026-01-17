---
{"dg-publish":true,"permalink":"/use-the-catch-re-catch-method-to-estimate-the-size-of-a-population-with-just-2-samples/","tags":[null,null,null,null,null],"created":"2025-10-23T17:42:44.070+01:00","updated":"2025-10-30T23:44:53.583+00:00"}
---




- Have a team sample X data points and tag them with an ID
- Have the team later take a second sample Y and record how many have a tag Z

Whilst originally used for ecology to count population numbers, you can also use it to estimate really any population, you just have to be able to sample that population twice and compare the overlap.
```python
def estimate_population_size(initially_marked, captured_second, recaptured_marked):
    """
    Estimate the population size using the catch-recatch method.
    
    Args:
        initially_marked (int): The number of individuals marked in the first capture.
        captured_second (int): The total number of individuals captured in the second sample.
        recaptured_marked (int): The number of marked individuals recaptured in the second sample.
    
    Returns:
        int: The estimated population size.
    """
    N = initially_marked * captured_second / recaptured_marked
    return int(N)

# Example usage

initially_marked = 50 # First capture: 50 fish are marked and released
captured_second = 60 # Second capture: 60 fish are caught
recaptured_marked = 15 # We find that 15 are marked

estimated_population = estimate_population_size(initially_marked, captured_second, recaptured_marked)
print(f"The estimated population size is: {estimated_population}")
```
## Assumptions
- The population is closed so does not change during the study
- Marked and unmarked individuals have an equal chance of being captured in the second sample
- Marks are not lost or overlooked

# AI suggested related notes

These notes appear semantically similar based on Smart Connections embeddings:

- [[Citations/35-150 billion fish are raised in captivity to be released into the wild every year (Rethink Priorities)\|35-150 billion fish are raised in captivity to be released into the wild every year (Rethink Priorities)]] (similarity: 40.6%)
- [[Citations/Abundance Estimates of Three Wild Populations (Rethink Priorities)\|Abundance Estimates of Three Wild Populations (Rethink Priorities)]] (similarity: 39.9%)
- [[Bryant Confidential/A sampling strategy to maximise representativeness and sub group analysis\|A sampling strategy to maximise representativeness and sub group analysis]] (similarity: 37.7%)

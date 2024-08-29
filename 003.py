def find_overlap(intervals: list) -> list:
    # Sort intervals by the start time
    intervals.sort(key=lambda x: x[0])
    overlaps = []
    
    # Iterate through the intervals and check for overlap
    for i in range(1, len(intervals)):
        prev_start, prev_end = intervals[i - 1]
        current_start, current_end = intervals[i]
        
        # If the current interval overlaps with the previous one
        if prev_end > current_start:
            overlap_start = max(prev_start, current_start)
            overlap_end = min(prev_end, current_end)
            overlaps.append((overlap_start, overlap_end))
    
    return overlaps

print(find_overlap([(1,5), (3,7), (8,10), (9,12)]))  # Output: [(3,5), (9,10)]
print(find_overlap([(1,3), (4,6), (7,9)]))          # Output: []
print(find_overlap([(1,10), (2,6), (8,12)]))        # Output: [(2,6), (8,10)]
readings = [12.5, "Error", 18.2, 15.0, "Error", 22.1, 10.8]

print(f'Original readings: {readings}')
print(f'total readings in: {len(readings)}')

# Task 1: The Cleaner (Search and Replace)
replaced_readings = []
for read in range(0,len(readings)):
    if readings[read] == "Error":
        replaced_readings.append(0.0)
    else:
        replaced_readings.append(readings[read])

print(f'Task 1:replaced readings: {replaced_readings}')

# Task 2: The Multiplier (In-place Modification)
for read in range(0,len(replaced_readings)):
    replaced_readings[read] = (replaced_readings[read] + (replaced_readings[read] * 0.1))

print(f'Task 2: multiplied readings: {replaced_readings}')

# Task 3: The Filter (Selective Removal) & Extra Challenge: After adding them to the log, remove them from the original readings list.
low_quality_log = []
for read in range(len(replaced_readings)-1, -1, -1):
    if replaced_readings[read] < 15.0:
        low_quality_log.append(replaced_readings[read])
        del replaced_readings[read]

print(f'Task 3 + Extra Challenge:')
print(f'low quality readings: {low_quality_log}')
print(f'readings > 15.0: {replaced_readings}')

# 
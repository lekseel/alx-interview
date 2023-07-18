#!/usr/bin/env python3

import sys

# Initialize variables
total_size = 0
status_codes = {}

try:
    # Read stdin line by line
    for i, line in enumerate(sys.stdin, 1):
        # Parse the line
        parts = line.split()
        if len(parts) != 7:
            continue

        ip_address, _, _, status_code, file_size = parts[0], parts[3], parts[5], int(parts[6])

        # Update total file size
        total_size += file_size

        # Update status code count
        if status_code.isdigit():
            status_code = int(status_code)
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

        # Print statistics every 10 lines
        if i % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes):
                print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    # Handle keyboard interruption
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")

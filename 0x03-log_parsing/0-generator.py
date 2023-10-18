import sys

total_size = 0
lines_count = 0
status_count = {}

def print_stats():
    print("Total file size: {}".format(total_size))
    print("Number of lines by status code:")
    for status_code in sorted(status_count.keys()):
        print("{}: {}".format(status_code, status_count[status_code]))

for line in sys.stdin:
    lines_count += 1
    line = line.strip()
    fields = line.split()

    if len(fields) != 8 or fields[4] != "\"GET" or fields[6] != "HTTP/1.1\"":
        continue

    file_size = int(fields[7])
    total_size += file_size

    status_code = int(fields[5])
    if status_code not in status_count:
        status_count[status_code] = 0
    status_count[status_code] += 1

    if lines_count % 10 == 0:
        print_stats()
        print("\n")

try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    pass

print_stats()

def process_data(data):
    return [item * 2 for item in data]


def filter_data(data, threshold):
    return [item for item in data if item > threshold]


def sort_data(data):
    return sorted(data)


def calculate_average(data):
    return sum(data) / len(data) if data else 0


def main():
    sample_data = [1, 2, 3, 4, 5]
    processed = process_data(sample_data)
    filtered = filter_data(processed, 5)
    sorted_data = sort_data(filtered)
    average = calculate_average(sorted_data)
    print(f"Processed: {processed}, Filtered: {filtered}, Sorted: {sorted_data}, Average: {average}")


if __name__ == '__main__':
    main()
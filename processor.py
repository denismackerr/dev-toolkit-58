import json
from validators import validate_input

def process_data(data):
    try:
        validated_data = validate_input(data)
        # Process validated data
        result = sum(validated_data)
        return result
    except ValueError as e:
        return str(e)

def main():
    data_input = input('Enter numbers separated by commas: ')
    data_list = data_input.split(',')
    try:
        data = [float(num.strip()) for num in data_list]
        result = process_data(data)
        print('Result:', result)
    except ValueError:
        print('Invalid input: Please enter valid numbers.')

if __name__ == '__main__':
    main()
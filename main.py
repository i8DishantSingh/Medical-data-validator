import data as dt
import re

medical_data = dt.medical_reports


def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print('Invalid format: expected a list or tuple')
        return False
    
    is_invalid = False
    key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
    if is_invalid:
        return False
    print('Valid format.')
    return True



validate(medical_data)


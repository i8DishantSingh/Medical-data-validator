import data as dt
import re

medical_data = dt.medical_reports

def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):

    constraints = {
        'patient_id': isinstance(patient_id, str) and re.fullmatch(r'p\d+', patient_id, re.IGNORECASE),
        'age': isinstance(age, int) and age >= 18,
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        'medications': isinstance(medications, list) and all([isinstance(i, str) for i in medications]),
        'last_visit_id': isinstance(last_visit_id, str)and re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE)
    }
    return [key for key, value in constraints.items() if not value]



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
            
            invalid_records = find_invalid_records(**dictionary)
            for i in invalid_records:
                print(f"Unexpected format '{i}: {dictionary[i]}' at postition {index}")
                is_invalid = True


    if is_invalid:
        print('Invalid Data')
        return False
        
    print('Valid format.')
    return True



validate(medical_data)


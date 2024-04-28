def process_string_to_list(input_string):
    """Convert the input string to a list of integers based on character positions,
       where 'a' is 1, 'z' is 26, and '_' is 0."""
    converted_list = []
    i = 0
    n = len(input_string)
    while i < n:
        if 'a' <= input_string[i] <= 'z':
            num_chars_to_consider = ord(input_string[i]) - ord('a') + 1
            converted_list.append(num_chars_to_consider)
            i += 1
        elif input_string[i] == '_':
            converted_list.append(0)
            i += 1
    return converted_list

def combine_consecutive_26s(converted_list):
    """Combine all consecutive 26s in the list with the next non-26 value."""
    combined_list = []
    i = 0
    while i < len(converted_list):
        if converted_list[i] == 26:
            sum_26 = 0
            while i < len(converted_list) and converted_list[i] == 26:
                sum_26 += converted_list[i]
                i += 1
            if i < len(converted_list):
                sum_26 += converted_list[i]
            combined_list.append(sum_26)
            i += 1  # Increment to skip the next element already added to sum_26
        else:
            combined_list.append(converted_list[i])
            i += 1
    return combined_list

def process_list(input_string):
    """Process the input string to combine consecutive 26s with the next value."""
    converted_list = process_string_to_list(input_string)
    combined_list = combine_consecutive_26s(converted_list)
    return combined_list

def create_result(input_string):
    if input_string.startswith('_'):
        return [0]  

    combined_list = process_list(input_string)
    results = []
    i = 0  

    while i < len(combined_list):
        count = combined_list[i] if i < len(combined_list) else 0  
        sum_sequence = 0  
        if count > 0 and i + 1 < len(combined_list):

            sum_sequence = sum(combined_list[i + 1:i + 1 + count])
        
        results.append(sum_sequence)
        i += count + 1  

        if i >= len(combined_list) and (count == 0 or i + 1 >= len(combined_list)):
            break

    return results


# Test the full processing function
print(create_result('abbcc'))
print(create_result('dz_a_aazzaaa'))
print(create_result('a_'))
print(create_result('abcdabcdab'))
print(create_result('abcdabcdab_'))
print(create_result('zdaaaaaaaabaaaaaaaabaaaaaaaabbaa'))
print(create_result('zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_'))
print(create_result('za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa'))
print(create_result('_a'))
print(create_result('_'))
print(create_result('_ad'))
print(create_result('_zzzb'))
print(create_result('__'))

import sys

def calculate_key(key_number):
    first_letter_range = [chr(i) for i in range(ord('c'), ord('m') + 1)]
    second_number_range = [str(i) for i in range(10)] # 0-9
    third_letter_range = [chr(i) for i in range(ord('f'), ord('z') + 1)]
    fourth_number_range = [str(i) for i in range(2, 8)] # 2-7
    fifth_number_range = [str(i) for i in range(1, 6)] # 1-5
    
    total_keys = len(first_letter_range) * len(second_number_range) * (len(third_letter_range) ** 2) * len(fourth_number_range) * len(fifth_number_range)
    
    if key_number >= total_keys:
        return "Key number is out of range"
    
    remainder = key_number
    first_letter_index = remainder // (len(second_number_range) * (len(third_letter_range) ** 2) * len(fourth_number_range) * len(fifth_number_range))
    remainder %= (len(second_number_range) * (len(third_letter_range) ** 2) * len(fourth_number_range) * len(fifth_number_range))
    
    second_number_index = remainder // ((len(third_letter_range) ** 2) * len(fourth_number_range) * len(fifth_number_range))
    remainder %= ((len(third_letter_range) ** 2) * len(fourth_number_range) * len(fifth_number_range))
    
    third_letter_first_index = remainder // (len(third_letter_range) * len(fourth_number_range) * len(fifth_number_range))
    remainder %= (len(third_letter_range) * len(fourth_number_range) * len(fifth_number_range))
    
    third_letter_second_index = remainder // (len(fourth_number_range) * len(fifth_number_range))
    remainder %= (len(fourth_number_range) * len(fifth_number_range))
    
    fourth_number_index = remainder // len(fifth_number_range)
    fifth_number_index = remainder % len(fifth_number_range)

    key = (first_letter_range[first_letter_index] + 
           second_number_range[second_number_index] + 
           third_letter_range[third_letter_first_index] + 
           third_letter_range[third_letter_second_index] + 
           fourth_number_range[fourth_number_index] + 
           fifth_number_range[fifth_number_index])
    
    return key

key = calculate_key(585936)
print("UiTHack{" + key + "}")

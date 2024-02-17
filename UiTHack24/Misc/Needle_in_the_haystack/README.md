# Needle in the Haystack
While walkin around in the home base a soldier comes running up to you.

THE KEY LIST, WE LOST IT!

After calming him down he starts to explain in more detail:

Every day the enemy broadcasts an unencrypted message saying which key to use from the list. In secret we managed to steal a copy of the list, but it has now been lost. We know the pattern of the list, but manually writing it out would take years. You must help us solve this problem.

The pattern is:

1 letter between "c" and "m" - 1 digit - 2 letters between "f" and "z" - 1 number between 2 and 7 - 1 number between 1 and 5
I remember key number 0 and 1 were c0ff21 and c0ff22 respectively.

and the correct key today is key number 585937

The flag will be in the form "UiTHack24{insert key}"

## Løsning
I denne oppgaven får vi mønsteret beskrevet ganske godt, og vi må lage en liste over alle kombinasjonene for å finne svaret. Her lagde jeg et python script med alle reglene og hentet koden.

```python
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

>> UiTHack{g4lg32}
```
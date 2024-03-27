# The script from the decoded message prints characters at positions that are perfect cubes.
# To follow this logic, let's extract characters from the decoded_message at positions that are perfect cubes.

# Initialize the variable to keep track of perfect cubes and the final message
with open("new.py", "r") as f:
    decoded_message = f.read()

b = 1
perfect_cube_message = ""

# Iterate through the length of the decoded message
for i in range(len(decoded_message)):
    # Check if the current index is a perfect cube
    if i == b ** 3:
        perfect_cube_message += decoded_message[i]
        b += 1

print(perfect_cube_message)

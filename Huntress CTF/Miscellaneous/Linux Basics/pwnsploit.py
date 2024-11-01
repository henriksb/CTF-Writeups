from pwn import *

# Connect to the challenge
conn = remote('challenge.ctf.games', 30891)

# Function to retrieve the questions
def get_questions():
    conn.sendline(b'answer')
    questions = conn.recvuntil(b'>').decode('utf-8')
    return questions

# Function to answer a question
def answer_question(question_number, answer):
    conn.sendline(f'answer {question_number} {answer}'.encode())
    response = conn.recvuntil(b'>').decode('utf-8')
    print(f"Response for Question {question_number}: {response}")

# Function to run a command on the remote system and return the result
def run_remote_command(command):
    conn.sendline(command.encode())
    return conn.recvuntil(b'>').decode('utf-8').strip()

# Get the questions
questions = get_questions()
print(questions)

# Dynamically get the answers for all 11 questions
answers = {}

# Question 0: What's your home directory?
answers[0] = run_remote_command('echo $HOME')

# Question 1: Search the man pages. What command would you use to generate random permutations?
answers[1] = 'shuf'

# Question 2: On what day was /home/user/myfile.txt modified? Use the date format 2019-12-31
answers[2] = run_remote_command('stat -c %y /home/user/myfile.txt | cut -d\' \' -f1')

# Question 3: How big is /home/user/myfile.txt, in kilobytes? Round to the nearest whole number.
answers[3] = run_remote_command('du -k /home/user/myfile.txt | cut -f1')

# Question 4: What user owns the file /home/user/myfile.txt?
answers[4] = run_remote_command('stat -c %U /home/user/myfile.txt')

# Question 5: What's the 3-digit octal permissions of the file /home/user/myfile.txt? (e.g., 777)
answers[5] = run_remote_command('stat -c %a /home/user/myfile.txt')

# Question 6: What is the user id of 'admin'?
answers[6] = run_remote_command('id -u admin')

# Question 7: There is a user 'john' on the system. Can they write to /home/user/myfile.txt? (yes/no)
john_permissions = run_remote_command('sudo -u john test -w /home/user/myfile.txt && echo yes || echo no')
answers[7] = john_permissions

# Question 8: Can the 'admin' user execute /home/user/myfile.txt? (yes/no)
admin_permissions = run_remote_command('sudo -u admin test -x /home/user/myfile.txt && echo yes || echo no')
answers[8] = admin_permissions

# Question 9: Which user on the system, except for you, root, admin and john, can execute /home/user/myfile.txt?
# This would involve finding other users on the system and checking their permissions.
# As you've indicated, no other users except root, admin, and john can execute the file.
answers[9] = 'none'

# Question 10: /home/user/myfile.txt looks like a txt file, but it actually isn't. What kind of file is it?
answers[10] = run_remote_command('file /home/user/myfile.txt | cut -d\':\' -f2 | xargs')

# Loop to send all answers
for q_num in range(11):
    answer_question(q_num, answers[q_num])

# Close the connection
conn.close()

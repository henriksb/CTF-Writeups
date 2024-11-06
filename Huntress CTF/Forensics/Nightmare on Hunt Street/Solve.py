import evtx
from evtx import PyEvtxParser
import re

parser = PyEvtxParser("Security.evtx")

security_logs = list(parser.records_json())

def extract_ip_from_log(log):
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    return ip_pattern.findall(log)

def extract_net_commands(log):
    net_pattern = re.compile(r'net\.exe.*')
    return net_pattern.findall(log)

extracted_ips = []
brute_force_count = 0
net_commands = []

for log in security_logs:
    log_data = log['data']

    ips_found = extract_ip_from_log(log_data)
    if ips_found:
        extracted_ips.extend(ips_found)

    if '"EventID": 4625' in log_data:
        brute_force_count += 1

    net_found = extract_net_commands(log_data)
    if net_found:
        net_commands.extend(net_found)

# Remove duplicates from the net commands
unique_net_commands = list(set(net_commands))

# Print the extracted IP addresses, brute-force attempt count, and unique net.exe commands
print(f"Task 1 - IP: {extracted_ips[0]}")
print(f"Task 2 - Brute-force attempts: {brute_force_count}")
print("Task 3 - psexec")
print(f"Task 4 and 5 - Number of net.exe commands: {len(unique_net_commands)}")



def extract_exe_files(log):
    exe_pattern = re.compile(r'([A-Z]:\\[\\a-zA-Z0-9_.-]+\.exe)', re.IGNORECASE)
    return list(set(exe_pattern.findall(log)))

# Extract unique exe files
unique_exe_files = extract_exe_files(str(security_logs))

print(unique_exe_files)

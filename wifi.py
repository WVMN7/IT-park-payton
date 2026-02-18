import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1].strip() for i in data if "All User Profile" in i]

for profile in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        password = [b.split(":")[1].strip() for b in results if "Key Content" in b]

        print(f"{profile:<30}|  {password[0] if password else 'None'}")
    except subprocess.CalledProcessError:
        print(f"{profile:<30}|  Error")

input("\n\nPress Enter to continue...")
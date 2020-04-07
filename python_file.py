import subprocess

with open('output.txt', 'w') as f:
    value = input("Please enter the domain name:\n")
    print(subprocess.run(['amass.exe', 'enum', '-active', '-d', value], stdout=f, text=True, shell=True))
    print(subprocess.run(['amass.exe', 'enum',  '-passive', '-d', value], stdout=f, text=True, shell=True))
    print(subprocess.run(['amass.exe', 'enum',  '-active', '-brute', '-d', value], stdout=f, text=True, shell=True))
    print(subprocess.run(['amass.exe', 'enum', '-d', value], stdout=f, text=True, shell=True))



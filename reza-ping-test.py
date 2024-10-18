import subprocess

def ping_test():
    result = subprocess.run(['ping', '-c','5','google.com'],capture_output=True, text=True)
    print(result.stdout)
ping_test()

import subprocess  
import time  

def ping_test(remote_server):  
    print(f"Pinging {remote_server}...\n")  
    try:  
        # Execute the ping command with a timeout of 5 seconds  
        result = subprocess.run(  
            ["ping", "-c", "5", remote_server],  
            capture_output=True,  
            text=True,  
            timeout=5  # This will stop after 5 seconds  
        )  
        
        # Output the results  
        print(result.stdout)  
        
        # Check for errors in the result  
        if result.returncode != 0:  
            print(f"Ping failed: {result.stderr}")  
        
    except subprocess.TimeoutExpired:  
        print("Ping command timed out.")  
    except Exception as e:  
        print(f"Error executing ping: {e}") 




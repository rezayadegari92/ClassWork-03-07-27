def throughput_test(file_url):  
    print(f"Testing download speed from {file_url}...\n")  
    try:  
        # Execute the curl command to measure download speed  
        start_time = time.time()  
        result = subprocess.run(  
            ["curl", "-o", "/dev/null", "-w", "%{size_download} bytes downloaded in %{time_total} seconds\n", file_url],  
            capture_output=True,  
            text=True  
        )  
        
        # Calculate throughput  
        if result.returncode == 0:  
            size_downloaded = int(result.stdout.split()[0])  # Get the size in bytes  
            time_taken = float(result.stdout.split()[3])    # Get the time in seconds  
            throughput = size_downloaded / time_taken       # Throughput in bytes/sec  

            print(result.stdout)  
            print(f"Throughput: {throughput:.2f} bytes/sec")  
        else:  
            print(f"Download failed: {result.stderr}")  

    except Exception as e:  
        print(f"Error executing throughput test: {e}")  

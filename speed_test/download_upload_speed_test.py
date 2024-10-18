# import subprocess
# import re
# import speedtest
#
# def test_speed_with_subprocess():
#     try:
#         # Run the speedtest-cli command using subprocess
#         result = subprocess.run(["speedtest-cli", "--simple"], capture_output=True, text=True)
#         output = result.stdout
#
#         # Output is something like:
#         # Ping: 12.34 ms
#         # Download: 123.45 Mbit/s
#         # Upload: 23.45 Mbit/s
#
#         # Use regular expressions to extract ping, download, and upload speeds
#         ping = re.search(r"Ping:\s+(\d+\.\d+)\s+ms", output)
#         download = re.search(r"Download:\s+(\d+\.\d+)\s+Mbit/s", output)
#         upload = re.search(r"Upload:\s+(\d+\.\d+)\s+Mbit/s", output)
#
#         # Extract the values if they are found
#         ping_value = ping.group(1) if ping else "Unknown"
#         download_speed = download.group(1) if download else "Unknown"
#         upload_speed = upload.group(1) if upload else "Unknown"
#
#         # Display the results
#         print(f"Ping: {ping_value} ms")
#         print(f"Download Speed: {download_speed} Mbit/s")
#         print(f"Upload Speed: {upload_speed} Mbit/s")
#
#     except Exception as e:
#         print(f"Error running speedtest: {e}")
#
# # Run the speed test
# test_speed_with_subprocess()

import speedtest

def test_speed():
    try:
        # Create a Speedtest object
        st = speedtest.Speedtest()

        # Fetch the list of servers and select the best one
        st.get_best_server()

        print("Testing download speed...")
        download_speed = st.download()  # Download speed in bits per second (bps)
        print("Testing upload speed...")
        upload_speed = st.upload()  # Upload speed in bits per second (bps)

        # Convert from bps to Mbps for readability
        download_speed_mbps = download_speed / 1_000_000  # Convert to Mbps
        upload_speed_mbps = upload_speed / 1_000_000  # Convert to Mbps

        print(f"Download Speed: {download_speed_mbps:.2f} Mbps")
        print(f"Upload Speed: {upload_speed_mbps:.2f} Mbps")

    except Exception as e:
        print(f"Error testing speed: {e}")

test_speed()



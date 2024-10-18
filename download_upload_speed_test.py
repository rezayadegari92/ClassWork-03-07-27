import speedtest

def test_speed():
    try:
        # Create a Speedtest object
        st = speedtest.Speedtest()
        best_server = st.get_best_server()
        # st.get_servers([best_server])

        print(f"test speed with server {best_server['sponsor'],best_server['name'],best_server['country']}")


        print("Testing download speed...")
        download_speed = st.download() # Download speed in bits per second (bps)
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



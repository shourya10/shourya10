import speedtest

def run_speedtest():
    # Create a Speedtest object
    st = speedtest.Speedtest()

    # Get the best server based on ping
    st.get_best_server()

    # Perform download and upload speed tests
    download_speed = st.download() / 1_000_000  # Convert from bits/s to Mbits/s
    upload_speed = st.upload() / 1_000_000     # Convert from bits/s to Mbits/s
    ping_result = st.results.ping              # Get ping

    # Print results
    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping_result} ms")

if __name__ == "__main__":
    run_speedtest()

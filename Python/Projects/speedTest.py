from speedtest import Speedtest

wifi = Speedtest()

print("Getting Download Speed...")

download = wifi.download()
print(f"Download: {download / 1024 / 1024:.2f} mbps")

print()
print("Getting Upload Speed...")

upload = wifi.upload()
print(f"Upload: {upload / 1024 / 1024:.2f} mbps")

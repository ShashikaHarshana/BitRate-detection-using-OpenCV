# from scapy.all import sniff
# import time
#
# esp32_ip = "192.168.4.1"  # Replace with the IP address of your ESP32
# video_port = 80  # Replace with the port number used for the video stream
#
# # Define a packet filter to capture only packets from the ESP32 and the video port
# packet_filter = f"src host {esp32_ip} and tcp port {video_port}"
#
#
# # Define a function to calculate the bitrate
# def calculate_bitrate(duration):
#     # Initialize variables for calculating bitrate
#     bit_count = 0
#     start_time = time.time()
#
#     # Define a custom callback function to process each captured packet
#     def packet_callback(packet):
#         nonlocal bit_count
#
#         # Get the size of the packet payload in bytes
#         packet_size = len(packet.payload)
#
#         # Update the total bit count
#         bit_count += packet_size * 8
#
#     # Start capturing packets using the filter and the callback function for the specified duration
#     sniff(filter=packet_filter, prn=packet_callback, timeout=duration)
#
#     # Calculate the elapsed time and the bitrate
#     elapsed_time = time.time() - start_time
#     bitrate = bit_count / elapsed_time / 1000  # Convert to Kbps
#
#     return bitrate
#
#
# # Calculate the bitrate 10 times and print the value each time
# for i in range(10):
#     bitrate = calculate_bitrate(1)  # Capture packets for 1 second
#     print("Bitrate:", round(bitrate, 2), "Kbps")
#-------------------------------------------------------------------------

from scapy.all import sniff
import time

esp32_ip = "192.168.4.1"  # Replace with the IP address of your ESP32
video_port = 80  # Replace with the port number used for the video stream

# Define a packet filter to capture only packets from the ESP32 and the video port
packet_filter = f"src host {esp32_ip} and tcp port {video_port}"

# Define a function to calculate the bitrate and FPS
def calculate_bitrate_and_fps(duration):
    # Initialize variables for calculating bitrate and FPS
    bit_count = 0
    frame_count = 0
    start_time = time.time()

    # Define a custom callback function to process each captured packet
    def packet_callback(packet):
        nonlocal bit_count, frame_count

        # Get the size of the packet payload in bytes
        packet_size = len(packet.payload)

        # Update the total bit count
        bit_count += packet_size * 8

        # Update the frame count
        frame_count += 1

    # Start capturing packets using the filter and the callback function for the specified duration
    sniff(filter=packet_filter, prn=packet_callback, timeout=duration)

    # Calculate the elapsed time, bitrate, and FPS
    elapsed_time = time.time() - start_time
    bitrate = bit_count / elapsed_time / 1000  # Convert to Mbps
    fps = frame_count / elapsed_time

    return bitrate, fps

# Calculate the bitrate and FPS 10 times and print the values each time
for i in range(10):
    bitrate, fps = calculate_bitrate_and_fps(1)  # Capture packets for 1 second
    print("Bitrate:", round(bitrate,2), "Kbps", "FPS:", round(fps))


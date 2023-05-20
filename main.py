import sys
import time
import os
import cv2
import argparse

parser = argparse.ArgumentParser(description='Bitrate monitor')
parser.add_argument('--url', type=str, help='URL of the video feed')
parser.add_argument('--count', type=int, help='Number of bitrate measurements')
args = parser.parse_args()
video_feed_url = args.url
measurements_limit = args.count

def calculate_fps(start_time, fps_avg_frame_count):
    end_time = time.time()
    fps = fps_avg_frame_count / (end_time - start_time)
    return fps


def get_color_depth(video_format):
    # Determine the color depth based on the format
    if video_format == cv2.CV_8U:
        color_depth = 8
    elif video_format == cv2.CV_16U:
        color_depth = 16
    elif video_format == cv2.CV_32F:
        color_depth = 32
    else:
        color_depth = None

    return color_depth

def run():
    # variables to calculate Fps
    counter, print_counter, fps = 0, 0, 0
    start_time = time.time()
    fps_avg_frame_count = 10

    cap = cv2.VideoCapture(video_feed_url)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            sys.exit(
                'ERROR: Unable to read from webcam. Please verify your webcam settings.'
            )
        # get resolution of the camera feed.
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # Get the format of the video frames
        video_format = cap.get(cv2.CAP_PROP_FORMAT)

        color_depth = get_color_depth(video_format)

        counter += 1
        # calculate Fps
        if counter % fps_avg_frame_count == 0:
            fps = calculate_fps(start_time, fps_avg_frame_count)
        start_time = time.time()
        bit_rate = int(height) * int(width) * int(color_depth) * round(fps, 0)

        if counter % 10 == 0:
            print(bit_rate)
            print_counter += 1

        # press esc to close the window
        if print_counter == measurements_limit:
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    run()

if __name__ == '__main__':
    main()
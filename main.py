import sys
import time
import os
import cv2

im = None


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


# def get_node_name():
#     # Load the Kubernetes configuration
#     config.load_incluster_config()
#
#     # Create the Kubernetes API client
#     api_instance = client.CoreV1Api()
#
#     # Get the name of the current pod
#     pod_name = os.environ['HOSTNAME']
#
#     # Get the namespace of the current pod
#     namespace = open('/var/run/secrets/kubernetes.io/serviceaccount/namespace').read()
#
#     # Get the pod object
#     pod = api_instance.read_namespaced_pod(name=pod_name, namespace=namespace)
#
#     # Get the name of the node where the pod is running
#     node_name = pod.spec.node_name
#
#     # Set the node name as an environment variable
#     os.environ['NODE_NAME'] = node_name
#
#     print(os.environ['NODE_NAME'])


def run():
    # variables to calculate Fps
    counter, print_counter, fps = 0, 0, 0
    start_time = time.time()
    fps_avg_frame_count = 10

    cap = cv2.VideoCapture('http://10.10.49.224:6677/videofeed?username=&password=')

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

        # live stream
        # cv2.imshow('streaming', image)
        # cv2.imshow('live', image)

        # press esc to close the window
        if print_counter == 10:
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    run()


if __name__ == '__main__':
    main()

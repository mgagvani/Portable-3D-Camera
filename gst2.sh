#!/bin/sh

export GST_V4L2_USE_LIBV4L2=1

gst-launch-1.0 -vvv -e v4l2src ! videoscale ! video/x-raw,width=656,height=192 ! autovideosink
#gst-launch-1.0 -vvv -e v4l2src ! videobox ! video/x-raw,width=960,height=270 ! omxh264enc ! h264parse ! mp4mux ! filesink location=out.mp4
#gst-launch-1.0 -vvv -e v4l2src ! videoscale ! video/x-raw,width=1104,height=312 ! omxh264enc !  filesink location=out.mp4
#gst-launch-1.0 -vvv -e v4l2src ! videoscale ! video/x-raw,width=960,height=270,framerate=30/1 ! omxh264enc  !  filesink location=out.mp4
#gst-launch-1.0 -vvv -e v4l2src ! videoscale ! video/x-raw,width=960,height=272,framerate=30/1 ! omxh264enc control-rate=1 target-bitrate=1000000  !  filesink location=out.mp4
#gst-launch-1.0 -vvv -e v4l2src ! videoscale ! video/x-raw,width=960,height=272,framerate=30/1 ! omxh264enc control-rate=1 target-bitrate=1000000  !  h264parse ! matroskamux ! filesink location=out.mkv
#gst-launch-1.0 -vvv -e v4l2src ! videoscale ! video/x-raw,width=1920,height=544,framerate=30/1 ! omxh264enc control-rate=1 target-bitrate=2000000  !  h264parse ! matroskamux ! filesink location=out.mkv

# two branches
#gst-launch-1.0 -vvv -e v4l2src ! tee name=t t. ! queue ! videoscale ! video/x-raw,width=656,height=192 ! autovideosink t. ! queue ! videoscale ! video/x-raw,width=3840,height=1080,framerate=30/1 ! omxh264enc control-rate=1 target-bitrate=3000000 ! h264parse ! matroskamux ! filesink  location=out.mkv

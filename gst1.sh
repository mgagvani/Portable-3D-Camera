#!/bin/sh

gst-launch-1.0 -vvv -e v4l2src ! videoscale ! textoverlay text="Rec"  font-desc="Sans,72" !  video/x-raw,width=1104,height=313 ! autovideosink
#gst-launch-1.0 -vvv -e v4l2src brightness=0 ! videoscale ! video/x-raw,width=1104,height=313 ! autovideosink
#gst-launch-1.0 -vvv -e v4l2src ! videobox ! video/x-raw,width=960,height=270 ! omxh264enc ! h264parse ! mp4mux ! filesink location=out.mp4
#gst-launch-1.0 -vvv -e v4l2src ! videoscale ! video/x-raw,width=1104,height=312 ! omxh264enc !  filesink location=out.mp4
#gst-launch-1.0 -vvv -e v4l2src ! videoscale ! video/x-raw,width=960,height=270,framerate=30/1 ! omxh264enc  !  filesink location=out.mp4
#gst-launch-1.0 -vvv -e v4l2src ! videoscale ! video/x-raw,width=960,height=272,framerate=30/1 ! omxh264enc control-rate=1 target-bitrate=1000000  !  filesink location=out.mp4
#gst-launch-1.0 -vvv -e v4l2src ! videoscale ! video/x-raw,width=960,height=272,framerate=30/1 ! omxh264enc control-rate=1 target-bitrate=1000000  !  h264parse ! matroskamux ! filesink location=out.mkv
#gst-launch-1.0 -vvv -e v4l2src ! videoscale ! video/x-raw,width=1920,height=544,framerate=30/1 ! omxh264enc control-rate=1 target-bitrate=2000000  !  h264parse ! matroskamux ! filesink location=out.mkv

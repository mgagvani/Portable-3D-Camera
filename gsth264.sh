#!/bin/sh

##

# Capture video from V4L source, convert to H264 and display
##

# --- Settings
##

# Output file 
OUTPUT=$1

# capture device to use
V4LDEV="/dev/video0"

# capture width
WIDTH=2560

# capture height
HEIGHT=720

# bitrate for theoraenc
BITRATE=2000

##
# --- END of settings
##


if [ "X$1" = "X" ]
then
   OUTPUT="webcam.mp4"
fi

echo "**"
echo "* Starting recording from webcam@${V4LDEV} to: ${OUTPUT}@${WIDTH}x${HEIGHT}"
echo "* Using mp4-container and H.264-encoding with bitrate: ${BITRATE}" 
echo "* Press CTRL+C to end recording"
echo "**"

#
# -e switch makes gst to close the OGG container properly when exited with CTRL+C
#

gst-launch-1.0 -vvvv -e \
   v4l2src device=${V4LDEV} ! \
   #tee name="splitter" ! queue ! xvimagesink sync=false splitter. ! \
   #queue ! videoconvert ! \
   omxh264enc ! qtmux ! filesink location=${OUTPUT}

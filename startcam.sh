#!/bin/sh

~/zed/recdisp.sh & 

sleep 1
# Move the window to the correct position
winid=`xdotool search --onlyvisible --name gst-launch`
echo $winid
xdotool windowmove $winid 780 390 
xdotool windowsize $winid 686 240
xdotool windowraise $winid 

sudo ~/fbcp-ili9341/build/fbcp-ili9341 &

# Move the window to the correct position
winid=`xdotool search --onlyvisible --name gst-launch`
echo $winid
# Settings for 1080p
#xdotool windowmove $winid 780 390 
# settings for 1024x768 in virtual headless framebuffer mode
xdotool windowmove $winid 330 250
xdotool windowsize $winid 686 240
xdotool windowraise $winid 


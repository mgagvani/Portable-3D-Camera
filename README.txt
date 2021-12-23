# gst-launch is not installed.  

sudo apt-get install gstreamer1.0-tools

# Install the OpenMAX plugin for gstreamer which allows hardware encode

sudo apt-get install gst-omx-listcomponents 
sudo apt-get install gstreamer1.0-omx-generic 
sudo apt-get install gstreamer1.0-omx
sudo apt-get install gstreamer1.0-omx-rpi 
sudo apt-get install gstreamer1.0-omx-rpi-config

# You can list v4l2 capture devices using 

v4l2-ctl --list-devices

# Use gst-inspect-1.0  to list all plugins

# To use the v4l2src plugin, enable the env variable
export GST_V4L2_USE_LIBV4L2=1

# Use the SPI display library at https://github.com/juj/fbcp-ili9341
# follow instructions to install cmake, clone the repo and build it 

# cmake -DILI9341=ON -DGPIO_TFT_DATA_CONTROL=18 -DGPIO_TFT_RESET_PIN=23 -DSPI_BUS_CLOCK_DIVISOR=30 -DARMV8A=ON -DDISPLAY_CROPPED_INSTEAD_OF_SCALING=ON ..


#!/bin/bash

# Defines the directories the shell searches from
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Defines the working directory for this task
DIR="/home/fu_pi/csc1107_assignment_qn1"

# Log message
echo "usb inserted" >> "$DIR/usb_inserted.log"

# Change into working directory
cd "$DIR" || exit 1

# Compile and insert kernel module
/usr/bin/make >> "$DIR/make_output.log" 2>&1
sudo insmod hello_module.ko

# Wait for device node
sleep 1

# Compile user program
gcc -o user_program user_program.c

# Broadcast user_program message and last 20 lines of dmesg
{
 	echo "=== Output from user_program ===";
 	sudo ./user_program;
 	echo ""
	echo "=== Last 20 lines of dmesg ===";
  	dmesg | tail -n 20;
	echo ""
	echo "You can continue typing commands below."
} | wall

# Cleanup
sudo rmmod hello_module


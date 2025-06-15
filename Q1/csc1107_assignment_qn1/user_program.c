#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

#define DEVICE_PATH "/dev/hello_device"	// path to the device file

int main() {
	// open the device file with r/w permissions
    	int fd = open(DEVICE_PATH, O_RDWR);
    	if (fd < 0) {
        	perror("Failed to open device");	// print error if open fails
        	return 1;
    	}

    	// write a message to the device
    	const char *message = "Hello World from the user space";
    	write(fd, message, strlen(message)); // send message to kernel device

    	// read message from device
    	char buf[128];
    	ssize_t bytes = read(fd, buf, sizeof(buf) - 1); // read data from device
    	if (bytes >= 0) {
        	buf[bytes] = '\0';
        	printf("Hello World from the kernel space\n"); // print confirmation message

    	} else {
        	perror("Read failed");	// print error if read fails
    	}

	// close device file descriptor
    	close(fd);
    	return 0;
}

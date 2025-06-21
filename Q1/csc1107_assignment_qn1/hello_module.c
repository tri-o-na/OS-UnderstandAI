#include <linux/module.h>
#include <linux/fs.h>
#include <linux/uaccess.h>
#include <linux/device.h>
#include <linux/cdev.h>

#define DEVICE_NAME "hello_device"	// name of device to create (/dev/hello_device)
#define CLASS_NAME "hello_class"	// name of the device class
#define BUF_LEN 128			// buffer length for messages

static int major;	// major number for device created
static char kernel_buf[BUF_LEN] = "Hello World from the kernel space";	// string to print from kernel space
static struct class* hello_class = NULL;
static struct device* hello_device = NULL;

// function to handle reading from the device
static ssize_t device_read(struct file *file, char __user *buf, size_t len, loff_t *offset) {
	printk(KERN_INFO "device_read: returning message to user\n");
    	return simple_read_from_buffer(buf, len, offset, kernel_buf, strlen(kernel_buf));
}

// function to handle writing to the device
static ssize_t device_write(struct file *file, const char __user *buf, size_t len, loff_t *offset) {
    	printk(KERN_INFO "device_write: receiving message from user\n");
    	if (len > BUF_LEN) len = BUF_LEN;
    	if (copy_from_user(kernel_buf, buf, len)) return -EFAULT;
    	kernel_buf[len] = '\0';
    	printk(KERN_INFO "Received from user: %s\n", kernel_buf);
    	return len;
}

// file operations structure links system calls to functions
static struct file_operations fops = {
    	.read = device_read,
    	.write = device_write,
};

// called when the module is loaded into the kernel
static int __init hello_init(void) {
    	major = register_chrdev(0, DEVICE_NAME, &fops);
    	if (major < 0) {
        	printk(KERN_ALERT "Registering char device failed\n");
        	return major;
    	}

    	// create device class
    	hello_class = class_create(CLASS_NAME);
    	if (IS_ERR(hello_class)) {
        	unregister_chrdev(major, DEVICE_NAME);
        	printk(KERN_ALERT "Failed to register device class\n");
        	return PTR_ERR(hello_class);
    	}

	// create the device node
    	hello_device = device_create(hello_class, NULL, MKDEV(major, 0), NULL, DEVICE_NAME);
    	if (IS_ERR(hello_device)) {
        	class_destroy(hello_class);
        	unregister_chrdev(major, DEVICE_NAME);
        	printk(KERN_ALERT "Failed to create device\n");
        	return PTR_ERR(hello_device);
    	}

    	printk(KERN_INFO "Hello module loaded with major number %d\n", major);
    	return 0;
}

// called when the module is removed from kernel
static void __exit hello_exit(void) {
    	device_destroy(hello_class, MKDEV(major, 0));
    	class_unregister(hello_class);
    	class_destroy(hello_class);
    	unregister_chrdev(major, DEVICE_NAME);
    	printk(KERN_INFO "Hello module unloaded\n");
}

// register the init and exit functions
module_init(hello_init);
module_exit(hello_exit);

MODULE_LICENSE("GPL");

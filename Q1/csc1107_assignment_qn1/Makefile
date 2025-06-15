obj-m += hello_module.o

UNAME := /usr/bin/uname
MAKE := /usr/bin/make
KERNELVER := $(shell $(UNAME) -r)

all:
	$(MAKE) -C /lib/modules/$(KERNELVER)/build M=$(PWD) modules

clean:
	$(MAKE) -C /lib/modules/$(KERNELVER)/build M=$(PWD) clean


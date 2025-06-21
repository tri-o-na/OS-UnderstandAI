#include <linux/module.h>
#include <linux/export-internal.h>
#include <linux/compiler.h>

MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};



static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x122c3a7e, "_printk" },
	{ 0x98cf60b3, "strlen" },
	{ 0x619cb7dd, "simple_read_from_buffer" },
	{ 0xd75c6742, "__register_chrdev" },
	{ 0xf311fc60, "class_create" },
	{ 0x93ab9e33, "device_create" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0x4a41ecb3, "class_destroy" },
	{ 0xe095e43a, "device_destroy" },
	{ 0x77b39d3d, "class_unregister" },
	{ 0xdcb764ad, "memset" },
	{ 0x12a4e128, "__arch_copy_from_user" },
	{ 0x39ff040a, "module_layout" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "B1B5D8EEDAD802065DF41B2");

| file | line | keyword | match|
| --- | --- | --- | --- |
| kernel/arch\alpha\include\asm\string.h | 8 | stupid | * GCC of any recent vintage doesn't do stupid things with bcopy. |
| kernel/arch\alpha\kernel\process.c | 324 | stupid | /* Once upon a time this was the PS value.  Which is stupid |
| kernel/arch\alpha\lib\dbg_stackcheck.S | 25 | damn | 1:	stq	$31, -8($31)	# oops me, damn it. |
| kernel/arch\alpha\lib\ev6-stxcpy.S | 175 | stupid | /* Finally, we've got all the stupid leading edge cases taken care |
| kernel/arch\alpha\lib\ev6-stxncpy.S | 222 | stupid | /* Finally, we've got all the stupid leading edge cases taken care |
| kernel/arch\alpha\lib\stxcpy.S | 152 | stupid | /* Finally, we've got all the stupid leading edge cases taken care |
| kernel/arch\alpha\lib\stxncpy.S | 180 | stupid | /* Finally, we've got all the stupid leading edge cases taken care |
| kernel/arch\arm64\include\asm\spinlock.h | 19 | ass | * https://lore.kernel.org/lkml/20200110100612.GC2827@hirez.programming.kicks-ass.net |
| kernel/arch\arm64\kernel\syscall.c | 88 | stupid | * doing something stupid, such as setting PROT_BTI on a page |
| kernel/arch\arm64\kvm\arch_timer.c | 1602 | stupid | * vcpu. Yes this is late. Blame it on the stupid API. |
| kernel/arch\arm64\kvm\emulate-nested.c | 2094 | stupid | /* Yes, this is recursive. Don't do anything stupid. */ |
| kernel/arch\arm64\kvm\hypercalls.c | 60 | damn | * nobody will give a damn about it). |
| kernel/arch\arm64\kvm\mmu.c | 1860 | stupid | * or if the guest is just being stupid. The only thing |
| kernel/arch\arm64\kvm\mmu.c | 2193 | damn | * - System caches don't support S/W at all (damn!) |
| kernel/arch\arm64\kvm\vgic\vgic-irqfd.c | 126 | damn | * as long as the damn vgic is initialized. |
| kernel/arch\m68k\include\asm\linkage.h | 9 | stupid | * Make sure the compiler doesn't do anything stupid with the |
| kernel/arch\m68k\include\asm\sun3ints.h | 30 | fuck | /* master list of VME vectors -- don't fuck with this */ |
| kernel/arch\mips\include\uapi\asm\bitfield.h | 13 | Damn | *  * Damn ...  bitfields depend from byteorder :-( |
| kernel/arch\mips\kernel\process.c | 657 | ass | * __get_wchan - a maintenance nightmare^W^Wpain in the ass ... |
| kernel/arch\mips\mm\c-r4k.c | 1400 | bitch | * This is such a bitch, you'd think they would make it easy to do |
| kernel/arch\mips\sni\reset.c | 16 | stupid | * and if it doesn't work, we do some other stupid things. |
| kernel/arch\powerpc\kernel\eeh_driver.c | 170 | ass | * This is just ass backwards. This maze has |
| kernel/arch\powerpc\kernel\pci_64.c | 131 | stupid | * that case.  Maybe we should due to stupid card with incomplete |
| kernel/arch\powerpc\kernel\pci_64.c | 169 | stupid | * the core does in that case. Maybe we should due to stupid card |
| kernel/arch\powerpc\platforms\44x\pci.c | 1488 | stupid | /* Remove the casts when we finally remove the stupid volatile |
| kernel/arch\s390\kernel\ptrace.c | 278 | Stupid | * Stupid gdb peeks/pokes the access registers in 64 bit with |
| kernel/arch\s390\kernel\ptrace.c | 417 | Stupid | * Stupid gdb peeks/pokes the access registers in 64 bit with |
| kernel/arch\sh\Makefile | 49 | stupid | # regarding FP generation. This is intentionally stupid (albeit many |
| kernel/arch\sh\drivers\pci\ops-dreamcast.c | 43 | stupid | * was at least done right, and we don't have to do the stupid masking and |
| kernel/arch\sh\include\asm\vga.h | 5 | Stupid | /* Stupid drivers. */ |
| kernel/arch\sh\kernel\cpu\sh4\sq.c | 250 | stupid | * putting the directory entries somewhere stupid and having to create |
| kernel/arch\sparc\kernel\wof.S | 293 | stupid | * if used below.  This helps find 'stupid' coding errors that |
| kernel/arch\sparc\lib\checksum_32.S | 322 | ass | be	ccdbl + 4		! 8 byte aligned, kick ass |
| kernel/arch\sparc\math-emu\math_32.c | 157 | stupid | * [The UltraSPARC makes FP a precise trap; this isn't as stupid as it |
| kernel/arch\sparc\mm\hypersparc.S | 166 | ass | /* Verified, my ass... */ |
| kernel/arch\sparc\mm\iommu.c | 92 | Stupid | /* Stupid alignment constraints give me a headache. |
| kernel/arch\x86\include\asm\debugreg.h | 26 | Damn | unsigned long val = 0;	/* Damn you, gcc! */ |
| kernel/arch\x86\include\asm\xor_32.h | 242 | stupid | Clobber them just to be sure nobody does something stupid |
| kernel/arch\x86\include\asm\xor_32.h | 515 | stupid | Clobber them just to be sure nobody does something stupid |
| kernel/arch\x86\include\asm\xen\interface.h | 114 | stupid | * start of the GDT because some stupid OSes export hard-coded selector values |
| kernel/arch\x86\kernel\hpet.c | 446 | stupid | *    reprogrammed due to the handler hijacking. Duh, stupid me! |
| kernel/arch\x86\kernel\ioport.c | 127 | stupid | * Search for a (possibly new) maximum. This is simple and stupid, |
| kernel/arch\x86\kernel\vm86_32.c | 671 | Damn | * Damn. This is incorrect: the 'sti' instruction should actually |
| kernel/arch\x86\kernel\apic\vector.c | 1148 | stupid | * as stupid as the real hardware. |
| kernel/arch\x86\math-emu\fpu_trig.c | 1391 | Stupid | #ifdef PECULIAR_486		/* Stupid 80486 doesn't worry about log(negative). */ |
| kernel/arch\x86\math-emu\fpu_trig.c | 1413 | Stupid | #ifdef PECULIAR_486		/* Stupid 80486 doesn't worry about log(negative). */ |
| kernel/arch\x86\math-emu\poly_l2.c | 139 | Stupid | #ifdef PECULIAR_486		/* Stupid 80486 doesn't worry about log(negative). */ |
| kernel/arch\x86\pci\irq.c | 433 | damn | * ALI pirq entries are damn ugly, and completely undocumented. |
| kernel/Documentation\crypto\descore-readme.rst | 290 | stupid | b) the compiler may be too stupid to realize table and table+256 should |
| kernel/Documentation\driver-api\media\drivers\zoran.rst | 328 | damn | How do I get this damn thing to work |
| kernel/Documentation\kernel-hacking\hacking.rst | 797 | damn | * Sun people can't spell worth damn. "compatability" indeed. |
| kernel/Documentation\networking\arcnet-hardware.rst | 2442 | ASS | and "-2 46-86" beside C2. Between C1 and C6 "ASS 'Y 300163" and "@1986 |
| kernel/Documentation\power\swsusp.rst | 134 | stupid | well, suspending a server is IMHO a really stupid thing, |
| kernel/Documentation\process\management-style.rst | 75 | stupid | It turns out that since nobody would be stupid enough to ever really let |
| kernel/Documentation\process\management-style.rst | 105 | stupid | to admit that you are stupid when you haven't **yet** done the really |
| kernel/Documentation\process\management-style.rst | 106 | stupid | stupid thing. |
| kernel/Documentation\process\volatile-considered-harmful.rst | 89 | stupid | to be a "stupid legacy" issue (Linus's words) in this regard; fixing it |
| kernel/Documentation\process\management-style.rst | 108 | stupid | Then, when it really does turn out to be stupid, people just roll their |
| kernel/Documentation\RCU\RTFP.txt | 1740 | ass | \url{https://lore.kernel.org/r/20070128120509.719287000@programming.kicks-ass.net} |
| kernel/Documentation\scsi\ncr53c8xx.rst | 1264 | arse | be surprised, because force-feeding anything and blocking its arse at the |
| kernel/Documentation\translations\it_IT\kernel-hacking\hacking.rst | 836 | damn | * Sun people can't spell worth damn. "compatability" indeed. |
| kernel/Documentation\translations\zh_CN\kernel-hacking\hacking.rst | 675 | damn | * Sun people can't spell worth damn. "compatibility" indeed. |
| kernel/drivers\acpi\cppc_acpi.c | 1897 | stupid | * Real stupid fallback value, just in case there is no |
| kernel/drivers\ata\pata_hpt366.c | 297 | stupid | * to both functions -- really stupid design decision... :-( |
| kernel/drivers\ata\sata_sil.c | 492 | ass | /* kick HSM in the ass */ |
| kernel/drivers\atm\eni.c | 50 | stupid | * - buffer space allocation algorithm is stupid |
| kernel/drivers\char\agp\isoch.c | 279 | stupid | * pretty stupid, divide the total number of RQ slots provided by the |
| kernel/drivers\clocksource\acpi_pm.c | 257 | Stupid | * Allow an override of the IOPort. Stupid BIOSes do not tell us about |
| kernel/drivers\gpio\gpio-sim.c | 625 | stupid | * configfs is stupid and calls the item's release callback after |
| kernel/drivers\gpu\drm\i915\display\intel_display.c | 5023 | stupid | pipe_config_mismatch(p, fastset, crtc, name, " "); /* stupid -Werror=format-zero-length */ |
| kernel/drivers\gpu\drm\i915\display\intel_hdcp.c | 906 | stupid | * the stupid thing instead of polling on one and not the other. |
| kernel/drivers\gpu\drm\i915\gem\i915_gem_wait.c | 220 | damn | *  -ENOMEM: damn |
| kernel/drivers\gpu\drm\msm\registers\adreno\a3xx.xml | 831 | ass | <!-- complete wild-ass-guess for sizes of these bitfields.. --> |
| kernel/drivers\gpu\drm\msm\registers\adreno\a4xx.xml | 1987 | ass | <!-- complete wild-ass-guess for sizes of these bitfields.. --> |
| kernel/drivers\gpu\drm\nouveau\dispnv04\hw.c | 93 | stupid | /* This might seem stupid, but the blob does it and |
| kernel/drivers\gpu\drm\nouveau\nvkm\subdev\pmu\fuc\macros.fuc | 49 | fuck | #define NV_PPWR_INTR_EN_CLR_MASK                    /* fuck i hate envyas */ -1 |
| kernel/drivers\gpu\drm\nouveau\nvkm\subdev\timer\base.c | 133 | stupid | /* This shouldn't happen if callers aren't stupid. |
| kernel/drivers\hid\hid-playstation.c | 1754 | stupid | * are likely resolved then (the dongle is quite stupid). |
| kernel/drivers\hwmon\adm1025.c | 489 | stupid | * that the ADM1025 comes with stupid default limits (all registers |
| kernel/drivers\hwmon\dme1737.c | 473 | stupid | /* the first two cases are special - stupid chip design! */ |
| kernel/drivers\irqchip\irq-gic.c | 1298 | stupid | * Check for a stupid firmware that only exposes the |
| kernel/drivers\leds\led-triggers.c | 120 | stupid | * It was stupid to create 10000 cpu triggers, but we are stuck with it now. |
| kernel/drivers\media\dvb-frontends\drx39xyj\drx_driver.h | 907 | ASS | #define DRX_CFG_AUD_AUTOSOUND       (DRX_CFG_BASE +  8)	/* ASS & ASC         */ |
| kernel/drivers\media\dvb-frontends\drx39xyj\drx_driver.h | 908 | ASS | #define DRX_CFG_AUD_ASS_THRES       (DRX_CFG_BASE +  9)	/* ASS Thresholds    */ |
| kernel/drivers\media\dvb-frontends\drx39xyj\drx_driver.h | 1567 | ASS | u16 a2;	/* A2 Threshold for ASS configuration */ |
| kernel/drivers\media\dvb-frontends\drx39xyj\drx_driver.h | 1568 | ASS | u16 btsc;	/* BTSC Threshold for ASS configuration */ |
| kernel/drivers\media\dvb-frontends\drx39xyj\drx_driver.h | 1569 | ASS | u16 nicam;	/* Nicam Threshold for ASS configuration */ |
| kernel/drivers\media\i2c\ov7670.c | 1038 | ass | * COM7 is a pain in the ass, it doesn't like to be read then |
| kernel/drivers\media\usb\gspca\kinect.c | 321 | stupid | * IR.  This is a stupid workaround, but we've yet to find a better |
| kernel/drivers\misc\sgi-gru\grufault.c | 382 | stupid | * Might be a hardware race OR a stupid user. Ignore FMM because FMM |
| kernel/drivers\mmc\host\wbsd.c | 769 | stupid | * The hardware is so delightfully stupid that it has a list |
| kernel/drivers\net\can\softing\softing_fw.c | 460 | stupid | * which is rather stupid to call close_candev() |
| kernel/drivers\net\ethernet\8390\axnet_cs.c | 769 | stupid | Alan Cox		: support arbitrary stupid port mappings on the |
| kernel/drivers\net\ethernet\8390\lib8390.c | 37 | stupid | Alan Cox		: support arbitrary stupid port mappings on the |
| kernel/drivers\net\ethernet\aeroflex\greth.c | 941 | stupid | /* Failed Allocating a new skb. This is rather stupid |
| kernel/drivers\net\ethernet\alteon\acenic.c | 518 | damn | * addresses but who gives a damn. |
| kernel/drivers\net\ethernet\amd\sunlance.c | 52 | stupid | *		  This was the sun4c killer. Shit, stupid bug. |
| kernel/drivers\net\ethernet\dec\tulip\tulip_core.c | 1548 | damn | sa_offset = 2;		/* Grrr, damn Matrox boards. */ |
| kernel/drivers\net\ethernet\intel\e1000\e1000_main.c | 2313 | stupid | * both stupid write combining chipsets, and flushing each write |
| kernel/drivers\net\ethernet\natsemi\ns83820.c | 50 | stupid | *			0.20 -	fix stupid RFEN thinko.  i am such a smurf. |
| kernel/drivers\net\ethernet\seeq\sgiseeq.c | 35 | stupid | * stupid Lance from a driver architecture perspective.  Only difference is that |
| kernel/drivers\net\ethernet\seeq\sgiseeq.c | 38 | stupid | * how a stupid idea like this can pay off in performance, not to mention |
| kernel/drivers\net\ethernet\sun\sunhme.h | 275 | ASS | * But.... THIS THING IS A PAIN IN THE ASS TO PROGRAM! |
| kernel/drivers\net\ethernet\sun\sunhme.c | 985 | fuck | /* Only Sun can take such nice parts and fuck up the programming interface |
| kernel/drivers\net\fddi\skfp\h\supern_2.h | 774 | ass | #define	PL_LOOPBACK	0x0080		/* it cause the /LPBCK pin ass. low */ |
| kernel/drivers\net\fddi\skfp\h\supern_2.h | 775 | ass | #define	PL_MINI_CTR_INT 0x0100		/* partially contr. when bit is ass. */ |
| kernel/drivers\net\hamradio\scc.c | 1443 | Damn | * Damn, where is my Z8530 programming manual...? |
| kernel/drivers\net\hippi\rrunner.c | 14 | stupid | * stupid bugs in my code. |
| kernel/drivers\net\wan\farsync.h | 344 | ass | * one of these then I've been an ass |
| kernel/drivers\net\wireless\ath\ath5k\eeprom.c | 104 | stupid | * Fail safe check to prevent stupid loops due |
| kernel/drivers\net\wireless\broadcom\b43\phy_n.h | 679 | retard | #define B43_NPHY_PHYSTAT_ADVRET			B43_PHY_N(0x1F3) /* PHY stats ADV retard */ |
| kernel/drivers\net\wireless\broadcom\b43\wa.c | 127 | retard | static void b43_wa_art(struct b43_wldev *dev) /* ADV retard table */ |
| kernel/drivers\net\wireless\broadcom\brcm80211\brcmsmac\d11.h | 1500 | Retard | /* Advance Retard */ |
| kernel/drivers\net\wireless\intel\iwlegacy\common.h | 97 | stupid | * (which is somewhat stupid -- look at common.c for instance |
| kernel/drivers\net\wireless\intersil\p54\txrx.c | 71 | stupid | * So, the firmware is somewhat stupid and doesn't know what places in its |
| kernel/drivers\net\wireless\mediatek\mt7601u\initvals_phy.h | 198 | stupid | *	 from channel switching. Seems stupid at best. |
| kernel/drivers\pci\quirks.c | 255 | stupid | /* stupid compiler warning, you would think with an enum... */ |
| kernel/drivers\pci\msi\msi.c | 42 | stupid | *  a) it's stupid .. |
| kernel/drivers\s390\block\dasd_fba.c | 510 | stupid | /* Locate record for stupid devices. */ |
| kernel/drivers\s390\char\tape_core.c | 76 | ASS | [TO_DIS] = "DIS",	[TO_ASSIGN] = "ASS", |
| kernel/drivers\scsi\aha152x.c | 216 | damn | * first "damn thing doesn't work" version |
| kernel/drivers\scsi\atari_scsi.c | 551 | stupid | /* ST DMA chip is stupid -- only multiples of 512 bytes! (and max. |
| kernel/drivers\scsi\ncr53c8xx.c | 7831 | stupid | **	announce stupid things to user. |
| kernel/drivers\scsi\qla1280.c | 3238 | damn | * This can be called from interrupt context, damn it!!! |
| kernel/drivers\scsi\scsi_transport_spi.c | 937 | stupid | * signal type (if known).  Some devices are stupid on |
| kernel/drivers\scsi\scsi_transport_spi.c | 980 | stupid | /* OK, the stupid drive can't do a write echo buffer |
| kernel/drivers\scsi\wd33c93.c | 56 | Stupid | * there are lots of lurking bugs and "Stupid Places". |
| kernel/drivers\scsi\pcmcia\nsp_cs.c | 388 | stupid | /* XXX: what a stupid chip! */ |
| kernel/drivers\scsi\sym53c8xx_2\sym_hipd.c | 2760 | stupid | *    When a stupid device does not want to handle the |
| kernel/drivers\spi\spi-gpio.c | 130 | stupid | * GCC be less stupid about reloading registers inside the I/O loops, |
| kernel/drivers\ssb\pci.c | 822 | stupid | /* Workaround: The BCM44XX chip has a stupid revision |
| kernel/drivers\staging\olpc_dcon\olpc_dcon.c | 147 | stupid | goto power_up;	/* argh, stupid hardware.. */ |
| kernel/drivers\staging\olpc_dcon\olpc_dcon.c | 190 | stupid | /* For now, this will be really stupid - we need to address how |
| kernel/drivers\tty\serial\serial_core.c | 1032 | bitch | * instead of clearing it, then bitch about it. |
| kernel/drivers\tty\serial\sunsu.c | 95 | Stupid | unsigned int		type_probed;	/* XXX Stupid */ |
| kernel/drivers\tty\serial\sunsu.c | 1079 | stupid | * manufacturer would be stupid enough to design a board |
| kernel/drivers\tty\serial\8250\8250_port.c | 1211 | stupid | * manufacturer would be stupid enough to design a board |
| kernel/drivers\usb\fotg210\fotg210-hcd.c | 2882 | ASS | /* Don't start the schedule until ASS is 0 */ |
| kernel/drivers\usb\fotg210\fotg210-hcd.c | 2895 | ASS | /* Don't turn off the schedule until ASS is 1 */ |
| kernel/drivers\usb\gadget\function\f_rndis.c | 49 | stupid | * "so smart it's stupid" hardware which takes over configuration changes |
| kernel/drivers\usb\host\ehci-hcd.c | 639 | ASS | /* For Aspeed, STS_HALT also depends on ASS/PSS status. |
| kernel/drivers\usb\host\ehci-q.c | 958 | ASS | /* Don't start the schedule until ASS is 0 */ |
| kernel/drivers\usb\host\ehci-q.c | 972 | ASS | /* Don't turn off the schedule until ASS is 1 */ |
| kernel/drivers\usb\image\microtek.c | 76 | Stupid | *	20000514 Stupid bug fixes (john) |
| kernel/drivers\usb\serial\belkin_sa.h | 24 | stupid | *    adapter, so pardon any stupid mistakes.  All of the information |
| kernel/drivers\video\fbdev\au1200fb.c | 1530 | damn | damn as to what the monitor specs are (the panel itself does, but that |
| kernel/drivers\video\fbdev\sa1100fb.c | 485 | stupid | * Make sure the user isn't doing something stupid. |
| kernel/drivers\video\fbdev\sa1100fb.c | 1103 | stupid | * does something stupid. |
| kernel/drivers\video\fbdev\sis\init.c | 3480 | Stupid | /* Stupid hack for 640x400/320x200 */ |
| kernel/drivers\watchdog\pc87413_wdt.c | 496 | bitch | *	resources we require and bitch if anyone beat us to them. |
| kernel/drivers\watchdog\wdt.c | 582 | bitch | *	resources we require and bitch if anyone beat us to them. |
| kernel/fs\coredump.c | 603 | stupid | * lots of stupid things. |
| kernel/fs\pipe.c | 1051 | stupid | * This is the stupid "wait for pipe to be readable or writable" |
| kernel/fs\adfs\dir_f.c | 66 | bitch | * assembler, but a bitch in C...  This is one |
| kernel/fs\affs\Changes | 243 | Damn | 30 characters. (Damn it! This kind of bug |
| kernel/fs\bcachefs\btree_update_interior.c | 190 | stupid | /* stupid integer promotion rules */ |
| kernel/fs\befs\ChangeLog | 14 | stupid | * Oy! Fixed stupid bug that would cause an unresolved symbol error. |
| kernel/fs\befs\ChangeLog | 98 | stupid | * Fixed stupid bug where specifying the uid or gid mount options as '0' |
| kernel/fs\btrfs\inode.c | 9789 | stupid | * file changes again after this, the user is doing something stupid and |
| kernel/fs\isofs\inode.c | 846 | stupid | * It would be incredibly stupid to allow people to mark every file |
| kernel/fs\notify\fsnotify.c | 129 | damn | * directory, there damn well better only be one item on this list */ |
| kernel/fs\ocfs2\cluster\heartbeat.c | 2208 | damn | * entire damn world #includes */ |
| kernel/fs\reiserfs\xattr.c | 843 | stupid | * We totally ignore the generic listxattr here because it would be stupid |
| kernel/fs\smb\client\dir.c | 880 | ass | * Here, we again ass|u|me that upper/lowercase versions of |
| kernel/fs\xfs\xfs_mru_cache.c | 524 | stupid | __release(mru_lock); /* help sparse not be stupid */ |
| kernel/fs\xfs\scrub\nlinks_repair.c | 177 | stupid | * store.  This is a never-ending and stupid battle; both tools missed |
| kernel/include\linux\printk.h | 93 | stupid | * really stupid or out of spec. Be aware that the responsible BIOS developer |
| kernel/include\linux\mtd\flashchip.h | 64 | damn | it'll make it a damn sight harder to find which chip we want from |
| kernel/include\net\dsa.h | 338 | stupid | * so keep it stupid at the moment and list them all. |
| kernel/include\uapi\linux\v4l2-controls.h | 422 | Stupid | /* Kept for backwards compatibility reasons. Stupid typo... */ |
| kernel/kernel\fork.c | 12 | bitch | * management can be a bitch. See 'mm/memory.c': 'copy_page_range()' |
| kernel/kernel\locking\lockdep.c | 3967 | damn | * More smoking hash instead of calculating it, damn see these |
| kernel/kernel\module\Kconfig | 51 | stupid | and want to see if userspace or the kernel is doing stupid things |
| kernel/kernel\module\main.c | 734 | damn | /* FIXME: if (force), slam module count damn the torpedoes */ |
| kernel/kernel\module\stats.c | 190 | stupid | *    seriously stupid or that could be improved. We should strive to fix these, |
| kernel/kernel\sched\fair.c | 7861 | stupid | * If the previous CPU is cache affine and idle, don't be stupid: |
| kernel/kernel\trace\ring_buffer.c | 1114 | stupid | /* Just stupid testing the normalize function and deltas */ |
| kernel/lib\btree.c | 9 | ass | * see http://programming.kicks-ass.net/kernel-patches/vma_lookup/btree.patch |
| kernel/lib\objagg.c | 502 | stupid | * As a very stupid example, consider integer numbers. For example |
| kernel/lib\test_xarray.c | 804 | stupid | * APIs won't be stupid, proper page cache APIs loop over the proper |
| kernel/net\core\skbuff.c | 5335 | Fuck | /* Fuck, we are miserable poor guys... */ |
| kernel/net\ipv4\ip_options.c | 192 | stupid | *	Simple and stupid 8), but the most efficient way. |
| kernel/net\ipv4\route.c | 3708 | damn | * We really need to sanitize the damn ipv4 init order, then all |
| kernel/net\mac80211\iface.c | 1155 | stupid | /* ok .. stupid driver, it asked for this! */ |
| kernel/net\netfilter\nf_conntrack_helper.c | 43 | Stupid | /* Stupid hash, but collision free for the default registrations of the |
| kernel/net\netfilter\xt_string.c | 44 | Damn | /* Damn, can't handle this case properly with iptables... */ |
| kernel/net\rfkill\core.c | 94 | stupid | * a bit of a stupid situation because drivers might want to register |
| kernel/net\sched\act_ife.c | 819 | stupid | /* could be stupid policy setup or mtu config |
| kernel/net\sctp\protocol.c | 736 | stupid | * This operation is a bit stupid, but the DHCP client attaches the |
| kernel/net\unix\garbage.c | 58 | Damn | *		Damn. Added missing check for ->dead in listen queues scanning. |
| kernel/net\unix\af_unix.c | 12 | stupid | *		Alan Cox	:	Fixed the stupid socketpair bug. |
| kernel/net\wireless\sme.c | 405 | stupid | * Some stupid APs don't accept reassoc, so we |
| kernel/net\xfrm\xfrm_policy.c | 3330 | stupid | * stupid way. Shame on me. :-) Of course, connected sockets must |
| kernel/scripts\checksyscalls.sh | 243 | stupid | /* sync_file_range had a stupid ABI. Allow sync_file_range2 instead */ |
| kernel/sound\pci\azt3328.c | 24 | stupid | *  (and I was stupid enough to manage to get hold of a PCI168 soundcard |
| kernel/sound\pci\azt3328.c | 141 | Stupid | *    If this can't be set, then get a mixer application that Isn't Stupid (tm) |
| kernel/sound\pci\ens1370.c | 105 | stupid | Yes, I know it's stupid and why didn't we use the sub IDs? |
| kernel/sound\pci\azt3328.c | 616 | damn | (13), make damn sure |
| kernel/sound\pci\hda\patch_realtek.c | 687 | ass | unsigned int ass, tmp, i; |
| kernel/sound\pci\hda\patch_realtek.c | 694 | ass | ass = spec->cdefine.sku_cfg; |
| kernel/sound\pci\hda\patch_realtek.c | 695 | ass | if (ass == ALC_FIXUP_SKU_IGNORE) |
| kernel/sound\pci\hda\patch_realtek.c | 702 | ass | ass = codec->core.subsystem_id & 0xffff; |
| kernel/sound\pci\hda\patch_realtek.c | 703 | ass | if (ass != codec->bus->pci->subsystem_device && (ass & 1)) |
| kernel/sound\pci\hda\patch_realtek.c | 709 | ass | ass = snd_hda_codec_get_pincfg(codec, nid); |
| kernel/sound\pci\hda\patch_realtek.c | 711 | ass | if (!(ass & 1)) { |
| kernel/sound\pci\hda\patch_realtek.c | 713 | ass | codec->core.chip_name, ass); |
| kernel/sound\pci\hda\patch_realtek.c | 720 | ass | if ((ass >> i) & 1) |
| kernel/sound\pci\hda\patch_realtek.c | 723 | ass | if (((ass >> 16) & 0xf) != tmp) |
| kernel/sound\pci\hda\patch_realtek.c | 726 | ass | spec->cdefine.port_connectivity = ass >> 30; |
| kernel/sound\pci\hda\patch_realtek.c | 727 | ass | spec->cdefine.enable_pcbeep = (ass & 0x100000) >> 20; |
| kernel/sound\pci\hda\patch_realtek.c | 728 | ass | spec->cdefine.check_sum = (ass >> 16) & 0xf; |
| kernel/sound\pci\hda\patch_realtek.c | 729 | ass | spec->cdefine.customization = ass >> 8; |
| kernel/sound\pci\hda\patch_realtek.c | 731 | ass | spec->cdefine.sku_cfg = ass; |
| kernel/sound\pci\hda\patch_realtek.c | 732 | ass | spec->cdefine.external_amp = (ass & 0x38) >> 3; |
| kernel/sound\pci\hda\patch_realtek.c | 733 | ass | spec->cdefine.platform_type = (ass & 0x4) >> 2; |
| kernel/sound\pci\hda\patch_realtek.c | 734 | ass | spec->cdefine.swap = (ass & 0x2) >> 1; |
| kernel/sound\pci\hda\patch_realtek.c | 735 | ass | spec->cdefine.override = ass & 0x1; |
| kernel/sound\pci\hda\patch_realtek.c | 778 | ass | unsigned int ass, tmp, i; |
| kernel/sound\pci\hda\patch_realtek.c | 783 | ass | ass = spec->cdefine.sku_cfg; |
| kernel/sound\pci\hda\patch_realtek.c | 784 | ass | if (ass == ALC_FIXUP_SKU_IGNORE) |
| kernel/sound\pci\hda\patch_realtek.c | 789 | ass | ass = codec->core.subsystem_id & 0xffff; |
| kernel/sound\pci\hda\patch_realtek.c | 791 | ass | ass != codec->bus->pci->subsystem_device && (ass & 1)) |
| kernel/sound\pci\hda\patch_realtek.c | 806 | ass | ass = snd_hda_codec_get_pincfg(codec, nid); |
| kernel/sound\pci\hda\patch_realtek.c | 809 | ass | ass, nid); |
| kernel/sound\pci\hda\patch_realtek.c | 810 | ass | if (!(ass & 1)) |
| kernel/sound\pci\hda\patch_realtek.c | 812 | ass | if ((ass >> 30) != 1)	/* no physical connection */ |
| kernel/sound\pci\hda\patch_realtek.c | 818 | ass | if ((ass >> i) & 1) |
| kernel/sound\pci\hda\patch_realtek.c | 821 | ass | if (((ass >> 16) & 0xf) != tmp) |
| kernel/sound\pci\hda\patch_realtek.c | 825 | ass | ass & 0xffff, codec->core.vendor_id); |
| kernel/sound\pci\hda\patch_realtek.c | 833 | ass | tmp = (ass & 0x38) >> 3;	/* external Amp control */ |
| kernel/sound\pci\hda\patch_realtek.c | 855 | ass | if (!(ass & 0x8000)) |
| kernel/sound\pci\hda\patch_realtek.c | 866 | ass | tmp = (ass >> 11) & 0x3;	/* HP to chassis */ |
| kernel/sound\soc\au1x\ac97c.c | 105 | stupid | /* stupid errata: data is only valid for 21us, so |
| kernel/sound\usb\misc\ua101.c | 33 | stupid | * sizes at all sample rates, taking into account the stupid cache pool sizes |
| kernel/tools\testing\radix-tree\tag_check.c | 115 | Stupid | * Stupid tag thrasher |
| kernel/tools\testing\selftests\powerpc\eeh\eeh-functions.sh | 33 | stupid | # EEH_STATE_DMA_ACTIVE flags set. For some goddamn stupid reason |


Last updated: 2024-09-28 19:51:41
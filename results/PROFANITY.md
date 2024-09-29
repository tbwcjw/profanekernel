| file | line | keyword | match |
| --- | --- | --- | --- |
| kernel/MAINTAINERS | 8357 | Dick | M:	Dick Kennedy <dick.kennedy@broadcom.com> |
| kernel/arch\alpha\kernel\sys_takara.c | 155 | hell | * assign it whatever the hell IRQ we like and it doesn't matter. |
| kernel/arch\alpha\lib\dbg_stackcheck.S | 25 | damn | 1:	stq	$31, -8($31)	# oops me, damn it. |
| kernel/arch\arc\mm\highmem.c | 66 | hell | /* Due to recursive include hell, we can't do this in processor.h */ |
| kernel/arch\arm\kernel\head.S | 86 | crap | * We're trying to keep crap to a minimum; DO NOT add any machine specific |
| kernel/arch\arm\kernel\head.S | 87 | crap | * crap here - that's what the boot loader (or in extreme, well justified |
| kernel/arch\arm\kernel\traps.c | 632 | hell | * the fires of hell burn in your belly if you break this rule. ;) |
| kernel/arch\arm64\include\asm\memory.h | 232 | hell | // For reasons of #include hell, we can't use TCR_T1SZ_OFFSET/TCR_T1SZ_MASK here |
| kernel/arch\arm64\include\asm\spinlock.h | 19 | ass | * https://lore.kernel.org/lkml/20200110100612.GC2827@hirez.programming.kicks-ass.net |
| kernel/arch\arm64\kernel\sys_compat.c | 80 | hell | * the fires of hell burn in your belly if you break this rule. ;) |
| kernel/arch\arm64\kernel\vdso\sigreturn.S | 7 | hell | * It's also fragile as hell, so please think twice before changing anything |
| kernel/arch\arm64\kvm\hypercalls.c | 60 | damn | * nobody will give a damn about it). |
| kernel/arch\arm64\kvm\mmu.c | 2193 | damn | * - System caches don't support S/W at all (damn!) |
| kernel/arch\arm64\kvm\hyp\vhe\switch.c | 94 | crap | * The architecture is a bit crap (what a surprise): an EL2 guest |
| kernel/arch\arm64\kvm\hyp\vhe\switch.c | 97 | sucker | * sucker using the very same bit it can't set... |
| kernel/arch\arm64\kvm\vgic\vgic-irqfd.c | 126 | damn | * as long as the damn vgic is initialized. |
| kernel/arch\arm64\lib\csum.c | 35 | piss | * however, have to be careful not to piss off KASAN, which means using |
| kernel/arch\hexagon\kernel\smp.c | 28 | crap | * (which is prior to any of our smp_prepare_cpu crap), in order to set |
| kernel/arch\hexagon\mm\init.c | 38 | Hell | * over until Hell freezes over.  Actual bound in years needs to be |
| kernel/arch\loongarch\lib\csum.c | 36 | piss | * however, have to be careful not to piss off KASAN, which means using |
| kernel/arch\m68k\include\asm\sun3ints.h | 30 | fuck | /* master list of VME vectors -- don't fuck with this */ |
| kernel/arch\m68k\include\asm\sun3xflop.h | 28 | crap | /* We don't need no stinkin' I/O port allocation crap. */ |
| kernel/arch\m68k\mac\config.c | 593 | hell | * Quadra-style VIAs. A few models also have IDE from hell. |
| kernel/arch\mips\dec\kn01-berr.c | 97 | Bloody | /* Bloody hardware doesn't record the address for reads... */ |
| kernel/arch\mips\dec\int-handler.S | 48 | hell | *    IRQ mask, that would make this routine slow as hell. |
| kernel/arch\mips\include\asm\mipsprom.h | 30 | shit | /* More PROM shit.  Probably has to do with VME RMW cycles??? */ |
| kernel/arch\mips\include\asm\prefetch.h | 20 | Hell | * Hell (and the book on my shelf I can't open ...) know what the R8000 does. |
| kernel/arch\mips\include\uapi\asm\bitfield.h | 13 | Damn | *  * Damn ...  bitfields depend from byteorder :-( |
| kernel/arch\mips\kernel\genex.S | 72 | shit | * Big shit, we now may have two dirty primary cache lines for the same |
| kernel/arch\mips\kernel\process.c | 657 | ass | * __get_wchan - a maintenance nightmare^W^Wpain in the ass ... |
| kernel/arch\mips\kernel\unaligned.c | 573 | sucker | * cache coherence problem.  Die sucker, die ... |
| kernel/arch\mips\kernel\unaligned.c | 1481 | sucker | * cache coherence problem.  Die sucker, die ... |
| kernel/arch\mips\kernel\vmlinux.lds.S | 234 | crap | /* ABI crap starts here */ |
| kernel/arch\mips\mm\c-r4k.c | 1400 | bitch | * This is such a bitch, you'd think they would make it easy to do |
| kernel/arch\mips\pci\fixup-ip32.c | 41 | crap | * right if there exists such a broken piece of crap. |
| kernel/arch\powerpc\kernel\eeh_driver.c | 170 | ass | * This is just ass backwards. This maze has |
| kernel/arch\powerpc\kernel\eeh_driver.c | 183 | shit | * shit unusable forever. |
| kernel/arch\powerpc\mm\nohash\tlb_low_64e.S | 140 | crap | * r15 = crap (free to use) |
| kernel/arch\powerpc\mm\nohash\tlb_low_64e.S | 144 | crap | * r10 = crap (free to use) |
| kernel/arch\powerpc\mm\nohash\tlb_low_64e.S | 186 | crap | clrrdi	r11,r16,12		/* Clear low crap in EA */ |
| kernel/arch\powerpc\mm\nohash\tlb_low_64e.S | 187 | crap | clrldi	r15,r15,12		/* Clear crap at the top */ |
| kernel/arch\powerpc\mm\nohash\tlb_low_64e.S | 284 | crap | * r15 = crap (free to use) |
| kernel/arch\powerpc\mm\nohash\tlb_low_64e.S | 288 | crap | * r10 = crap (free to use) |
| kernel/arch\powerpc\mm\nohash\tlb_low_64e.S | 474 | crap | clrldi	r15,r15,PAGE_SHIFT	/* Clear crap at the top */ |
| kernel/arch\powerpc\mm\nohash\tlb_low_64e.S | 515 | crap | * r14 = crap (free to use) |
| kernel/arch\powerpc\mm\nohash\tlb_low_64e.S | 518 | crap | * r11 = crap (free to use) |
| kernel/arch\powerpc\mm\nohash\tlb_low_64e.S | 519 | crap | * r10 = crap (free to use) |
| kernel/arch\powerpc\mm\nohash\tlb_low_64e.S | 671 | crap | * r15 = crap (free to use) |
| kernel/arch\powerpc\mm\nohash\tlb_low_64e.S | 675 | crap | * r11 = crap (free to use) |
| kernel/arch\powerpc\mm\nohash\tlb_low_64e.S | 676 | crap | * r10 = crap (free to use) |
| kernel/arch\powerpc\platforms\cell\spider-pic.c | 204 | crap | * crap and we don't know on which BE iic interrupt we are hooked on at |
| kernel/arch\powerpc\platforms\cell\spider-pic.c | 254 | hell | /* ugly as hell but works for now */ |
| kernel/arch\powerpc\platforms\powermac\low_i2c.c | 741 | hell | /* I know that looks like a lot, slow as hell, but darwin |
| kernel/arch\powerpc\platforms\powermac\smp.c | 338 | crap | * crap to avoid giving people ideas that they can do the |
| kernel/arch\powerpc\platforms\powermac\smp.c | 824 | crap | * ideally, all that crap will be done in prom.c and the CPU left |
| kernel/arch\s390\kernel\ptrace.c | 279 | hell | * an alignment of 4. Programmers from hell... |
| kernel/arch\s390\kernel\ptrace.c | 418 | hell | * an alignment of 4. Programmers from hell indeed... |
| kernel/arch\sh\kernel\cpu\sh4\sq.c | 254 | hell | * queue, but considering the kobject hell we already have to deal with, |
| kernel/arch\sparc\include\asm\floppy_32.h | 21 | crap | /* We don't need no stinkin' I/O port allocation crap. */ |
| kernel/arch\sparc\kernel\pcic.c | 504 | shit | * to shit into regions like that. |
| kernel/arch\sparc\kernel\traps_64.c | 315 | Shit | /* Shit... */ |
| kernel/arch\sparc\kernel\viohs.c | 683 | crap | * to be aware of this crap. |
| kernel/arch\sparc\kernel\wof.S | 131 | hell | * and messy as all hell.  And difficult to follow if you |
| kernel/arch\sparc\lib\checksum_32.S | 306 | shit | * give up.  I'm serious, I am going to kick the living shit |
| kernel/arch\sparc\lib\checksum_32.S | 322 | ass | be	ccdbl + 4		! 8 byte aligned, kick ass |
| kernel/arch\sparc\mm\hypersparc.S | 166 | ass | /* Verified, my ass... */ |
| kernel/arch\sparc\mm\srmmu.c | 1136 | crap | /* Clear any crap from the cache or else... */ |
| kernel/arch\sparc\mm\srmmu.c | 1149 | shit | * this shit off... nice job Fujitsu. |
| kernel/arch\sparc\mm\ultra.S | 25 | shit | * in Microelectronics who refused to fix this shit. |
| kernel/arch\sparc\mm\srmmu.c | 1317 | crap | /* Clear any crap from the cache or else... */ |
| kernel/arch\um\drivers\daemon_kern.c | 32 | crap | /* We will free this pointer. If it contains crap we're burned. */ |
| kernel/arch\x86\include\asm\debugreg.h | 26 | Damn | unsigned long val = 0;	/* Damn you, gcc! */ |
| kernel/arch\x86\include\asm\nospec-branch.h | 540 | hell | * (Implemented as CPP macros due to header hell.) |
| kernel/arch\x86\include\asm\pci_x86.h | 94 | Crap | u32 miniport_data;		/* Crap */ |
| kernel/arch\x86\include\asm\preempt.h | 41 | hell | * must be macros to avoid header recursion hell |
| kernel/arch\x86\include\asm\ptrace.h | 385 | hell | /* To avoid include hell, we can't include uaccess.h */ |
| kernel/arch\x86\include\asm\trace\irq_vectors.h | 79 | hell | * The ifdef is required because that tracepoint macro hell emits tracepoint |
| kernel/arch\x86\kernel\uprobes.c | 510 | hell | *   Evil SSE4.2 string comparison ops from hell. |
| kernel/arch\x86\kernel\vm86_32.c | 671 | Damn | * Damn. This is incorrect: the 'sti' instruction should actually |
| kernel/arch\x86\kernel\cpu\mce\core.c | 1907 | crap | * by default and leave crap in there. Don't log: |
| kernel/arch\x86\pci\irq.c | 433 | damn | * ALI pirq entries are damn ugly, and completely undocumented. |
| kernel/arch\x86\platform\efi\efi_64.c | 313 | crap | * to virtual mode and would otherwise crap on us. |
| kernel/Documentation\arch\s390\3270.rst | 298 | Dick | Dick Hitt <rbh00@utsglobal.com> |
| kernel/Documentation\arch\x86\i386\IO-APIC.rst | 26 | hell | hell:~> cat /proc/interrupts |
| kernel/Documentation\arch\x86\i386\IO-APIC.rst | 37 | hell | hell:~> |
| kernel/Documentation\core-api\irq\irq-affinity.rst | 32 | hell | PING hell (195.4.7.3): 56 data bytes |
| kernel/Documentation\core-api\irq\irq-affinity.rst | 34 | hell | --- hell ping statistics --- |
| kernel/Documentation\core-api\irq\irq-affinity.rst | 51 | hell | PING hell (195.4.7.3): 56 data bytes |
| kernel/Documentation\core-api\irq\irq-affinity.rst | 53 | hell | --- hell ping statistics --- |
| kernel/Documentation\driver-api\media\drivers\zoran.rst | 328 | damn | How do I get this damn thing to work |
| kernel/Documentation\filesystems\ramfs-rootfs-initramfs.rst | 331 | hell | 5) Al Viro made the decision (quote: "tar is ugly as hell and not going to be |
| kernel/Documentation\kernel-hacking\hacking.rst | 797 | damn | * Sun people can't spell worth damn. "compatability" indeed. |
| kernel/Documentation\kernel-hacking\hacking.rst | 816 | shit | * give up.  I'm serious, I am going to kick the living shit |
| kernel/Documentation\networking\arcnet-hardware.rst | 2442 | ASS | and "-2 46-86" beside C2. Between C1 and C6 "ASS 'Y 300163" and "@1986 |
| kernel/Documentation\process\coding-style.rst | 862 | hell | might look like a good thing, but it's confusing as hell when one reads the |
| kernel/Documentation\process\handling-regressions.rst | 672 | dammit | And dammit, we upgrade the kernel ALL THE TIME without upgrading any |
| kernel/Documentation\process\management-style.rst | 67 | bullshit | And people will even see that as true leadership (*cough* bullshit |
| kernel/Documentation\process\management-style.rst | 114 | hell | sure as hell shouldn't encourage them by promising them that what they |
| kernel/Documentation\process\management-style.rst | 272 | crap | a while, and you'll feel cleansed. Just don't crap too close to home. |
| kernel/Documentation\process\submitting-patches.rst | 862 | piss | Greg Kroah-Hartman, "How to piss off a kernel subsystem maintainer". |
| kernel/Documentation\RCU\RTFP.txt | 1740 | ass | \url{https://lore.kernel.org/r/20070128120509.719287000@programming.kicks-ass.net} |
| kernel/Documentation\trace\postprocess\trace-pagealloc-postprocess.pl | 2 | crap | # This is a POC (proof of concept or piece of crap, take your pick) for reading the |
| kernel/Documentation\translations\it_IT\kernel-hacking\hacking.rst | 836 | damn | * Sun people can't spell worth damn. "compatability" indeed. |
| kernel/Documentation\translations\it_IT\kernel-hacking\hacking.rst | 855 | shit | * give up.  I'm serious, I am going to kick the living shit |
| kernel/Documentation\translations\ja_JP\SubmittingPatches | 699 | piss | Greg Kroah-Hartman, "How to piss off a kernel subsystem maintainer". |
| kernel/Documentation\translations\sp_SP\process\submitting-patches.rst | 897 | piss | "How to piss off a kernel subsystem maintainer" por Greg Kroah-Hartman. |
| kernel/Documentation\translations\zh_CN\core-api\irq\irq-affinity.rst | 40 | hell | PING hell (195.4.7.3): 56 data bytes |
| kernel/Documentation\translations\zh_CN\core-api\irq\irq-affinity.rst | 42 | hell | --- hell ping statistics --- |
| kernel/Documentation\translations\zh_CN\core-api\irq\irq-affinity.rst | 58 | hell | PING hell (195.4.7.3): 56 data bytes |
| kernel/Documentation\translations\zh_CN\core-api\irq\irq-affinity.rst | 60 | hell | --- hell ping statistics --- |
| kernel/Documentation\translations\zh_CN\kernel-hacking\hacking.rst | 675 | damn | * Sun people can't spell worth damn. "compatibility" indeed. |
| kernel/Documentation\translations\zh_CN\kernel-hacking\hacking.rst | 694 | shit | * give up.  I'm serious, I am going to kick the living shit |
| kernel/drivers\acpi\acpi_video.c | 1754 | hell | * Also, why the hell we are returning early and not attempt to |
| kernel/drivers\ata\libata-acpi.c | 491 | crap | /* we always use the 0 slot for crap hardware */ |
| kernel/drivers\ata\pata_cmd640.c | 204 | crap | * Of putting crap on the disk |
| kernel/drivers\ata\sata_sil.c | 492 | ass | /* kick HSM in the ass */ |
| kernel/drivers\ata\sata_via.c | 315 | shit | *	SCR registers on vt6420 are pieces of shit and may hang the |
| kernel/drivers\atm\he.c | 1518 | hell | HPRINTK("hell bent for leather!\n"); |
| kernel/drivers\base\bus.c | 693 | hell | /* How the hell do we get out of this pickle? Give up */ |
| kernel/drivers\char\agp\amd64-agp.c | 283 | crap | /* Northbridge seems to contain crap. Try the AGP bridge. */ |
| kernel/drivers\comedi\drivers\das08.c | 181 | crap | /* clear crap */ |
| kernel/drivers\comedi\drivers\ni_daq_dio24.c | 6 | crap | * PCMCIA crap at end of file is adapted from dummy_cs.c 1.31 |
| kernel/drivers\comedi\drivers\ni_labpc_cs.c | 6 | crap | * PCMCIA crap is adapted from dummy_cs.c 1.31 2001/08/24 12:13:13 |
| kernel/drivers\gpu\drm\amd\display\dc\dml\display_mode_vba.c | 313 | bastard | soc->pct_ideal_dram_sdp_bw_after_urgent_pixel_only; // there's always that one bastard variable that's so long it throws everything out of alignment! |
| kernel/drivers\gpu\drm\i915\display\intel_atomic_plane.c | 557 | bollocks | /* FIXME bollocks */ |
| kernel/drivers\gpu\drm\i915\gem\i915_gem_wait.c | 220 | damn | *  -ENOMEM: damn |
| kernel/drivers\gpu\drm\msm\registers\adreno\a3xx.xml | 831 | ass | <!-- complete wild-ass-guess for sizes of these bitfields.. --> |
| kernel/drivers\gpu\drm\msm\registers\adreno\a4xx.xml | 1987 | ass | <!-- complete wild-ass-guess for sizes of these bitfields.. --> |
| kernel/drivers\gpu\drm\nouveau\nouveau_drm.c | 459 | crap | /*XXX: this is crap, but the fence/channel stuff is a little |
| kernel/drivers\gpu\drm\nouveau\include\nvkm\subdev\clk.h | 113 | shit | *     bat-shit insane what-was-nouveau_hw.c code |
| kernel/drivers\gpu\drm\nouveau\nvkm\subdev\instmem\nv40.c | 203 | crap | * 0x21000-0x40000: padding and some unknown crap |
| kernel/drivers\gpu\drm\nouveau\nvkm\subdev\pmu\fuc\macros.fuc | 49 | fuck | #define NV_PPWR_INTR_EN_CLR_MASK                    /* fuck i hate envyas */ -1 |
| kernel/drivers\greybus\es2.c | 330 | Crap | * Crap, pool is empty, complain to the syslog and go allocate one |
| kernel/drivers\hwmon\abituguru.c | 1306 | crap | * anyways. If we read sensors/pwms not there we'll just read crap |
| kernel/drivers\infiniband\hw\qib\qib_file_ops.c | 65 | shit | * This is really, really weird shit - write() and writev() here |
| kernel/drivers\input\joydev.c | 6 | Dyke | * Copyright (c) 1999 Colin Van Dyke |
| kernel/drivers\input\serio\hp_sdc_mlc.c | 111 | Bastard | printk(KERN_WARNING PREFIX "Bastard SDC reconfigured loop!\n"); |
| kernel/drivers\input\serio\hp_sdc_mlc.c | 124 | Bastard | printk(KERN_WARNING PREFIX "Bastard SDC decided to reconfigure loop!\n"); |
| kernel/drivers\iommu\arm\arm-smmu-v3\arm-smmu-v3.c | 3953 | crap | /* CR2 (random crap) */ |
| kernel/drivers\ipack\devices\scc2698.h | 27 | crap | u8 junk[8]; /* other crap for block control */ |
| kernel/drivers\ipack\devices\scc2698.h | 34 | crap | u8 junk[8]; /* other crap for block control */ |
| kernel/drivers\irqchip\irq-gic-v4.c | 46 | crap | *   confines the crap to a single location. And map/unmap really is |
| kernel/drivers\irqchip\irq-gic-v3-its.c | 1120 | hell | /* Warning, macro hell follows */ |
| kernel/drivers\macintosh\adb.c | 239 | bullshit | __adb_probe_task(struct work_struct *bullshit) |
| kernel/drivers\media\dvb-core\dvb_frontend.c | 2206 | crap | * return crap, if they don't check if the data is available |
| kernel/drivers\media\dvb-core\dvb_frontend.c | 2387 | crap | * return crap, if they don't check if the data is available |
| kernel/drivers\media\dvb-core\dvb_frontend.c | 2422 | crap | * return crap, if they don't check if the data is available |
| kernel/drivers\media\dvb-frontends\drx39xyj\drx_driver.h | 907 | ASS | #define DRX_CFG_AUD_AUTOSOUND       (DRX_CFG_BASE +  8)	/* ASS & ASC         */ |
| kernel/drivers\media\dvb-frontends\drx39xyj\drx_driver.h | 908 | ASS | #define DRX_CFG_AUD_ASS_THRES       (DRX_CFG_BASE +  9)	/* ASS Thresholds    */ |
| kernel/drivers\media\dvb-frontends\drx39xyj\drx_driver.h | 1567 | ASS | u16 a2;	/* A2 Threshold for ASS configuration */ |
| kernel/drivers\media\dvb-frontends\drx39xyj\drx_driver.h | 1568 | ASS | u16 btsc;	/* BTSC Threshold for ASS configuration */ |
| kernel/drivers\media\dvb-frontends\drx39xyj\drx_driver.h | 1569 | ASS | u16 nicam;	/* Nicam Threshold for ASS configuration */ |
| kernel/drivers\media\i2c\ov7670.c | 1038 | ass | * COM7 is a pain in the ass, it doesn't like to be read then |
| kernel/drivers\media\i2c\ov7670.c | 1285 | crap | * Weird crap seems to exist in the upper part of |
| kernel/drivers\media\pci\solo6x10\solo6x10-core.c | 566 | crap | /* Undocumented crap */ |
| kernel/drivers\media\usb\gspca\stv06xx\stv06xx_pb0100.h | 4 | Dick | *		      Mark Cave-Ayland, Carlo E Prelz, Dick Streefland |
| kernel/drivers\media\usb\gspca\stv06xx\stv06xx.c | 4 | Dick | *		      Mark Cave-Ayland, Carlo E Prelz, Dick Streefland |
| kernel/drivers\media\usb\gspca\stv06xx\stv06xx_st6422.c | 11 | Dick | *		      Mark Cave-Ayland, Carlo E Prelz, Dick Streefland |
| kernel/drivers\media\usb\gspca\stv06xx\stv06xx_sensor.h | 4 | Dick | *		      Mark Cave-Ayland, Carlo E Prelz, Dick Streefland |
| kernel/drivers\media\usb\gspca\stv06xx\stv06xx_hdcs.h | 4 | Dick | *		      Mark Cave-Ayland, Carlo E Prelz, Dick Streefland |
| kernel/drivers\media\usb\gspca\stv06xx\stv06xx.h | 4 | Dick | *		      Mark Cave-Ayland, Carlo E Prelz, Dick Streefland |
| kernel/drivers\media\usb\gspca\stv06xx\stv06xx_pb0100.c | 4 | Dick | *		      Mark Cave-Ayland, Carlo E Prelz, Dick Streefland |
| kernel/drivers\media\usb\gspca\stv06xx\stv06xx_hdcs.c | 4 | Dick | *		      Mark Cave-Ayland, Carlo E Prelz, Dick Streefland |
| kernel/drivers\media\usb\gspca\stv06xx\stv06xx_st6422.h | 11 | Dick | *		      Mark Cave-Ayland, Carlo E Prelz, Dick Streefland |
| kernel/drivers\media\usb\gspca\stv06xx\stv06xx_vv6410.c | 4 | Dick | *		      Mark Cave-Ayland, Carlo E Prelz, Dick Streefland |
| kernel/drivers\media\usb\gspca\stv06xx\stv06xx_vv6410.h | 4 | Dick | *		      Mark Cave-Ayland, Carlo E Prelz, Dick Streefland |
| kernel/drivers\message\fusion\mptlan.c | 742 | bloody | /* No Flags, 8 bytes of Details, 32bit Context (bloody turbo replies) */ |
| kernel/drivers\misc\cs5535-mfgpt.c | 191 | hell | /* aw hell */ |
| kernel/drivers\mtd\chips\cfi_util.c | 74 | crap | of optimising away all the crap for 'bankwidth' larger than |
| kernel/drivers\mtd\chips\cfi_util.c | 140 | crap | of optimising away all the crap for 'bankwidth' larger than |
| kernel/drivers\net\can\mscan\mscan.c | 203 | hell | * since buffer with lower id have higher priority (hell..) |
| kernel/drivers\net\dsa\ocelot\felix.c | 602 | crap | * So there might still be all sorts of crap in the queues. On the |
| kernel/drivers\net\dsa\sja1105\sja1105_tas.c | 93 | hell | /* Lo and behold: the egress scheduler from hell. |
| kernel/drivers\net\ethernet\alteon\acenic.c | 518 | damn | * addresses but who gives a damn. |
| kernel/drivers\net\ethernet\amd\declance.c | 33 | shit | *      v0.007: Big shit. The LANCE seems to use a different DMA mechanism to |
| kernel/drivers\net\ethernet\amd\sunlance.c | 52 | Shit | *		  This was the sun4c killer. Shit, stupid bug. |
| kernel/drivers\net\ethernet\broadcom\bnx2x\bnx2x_link.c | 4347 | shit | * it means the shit hit the fan. |
| kernel/drivers\net\ethernet\cortina\gemini.c | 1712 | crap | /* Oh, crap */ |
| kernel/drivers\net\ethernet\dec\tulip\tulip_core.c | 1548 | damn | sa_offset = 2;		/* Grrr, damn Matrox boards. */ |
| kernel/drivers\net\ethernet\marvell\sky2.c | 2576 | crap | * to handle crap frames. |
| kernel/drivers\net\ethernet\qlogic\qla3xxx.h | 869 | crap | u16 version_and_numPorts; /* together to avoid endianness crap */ |
| kernel/drivers\net\ethernet\smsc\smc91x.c | 430 | bloody | /* bloody hardware */ |
| kernel/drivers\net\ethernet\sun\sunhme.c | 958 | shit | /* Remember: "Different name, same old buggy as shit hardware." */ |
| kernel/drivers\net\ethernet\sun\sunhme.h | 275 | ASS | * But.... THIS THING IS A PAIN IN THE ASS TO PROGRAM! |
| kernel/drivers\net\ethernet\sun\sunhme.c | 985 | fuck | /* Only Sun can take such nice parts and fuck up the programming interface |
| kernel/drivers\net\fddi\skfp\h\supern_2.h | 774 | ass | #define	PL_LOOPBACK	0x0080		/* it cause the /LPBCK pin ass. low */ |
| kernel/drivers\net\fddi\skfp\h\supern_2.h | 775 | ass | #define	PL_MINI_CTR_INT 0x0100		/* partially contr. when bit is ass. */ |
| kernel/drivers\net\hamradio\6pack.c | 468 | crap | default:			/* gcc oh piece-o-crap ... */ |
| kernel/drivers\net\hamradio\scc.c | 1443 | Damn | * Damn, where is my Z8530 programming manual...? |
| kernel/drivers\net\wan\farsync.h | 344 | ass | * one of these then I've been an ass |
| kernel/drivers\net\wireless\ath\ath5k\desc.c | 197 | crap | * WEP crap |
| kernel/drivers\net\wireless\ath\ath5k\desc.c | 333 | crap | * WEP crap |
| kernel/drivers\net\wireless\atmel\at76c50x-usb.c | 188 | Dick | /* Dick Smith Electronics XH1153 802.11b USB adapter */ |
| kernel/drivers\net\wireless\broadcom\b43\phy_n.h | 679 | retard | #define B43_NPHY_PHYSTAT_ADVRET			B43_PHY_N(0x1F3) /* PHY stats ADV retard */ |
| kernel/drivers\net\wireless\broadcom\b43\wa.c | 127 | retard | static void b43_wa_art(struct b43_wldev *dev) /* ADV retard table */ |
| kernel/drivers\net\wireless\broadcom\brcm80211\brcmsmac\d11.h | 1500 | Retard | /* Advance Retard */ |
| kernel/drivers\net\wireless\broadcom\brcm80211\brcmsmac\main.c | 7864 | hell | /* ..now really unleash hell (allow the MAC out of suspend) */ |
| kernel/drivers\net\wireless\intel\iwlegacy\3945-mac.c | 3300 | shit | /* all this shit doesn't belong into sysfs anyway */ |
| kernel/drivers\net\wireless\realtek\rtl818x\rtl8187\dev.c | 69 | Dick | /* Dick Smith Electronics */ |
| kernel/drivers\net\wireless\silabs\wfx\traces.h | 21 | hell | /* The hell below need some explanations. For each symbolic number, we need to define it with |
| kernel/drivers\parport\parport_pc.c | 3131 | crap | *	Piles of crap below pretend to be a parser for module and kernel |
| kernel/drivers\pci\pci-driver.c | 497 | crap | * horrible the crap we have to deal with is when we are awake... |
| kernel/drivers\pinctrl\aspeed\pinmux-aspeed.h | 485 | hell | /* Macro hell */ |
| kernel/drivers\s390\char\tape_core.c | 76 | ASS | [TO_DIS] = "DIS",	[TO_ASSIGN] = "ASS", |
| kernel/drivers\s390\net\lcs.c | 1404 | Bloody | /* Bloody io subsystem tells us lies about cpa... */ |
| kernel/drivers\scsi\aha152x.c | 216 | damn | * first "damn thing doesn't work" version |
| kernel/drivers\scsi\aha1542.c | 956 | crap | * the strategy handler takes care of that crap. |
| kernel/drivers\scsi\dc395x.c | 3498 | crap | /* KG: Can this prevent crap sense data ? */ |
| kernel/drivers\scsi\qla1280.c | 3238 | damn | * This can be called from interrupt context, damn it!!! |
| kernel/drivers\scsi\qlogicpti.c | 810 | bullshit | if (qpti->clock == 0) /* bullshit */ |
| kernel/drivers\scsi\script_asm.pl | 763 | hell | # what the hell? |
| kernel/drivers\staging\media\atomisp\include\linux\atomisp.h | 394 | shit | /* GDC shit size [BQ] */ |
| kernel/drivers\tty\serial\pmac_zilog.c | 1435 | crap | * shadows so we don't write crap there before baud rate is |
| kernel/drivers\tty\serial\serial_core.c | 1032 | bitch | * instead of clearing it, then bitch about it. |
| kernel/drivers\tty\serial\sunsu.c | 930 | crap | * splitting all the OBP probing crap from the UART probing. |
| kernel/drivers\tty\serial\8250\8250_pci.c | 676 | hell | * Ugh, this is ugly as all hell --- TYT |
| kernel/drivers\usb\fotg210\fotg210-hcd.c | 2882 | ASS | /* Don't start the schedule until ASS is 0 */ |
| kernel/drivers\usb\fotg210\fotg210-hcd.c | 2895 | ASS | /* Don't turn off the schedule until ASS is 1 */ |
| kernel/drivers\usb\host\ehci-hcd.c | 639 | ASS | /* For Aspeed, STS_HALT also depends on ASS/PSS status. |
| kernel/drivers\usb\host\ehci-q.c | 958 | ASS | /* Don't start the schedule until ASS is 0 */ |
| kernel/drivers\usb\host\ehci-q.c | 972 | ASS | /* Don't turn off the schedule until ASS is 1 */ |
| kernel/drivers\usb\serial\ftdi_sio_ids.h | 748 | Dick | /* Note: OCT US101 is also rebadged as Dick Smith Electronics (NZ) XH6381 */ |
| kernel/drivers\usb\serial\ftdi_sio_ids.h | 749 | Dick | /* Also rebadged as Dick Smith Electronics (Aus) XH6451 */ |
| kernel/drivers\usb\storage\shuttle_usbat.c | 1347 | bloody | if (buffer == NULL) /* bloody hell! */ |
| kernel/drivers\usb\storage\shuttle_usbat.c | 1347 | hell | if (buffer == NULL) /* bloody hell! */ |
| kernel/drivers\video\fbdev\au1200fb.c | 1530 | damn | damn as to what the monitor specs are (the panel itself does, but that |
| kernel/drivers\video\fbdev\sstfb.c | 580 | crap | and as reading fbinit 6 will return crap (see FBIINIT6_DEFAULT) we just |
| kernel/drivers\video\fbdev\aty\radeon_pm.c | 284 | shit | /* Hrm... same shit, X doesn't do that but I have to */ |
| kernel/drivers\video\fbdev\sis\init301.c | 10029 | crap | /* This is a piece of typical SiS crap: They code the OEM LCD |
| kernel/drivers\watchdog\pc87413_wdt.c | 496 | bitch | *	resources we require and bitch if anyone beat us to them. |
| kernel/drivers\watchdog\wdt.c | 582 | bitch | *	resources we require and bitch if anyone beat us to them. |
| kernel/drivers\xen\platform-pci.c | 137 | hell | * as hell better process the event channel ports delivered |
| kernel/fs\namespace.c | 740 | bastard | int __legitimize_mnt(struct vfsmount *bastard, unsigned seq) |
| kernel/fs\namespace.c | 745 | bastard | if (bastard == NULL) |
| kernel/fs\namespace.c | 747 | bastard | mnt = real_mount(bastard); |
| kernel/fs\namespace.c | 752 | bastard | if (bastard->mnt_flags & MNT_SYNC_UMOUNT) { |
| kernel/fs\super.c | 1733 | Bollocks | * then a chunk of this can be removed.  [Bollocks -- AV] |
| kernel/fs\namespace.c | 757 | bastard | if (unlikely(bastard->mnt_flags & MNT_DOOMED)) { |
| kernel/fs\namespace.c | 768 | bastard | static bool legitimize_mnt(struct vfsmount *bastard, unsigned seq) |
| kernel/fs\namespace.c | 770 | bastard | int res = __legitimize_mnt(bastard, seq); |
| kernel/fs\namespace.c | 775 | bastard | mntput(bastard); |
| kernel/fs\namespace.c | 4025 | sucker | /* lock the sucker */ |
| kernel/fs\adfs\dir_f.c | 66 | bitch | * assembler, but a bitch in C...  This is one |
| kernel/fs\affs\Changes | 243 | Damn | 30 characters. (Damn it! This kind of bug |
| kernel/fs\bcachefs\btree_gc.h | 30 | crap | * position inside its cmpxchg loop, so crap magically works). |
| kernel/fs\bcachefs\btree_gc.c | 1091 | crap | *    various other crap: everything needs to agree on the ordering |
| kernel/fs\btrfs\file.c | 3084 | crap | /* Make sure we aren't being give some crap mode */ |
| kernel/fs\configfs\symlink.c | 188 | bastard | *  AV, a thoroughly annoyed bastard. |
| kernel/fs\jffs2\background.c | 110 | hell | * This forces the GCD to slow the hell down.   Pulling an |
| kernel/fs\jffs2\dir.c | 856 | shit | /* Oh shit. We really ought to make a single node which can do both atomically */ |
| kernel/fs\jffs2\gc.c | 424 | crap | all the iget() crap anyway */ |
| kernel/fs\jffs2\dir.c | 870 | sucker | * for that sucker and we have to trigger mount eviction - the |
| kernel/fs\notify\fsnotify.c | 129 | damn | * directory, there damn well better only be one item on this list */ |
| kernel/fs\ocfs2\cluster\heartbeat.c | 2208 | damn | * entire damn world #includes */ |
| kernel/fs\ocfs2\xattr.c | 2243 | sucker | * sane state.  Thus, even with errors we dirty the sucker. |
| kernel/fs\reiserfs\inode.c | 2401 | crap | /* crap, we are writing to a hole */ |
| kernel/fs\smb\client\dir.c | 880 | ass | * Here, we again ass|u|me that upper/lowercase versions of |
| kernel/fs\smb\client\inode.c | 1956 | sucker | * sucker and replace it with non-directory.  Return success, |
| kernel/include\asm-generic\memory_model.h | 25 | hell | /* avoid <linux/mm.h> include hell */ |
| kernel/include\asm-generic\preempt.h | 25 | hell | * must be macros to avoid header recursion hell |
| kernel/include\linux\preempt.h | 462 | hell | /* Macro to avoid header recursion hell vs. lockdep */ |
| kernel/include\linux\rcupdate.h | 165 | hell | * This is a macro rather than an inline function to avoid #include hell. |
| kernel/include\linux\timer.h | 36 | crap | * workqueue locking issues. It's not meant for executing random crap |
| kernel/include\linux\mtd\flashchip.h | 64 | damn | it'll make it a damn sight harder to find which chip we want from |
| kernel/include\scsi\scsi_host.h | 696 | crap | /* legacy crap */ |
| kernel/include\uapi\sound\asound.h | 63 | shit | unsigned char db5_dminh_lsv; /* downmix inhibit & level-shit values */ |
| kernel/kernel\audit_tree.c | 85 | sucker | * MSB of that sucker is stolen to mark taggings that we might have to |
| kernel/kernel\fork.c | 12 | bitch | * management can be a bitch. See 'mm/memory.c': 'copy_page_range()' |
| kernel/kernel\panic.c | 505 | CRAP | TAINT_FLAG(CRAP,			'C', ' ', true), |
| kernel/kernel\params.c | 214 | bastard | /* Lazy bastard, eh? */ |
| kernel/kernel\events\internal.h | 34 | crap | /* poll crap */ |
| kernel/kernel\irq\irqdomain.c | 932 | hell | * don't do it again, or hell will break loose. |
| kernel/kernel\locking\lockdep.c | 3967 | damn | * More smoking hash instead of calculating it, damn see these |
| kernel/kernel\module\main.c | 734 | damn | /* FIXME: if (force), slam module count damn the torpedoes */ |
| kernel/kernel\printk\printk.c | 225 | crap | * trailing crap... |
| kernel/kernel\sched\clock.c | 439 | crap | * TSC to be unstable, any computation will be computing crap. |
| kernel/kernel\sched\core.c | 5385 | bollocks | * IO-wait accounting, and how it's mostly bollocks (on SMP). |
| kernel/kernel\sched\fair.c | 4757 | Hell | * Hell(o) Nasty stuff.. we need to recompute _sum based on the new |
| kernel/kernel\time\posix-cpu-timers.c | 1193 | hell | * keep the callback static and to avoid header recursion hell. |
| kernel/lib\btree.c | 9 | ass | * see http://programming.kicks-ass.net/kernel-patches/vma_lookup/btree.patch |
| kernel/lib\test_linear_ranges.c | 12 | hell | /* First things first. I deeply dislike unit-tests. I have seen all the hell |
| kernel/lib\vsprintf.c | 624 | sucker | /* we want to pad the sucker */ |
| kernel/mm\swapfile.c | 3740 | hell | * out-of-line methods to avoid include hell. |
| kernel/net\8021q\vlan.c | 190 | sucker | /* So, got the sucker initialized, now lets place |
| kernel/net\8021q\vlan.c | 549 | sucker | /* Null terminate this sucker, just in case. */ |
| kernel/net\appletalk\ddp.c | 1431 | crap | * Size check to see if ddp->deh_len was crap |
| kernel/net\ceph\messenger_v1.c | 69 | hell | msg.msg_flags |= MSG_EOR;  /* superfluous, but what the hell */ |
| kernel/net\core\skbuff.c | 5335 | Fuck | /* Fuck, we are miserable poor guys... */ |
| kernel/net\ipv4\ah4.c | 97 | crap | case 0x85:	/* Some "Extended Security" crap. */ |
| kernel/net\ipv4\ip_input.c | 28 | crap | *					new frame it queues. Still crap because |
| kernel/net\ipv4\ip_gre.c | 136 | hell | what the hell these idiots break standards established |
| kernel/net\ipv4\ip_input.c | 462 | crap | /* When the interface is in promisc. mode, drop all the crap |
| kernel/net\ipv4\ip_gre.c | 227 | hell | * what the hell these idiots break standards established |
| kernel/net\ipv4\route.c | 3708 | damn | * We really need to sanitize the damn ipv4 init order, then all |
| kernel/net\ipv4\tcp_input.c | 977 | crap | /* Old crap is replaced with new one. 8) |
| kernel/net\ipv4\tcp_input.c | 991 | shit | *    all the algo is pure shit and should be replaced |
| kernel/net\llc\af_llc.c | 337 | hell | *	otherwise all hell will break loose. |
| kernel/net\llc\llc_input.c | 173 | crap | * When the interface is in promisc. mode, drop all the crap that it |
| kernel/net\netfilter\nf_conntrack_ftp.c | 212 | crap | else { /* Some other crap */ |
| kernel/net\netfilter\xt_hashlimit.c | 71 | crap | /* hash table crap */ |
| kernel/net\netfilter\xt_string.c | 44 | Damn | /* Damn, can't handle this case properly with iptables... */ |
| kernel/net\rds\ib_cm.c | 730 | crap | /* Even if len is crap *now* I still want to check it. -ASG */ |
| kernel/net\rxrpc\rtt.c | 120 | shit | *    all the algo is pure shit and should be replaced |
| kernel/net\unix\garbage.c | 58 | Damn | *		Damn. Added missing check for ->dead in listen queues scanning. |
| kernel/scripts\extract-ikconfig | 10 | Dick | # (c) 2009,2010 Dick Streefland <dick@streefland.net> |
| kernel/scripts\extract-vmlinux | 7 | Dick | # (c) 2009,2010 Dick Streefland <dick@streefland.net> |
| kernel/sound\aoa\soundbus\i2sbus\core.c | 250 | crap | * useless crap (ugh ugh ugh). We work around that here by calling |
| kernel/sound\isa\wavefront\wavefront_synth.c | 2118 | sucker | /* reset that sucker so that it doesn't bother us. */ |
| kernel/sound\pci\ad1889.c | 787 | dammit | ad1889_readl(chip, AD_DMA_DISR);	/* flush, dammit! */ |
| kernel/sound\pci\azt3328.c | 185 | crap | * Config switch, to use ALSA's AC97 layer instead of old custom mixer crap. |
| kernel/sound\pci\ens1370.c | 614 | dammit | /* wait for a SAFE time to write addr/data and then do it, dammit */ |
| kernel/sound\pci\azt3328.c | 616 | damn | (13), make damn sure |
| kernel/sound\pci\es1968.c | 1145 | crap | /* parallel in crap, see maestro reg 0xC [8-11] */ |
| kernel/sound\pci\ens1370.c | 657 | dammit | /* wait for a SAFE time to write addr/data and then do it, dammit */ |
| kernel/sound\pci\ac97\ac97_patch.c | 1311 | BLOODY | WHY CAN'T ANYONE FOLLOW THE BLOODY SPEC?  *sigh* |
| kernel/sound\pci\ac97\ac97_patch.c | 3642 | hell | * I have no idea what the hell Reserved does, but on an MSI |
| kernel/sound\pci\ac97\ac97_patch.c | 3644 | shit | * shit may happen. |
| kernel/sound\pci\au88x0\au88x0_core.c | 370 | crap | // FIXME: get rid of this crap. |
| kernel/sound\pci\cs46xx\dsp_spos_scb_lib.c | 206 | SHIT | /* !!!! THIS IS A PIECE OF SHIT MADE BY ME !!! */ |
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
| kernel/sound\soc\codecs\wm8994.c | 346 | hell | /* Icky as hell but saves code duplication */ |
| kernel/sound\soc\codecs\wm8996.c | 399 | hell | /* Icky as hell but saves code duplication */ |
| kernel/sound\soc\codecs\wm8994.c | 453 | hell | /* Icky as hell but saves code duplication */ |
| kernel/sound\usb\mixer.c | 1346 | crap | /* totally crap, return an error */ |
| kernel/tools\perf\builtin-c2c.c | 10 | Dick | *   Dick Fowles <fowles@inreach.com> |
| kernel/tools\perf\bench\futex-hash.c | 5 | hell | * futex-hash: Stress the hell out of the Linux kernel futex uaddr hashing. |
| kernel/tools\perf\Documentation\perf-c2c.txt | 335 | Dick | Although Don Zickus, Dick Fowles and Joe Mario worked together |
| kernel/tools\perf\trace\beauty\include\uapi\sound\asound.h | 63 | shit | unsigned char db5_dminh_lsv; /* downmix inhibit & level-shit values */ |
| kernel/tools\testing\selftests\net\psock_tpacket.c | 147 | crap | /* Lets create some broken crap, that still passes |
| kernel/tools\testing\selftests\net\af_unix\msg_oob.c | 385 | hell | recvpair("hell", 4, 4, 0); |
| kernel/tools\testing\selftests\net\af_unix\msg_oob.c | 396 | hell | recvpair("hell", 4, 5, 0);		/* Break at OOB even with enough buffer. */ |
| kernel/tools\testing\selftests\net\af_unix\msg_oob.c | 422 | hell | recvpair("hell", 4, 9, 0);		/* Break at OOB even after it's recv()ed. */ |
| kernel/tools\testing\selftests\net\af_unix\msg_oob.c | 441 | hell | recvpair("hell", 4, 10, 0);		/* Break at OOB even with enough buffer. */ |
| kernel/tools\testing\selftests\net\af_unix\msg_oob.c | 595 | hell | recvpair("hell", 4, 4, 0);		/* Intentionally stop at ex-OOB. */ |
| kernel/tools\testing\selftests\net\af_unix\msg_oob.c | 629 | hell | recvpair("hell", 4, 5, 0);		/* Break at OOB but not at ex-OOB. */ |
| kernel/tools\testing\selftests\net\af_unix\msg_oob.c | 654 | hell | recvpair("hell", 4, 9, 0);		/* Break at OOB even with enough buffer. */ |
| kernel/tools\testing\selftests\net\af_unix\msg_oob.c | 752 | hell | recvpair("hell", 4, 4, 0);		/* Intentionally stop at ex-OOB. */ |
| kernel/tools\testing\selftests\powerpc\signal\sig_sc_double_restart.c | 18 | sucker | *  that sucker at the same time.  Same for multiple signals of any kind |
| kernel/tools\testing\selftests\powerpc\signal\sig_sc_double_restart.c | 19 | sucker | *  interrupting that sucker on 64bit... |


Last updated: 2024-09-29 01:04:00
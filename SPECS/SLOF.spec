%define GITDATE        20210217

%global debug_package %{nil}

Name:       SLOF
Version:    %{GITDATE}
Release:    1%{?dist}
Summary:    Slimline Open Firmware
Group:      Applications/Emulators
License:    BSD
URL:        http://www.openfirmware.info/SLOF

Source0: https://github.com/aik/SLOF/archive/qemu-slof-20210217.tar.gz


BuildArch: noarch
ExclusiveArch: %{power64}

BuildRequires:  binutils
BuildRequires:  perl(Data::Dumper)

%description
Slimline Open Firmware (SLOF) is initialization and boot source code
based on the IEEE-1275 (Open Firmware) standard, developed by
engineers of the IBM Corporation.

The SLOF source code provides illustrates what's needed to initialize
and boot Linux or a hypervisor on the industry Open Firmware boot
standard.

Note that you normally wouldn't need to install this package
separately.  It is a dependency of qemu-system-ppc64.

%prep
%setup -q -n SLOF-qemu-slof-%{GITDATE}
%autopatch -p1

%build
export CROSS=""

# Workaround for problems on the TPS machines.  They have a
# environment variable called "RELEASE" which somehow confuses the
# SLOF Makefiles which also use a variable named RELEASE.
unset RELEASE

make qemu %{?_smp_mflags} V=2

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/qemu-kvm
install -c -m 0644 boot_rom.bin $RPM_BUILD_ROOT%{_datadir}/qemu-kvm/slof.bin

%files
%doc LICENSE
%doc README
%dir %{_datadir}/qemu-kvm
%{_datadir}/qemu-kvm/slof.bin

%changelog
* Thu Sep 2 2021 Danilo C. L. de Paula <ddepaula@redhat.com> - 20210217-1.el8
- Resolves: bz#2000225
  (Rebase virt:rhel module:stream based on AV-8.6)

* Mon Apr 27 2020 Danilo C. L. de Paula <ddepaula@redhat.com> - 20191022
- Resolves: bz#1810193
  (Upgrade components in virt:rhel module:stream for RHEL-8.3 release)

* Fri Jun 28 2019 Danilo de Paula <ddepaula@redhat.com> - 20171214-6.gitfa98132
- Rebuild all virt packages to fix RHEL's upgrade path
- Resolves: rhbz#1695587
  (Ensure modular RPM upgrade path)

* Fri Jan 04 2019 Danilo Cesar Lemes de Paula <ddepaula@redhat.com> - 20171214-5.gitfa98132.el8
- slof-board-qemu-slof-vio-vscsi-Scan-up-to-64-SCSI-IDs.patch [bz#1655649]
- slof-usb-storage-Invert-the-logic-of-the-IF-statements.patch [bz#1654196]
- slof-usb-storage-Implement-block-write-support.patch [bz#1654196]
- Resolves: bz#1654196
  ([RHEL8.0][USB]  guest failed to boot from emulated usb-storage)
- Resolves: bz#1655649
  (RHEL8.0 - ISST-LTE:KVM:Failed to boot the guest from cdrom drive)

* Fri Aug 10 2018 Danilo Cesar Lemes de Paula <ddepaula@redhat.com> - 20171214-4.gitfa98132.el8
- slof-libelf-Add-REL32-to-the-list-of-ignored-relocations.patch [bz#1613619]
- slof-Fix-bad-assembler-statements-for-compiling-with-gcc-.patch [bz#1613619]
- slof-make.rules-Compile-SLOF-with-fno-asynchronous-unwind.patch [bz#1613619]
- slof-romfs-tools-Remove-superfluous-union-around-the-rom-.patch [bz#1613619]
- slof-romfs-tools-Silence-GCC-8.1-compiler-warning-with-FL.patch [bz#1613619]
- slof-romfs-tools-Silence-more-compiler-warnings-with-GCC-.patch [bz#1613619]
- Resolves: bz#1613619
  ([RHEL8.0]Console contains error message (ERROR: Unhandled relocation (A) type 26) after continuing a guest)
- Resolves: bz#1600154
  (SLOF needs to be build in power hosts)


* Wed Jul 11 2018 Danilo Cesar Lemes de Paula - 20171214-3.gitfa98132.el8
- Release to RHEL-8.0

* Fri Jun 01 2018 Miroslav Rezanina <mrezanin@redhat.com> - 20171214-2.gitfa98132.el7
- slof-Fix-output-word.patch [bz#1495467]
- slof-resolve-ihandle-and-xt-handle-in-the-input-command-l.patch [bz#1495467]
- Resolves: bz#1495467
  (SLOF does not honour output-path environment variable)

* Wed Apr 18 2018 Miroslav Rezanina <mrezanin@redhat.com> - 20171214-1.gitfa98132.el7
- Rebase to qemu-slof-20171214 [bz#1562106]
- Resolves: bz#1562106
  (Rebase SLOF for RHEL-7.6)

* Mon Oct 09 2017 Miroslav Rezanina <mrezanin@redhat.com> - 20170724-2.git89f519f.el7
- slof-virtio-net-rework-the-driver-to-support-multiple-ope.patch [bz#1477937]
- Resolves: bz#1477937
  (VM fails to boot at SLOF prompt with "Out of internal memory." with lots of virtio-net-pci devices)

* Mon Oct 02 2017 Miroslav Rezanina <mrezanin@redhat.com> - 20170724-1.git89f519f.el7
- Rebase to qemu-slof-20170724 [bz#1471284]
- Resolves: bz#1471284
  (Rebase SLOF for RHEL-7.5)

* Fri May 19 2017 Miroslav Rezanina <mrezanin@redhat.com> - 20170303-4.git66d250e.el7
- slof-pci-Reserve-free-space-at-the-end-of-bridge-windows-.patch [bz#1443433]
- Resolves: bz#1443433
  ([ppc64le] Guest failed to boot up with 8 nested pci-bridge)

* Fri May 05 2017 Miroslav Rezanina <mrezanin@redhat.com> - 20170303-3.git66d250e.el7
- slof-pci-Put-non-prefetchable-64bit-BARs-into-32bit-MMIO-.patch [bz#1442930]
- slof-pci-Fix-assigned-addresses-for-64bit-nonprefetchable.patch [bz#1442930]
- slof-pci-phb-Set-pci-max-mem64-to-the-correct-value.patch [bz#1442930]
- slof-pci-Generate-a-64-bit-range-property-if-necessary.patch [bz#1442930]
- Resolves: bz#1442930
  ([ppc64le] BARs are incorrectly assigned for some devices under P2P bridges)

* Fri Apr 28 2017 Miroslav Rezanina <mrezanin@redhat.com> - 20170303-2.git66d250e.el7
- slof-logo-Update-the-logo.patch [bz#1443904]
- slof-Rework-the-printing-of-the-banner-during-boot.patch [bz#1443904]
- Resolves: bz#1443904
  (SLOF user interface display bootable device and "SLOF" words duplicate)

* Thu Mar 09 2017 Miroslav Rezanina <mrezanin@redhat.com> - 20170303-0.git66d250e.el7
- Rebaes to SLOF version used by QEMU 2.9 [bz#1392055]
- Resolves: bz#1392055
  (Rebase SLOF for RHEL-7.4)

* Fri Aug 05 2016 Miroslav Rezanina <mrezanin@redhat.com> - 20160223-6.gitdbbfda4.el7
- slof-usb-Move-XHCI-port-state-arrays-from-header-to-.c-fi.patch [bz#1352765]
- slof-usb-Increase-amount-of-maximum-slot-IDs-and-add-a-sa.patch [bz#1352765]
- slof-usb-Initialize-USB3-devices-on-a-hub-and-keep-track-.patch [bz#1352765]
- slof-usb-Build-correct-route-string-for-USB3-devices-behi.patch [bz#1352765]
- slof-usb-Set-XHCI-slot-speed-according-to-port-status.patch [bz#1352765]
- Resolves: bz#1352765
  (SLOF can not handle devices attached to an XHCI USB hub)

* Tue Jul 26 2016 Miroslav Rezanina <mrezanin@redhat.com> - 20160223-5.gitdbbfda4.el7
- slof-usb-hid-Fix-non-working-comma-key.patch [bz#1352821]
- Resolves: bz#1352821
  (Key  "," can not be inputted during SLOF and yaboot stage)

* Tue Jun 07 2016 Miroslav Rezanina <mrezanin@redhat.com> - 20160223-4.gitdbbfda4.el7
- slof-xhci-add-memory-barrier-after-filling-the-trb.patch [bz#1339528]
- slof-xhci-fix-missing-keys-from-keyboard.patch [bz#1339528]
- slof-Improve-F12-key-handling-in-boot-menu.patch [bz#1339528]
- Resolves: bz#1339528
  (SLOF boot menu gets delayed if press 'F12' key for multiple times)

* Wed May 11 2016 Miroslav Rezanina <mrezanin@redhat.com> - 20160223-3.gitdbbfda4.el7
- slof-ipv6-Do-not-use-unitialized-MAC-address-array.patch [bz#1287716]
- slof-ipv6-send_ipv6-has-to-return-after-doing-NDP.patch [bz#1287716]
- slof-ipv6-Fix-possible-NULL-pointer-dereference-in-send_i.patch [bz#1287716]
- slof-ipv6-Clear-memory-after-malloc-if-necessary.patch [bz#1287716]
- slof-ipv6-Fix-memory-leak-in-set_ipv6_address-ip6_create_.patch [bz#1287716]
- slof-ipv6-Indent-code-with-tabs-not-with-spaces.patch [bz#1287716]
- slof-ipv6-Fix-NULL-pointer-dereference-in-ip6addr_add.patch [bz#1287716]
- slof-ipv6-Replace-magic-number-1500-with-ETH_MTU_SIZE-i.e.patch [bz#1287716]
- Resolves: bz#1287716
  (IPv6 boot support in SLOF)

* Fri May 06 2016 Miroslav Rezanina <mrezanin@redhat.com> - 20160223-2.gitdbbfda4.el7
- slof-dev-null-The-read-function-has-to-return-0-if-nothin.patch [bz#1310737]
- slof-ipv6-Add-support-for-sending-packets-through-a-route.patch [bz#1301081]
- slof-virtio-net-initialize-to-populate-mac-address.patch [bz#1331698]
- Resolves: bz#1301081
  (IPv6 boot does not work in SLOF when TFTP server is behind a router)
- Resolves: bz#1310737
  (SLOF cannot boot without a console)
- Resolves: bz#1331698
  (Network booting in grub fails when using virtio-net and SLOF-20160223-0)

* Fri Sep 18 2015 Miroslav Rezanina <mrezanin@redhat.com> - 20150313-5.gitc89b0df.el7
- slof-pci-Use-QEMU-created-PCI-device-nodes.patch [bz#1250326]
- Resolves: bz#1250326
  (vfio device can't be hot unplugged on powerpc guest)

* Wed Sep 16 2015 Miroslav Rezanina <mrezanin@redhat.com> - 20150313-4.gitc89b0df.el7
- slof-cas-Increase-FDT-buffer-size-to-accomodate-larger-ib.patch [bz#1263039]
- slof-Downstream-only-Correctly-set-ibm-my-drc-index.patch [bz#1250326]
- Resolves: bz#1250326
  (vfio device can't be hot unplugged on powerpc guest)
- Resolves: bz#1263039
  (SLOF doesn't allow enough room for CAS response with large maxmem)

* Thu Aug 06 2015 Miroslav Rezanina <mrezanin@redhat.com> - 20150313-3.gitc89b0df.el7
- slof-fbuffer-Improve-invert-region-helper.patch [bz#1237052]
- slof-fbuffer-Use-a-smaller-cursor.patch [bz#1237052]
- slof-terminal-Disable-the-terminal-write-trace-by-default.patch [bz#1237052]
- slof-fbuffer-Precalculate-line-length-in-bytes.patch [bz#1237052]
- slof-fbuffer-Implement-MRMOVE-as-an-accelerated-primitive.patch [bz#1237052]
- slof-fbuffer-Implement-RFILL-as-an-accelerated-primitive.patch [bz#1237052]
- slof-Add-missing-half-word-access-case-to-_FASTRMOVE-and-.patch [bz#1237052]
- Resolves: bz#1237052
  (Curser movement issue - the curser would move right and left before get its position in grub interface of a qemu-kvm guest)

* Tue Jun 09 2015 Miroslav Rezanina <mrezanin@redhat.com> - 20150313-2.gitc89b0df.el7
- slof-fbuffer-simplify-address-computations-in-fb8-toggle-.patch [bz#1212256]
- slof-fbuffer-introduce-the-invert-region-helper.patch [bz#1212256]
- slof-fbuffer-introduce-the-invert-region-x-helper.patch [bz#1212256]
- slof-spec-Remove-FlashingSLOF.pdf.patch [bz#1226264]
- Resolves: bz#1212256
  ([Power KVM] Grub interface of guest response slow)
- Resolves: bz#1226264
  (Remove FlashingSLOF.pdf)

* Thu May 28 2015 Miroslav Rezanina <mrezanin@redhat.com> - 20150313-1.gitc89b0df
- rebase to 20150313 version
- Resolves: bz#1225720
  (Update SLOF package to match current qemu-kvm-rhev package)

* Tue Jan 27 2015 Miroslav Rezanina <mrezanin@redhat.com> - 20140630-4.gitf284ab3
- slof-Downstream-only-Workaround-for-TPS-environment-oddit.patch [bz#1183927]
- Resolves: bz#1183927
  (TPS srpm rebuild test failure for SLOF)

* Fri Nov 14 2014 Miroslav Rezanina <mrezanin@redhat.com> - 20140630-3.gitf284ab3
- slof-net-snk-use-socket-descriptor-in-the-network-stack.patch [bz#1158217]
- slof-ipv4-Fix-send-packet-across-a-subnet.patch [bz#1158217]
- Resolves: bz#1158217
  (SLOF can not reach tftp server on different subnet)

* Thu Aug 28 2014 Miroslav Rezanina <mrezanin@redhat.com> - 20140630-2.gitf284ab3
- building as noarch

* Tue Jun 24 2014 Miroslav Rezanina <mrezanin@redhat.com> - 20140630-1.gitf284ab3
- Initial version

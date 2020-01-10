Name:		openocd
Version:	0.8.0
Release:	1
Summary:	Debugging, in-system programming and boundary-scan testing for embedded devices

Group:		Development/Other
License:	GPLv2
URL:		http://sourceforge.net/projects/openocd
Source0:	http://downloads.sourceforge.net/project/openocd/openocd/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(hidapi-hidraw)
BuildRequires:	pkgconfig(libftdi1)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	sdcc

%description
The Open On-Chip Debugger (OpenOCD) provides debugging, in-system programming 
and boundary-scan testing for embedded devices.  Various different boards, 
targets, and interfaces are supported to ease development time.

Install OpenOCD if you are looking for an open source solution for hardware 
debugging.

%prep
%setup -q
%autopatch -p1

rm src/jtag/drivers/OpenULINK/ulink_firmware.hex

cd doc
iconv -f iso8859-1 -t utf-8 openocd.info > openocd.info.conv
mv -f openocd.info.conv openocd.info

%build
pushd src/jtag/drivers/OpenULINK
%make hex
popd

%configure	--disable-werror \
		--enable-static \
		--disable-shared \
		--enable-dummy \
		--enable-gw16012 \
		--enable-parport \
		--enable-parport_ppdev \
		--enable-presto_libftdi \
		--enable-amtjtagaccel \
		--enable-armjtagew \
		--enable-jlink \
		--enable-rlink \
		--enable-stlink \
		--enable-ulink \
		--enable-usbprog \
		--enable-vsllink \
		--enable-oocd_trace \
		--enable-ep39xx \
		--enable-at91rm9200 \
		--disable-doxygen-html \
		--enable-ftdi \
		--enable-ti-icdi \
		--enable-osbdm \
		--enable-opendous \
		--enable-aice \
		--enable-usbprog \
		--enable-cmsis-dap \
		--enable-jtag_vpi \
		--enable-usb_blaster_libftdi \
		--enable-usb-blaster-2 \
		--enable-zy1000-master \
		--enable-ioutil\
		--enable-ep93xx \
		--enable-at91rm9200 \
		--enable-bcm2835gpio \
		--enable-openjtag_ftdi \
		--enable-oocd_trace \
		--enable-buspirate \
		--enable-sysfsgpio \
		--enable-remote-bitbang
%make

%install
%makeinstall_std

%files
%doc README AUTHORS ChangeLog NEWS TODO
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_bindir}/%{name}
%{_infodir}/%{name}.info*
%{_mandir}/man1/*

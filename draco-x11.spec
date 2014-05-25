%define debug_package %{nil}

Name:           draco-x11
Version:        1.0
Release:        2.draco1
Summary:        X11 Window System
Group:          System Environment/Base
License:        GPLv2
Provides:	draco-x11

BuildArch:noarch
Requires:draco-base
Requires:eggdbus
Requires:hdparm
Requires:dmidecode
Requires:cryptsetup-luks
Requires:cryptsetup-luks-libs
Requires:pm-utils
Requires:polkit
Requires:slim
Requires:ConsoleKit
Requires:ConsoleKit-libs
Requires:ConsoleKit-x11
Requires:dbus
Requires:dbus-python
Requires:dbus-x11
Requires:hal
Requires:hal-info
Requires:hal-libs
Requires:libjpeg-turbo
Requires:libmcpp
Requires:libpng
Requires:libxkbfile
Requires:mcpp
Requires:mtdev
Requires:system-setup-keyboard

Requires:libXScrnSaver
Requires:dejavu-sans-fonts
Requires:dejavu-sans-mono-fonts
Requires:dejavu-serif-fonts
Requires:fontconfig
Requires:fontpackages-filesystem
Requires:freetype
Requires:glx-utils
Requires:libdmx
Requires:liberation-mono-fonts
Requires:liberation-sans-fonts
Requires:liberation-serif-fonts
Requires:libfontenc
Requires:libICE
Requires:libSM
Requires:libX11
Requires:libX11-common
Requires:libXau
Requires:libXaw
Requires:libxcb
Requires:libXcomposite
Requires:libXcursor
Requires:libXdamage
Requires:libXdmcp
Requires:libXext
Requires:libXfixes
Requires:libXfont
Requires:libXft
Requires:libXi
Requires:libXinerama
Requires:libXmu
Requires:libXpm
Requires:libXrandr
Requires:libXrender
Requires:libXt
Requires:libXtst
Requires:libXv
Requires:libXvMC
Requires:libXxf86dga
Requires:libXxf86misc
Requires:libXxf86vm
Requires:mesa-dri1-drivers
Requires:mesa-dri-drivers
Requires:mesa-dri-filesystem
Requires:mesa-libEGL
Requires:mesa-libgbm
Requires:mesa-libGL
Requires:mesa-libGLU
Requires:mesa-private-llvm
Requires:pixman
Requires:xcb-util
Requires:xkeyboard-config
Requires:xorg-x11-apps
Requires:xorg-x11-drivers
Requires:xorg-x11-drv-acecad
Requires:xorg-x11-drv-aiptek
Requires:xorg-x11-drv-apm
Requires:xorg-x11-drv-ast
Requires:xorg-x11-drv-ati
Requires:xorg-x11-drv-ati-firmware
Requires:xorg-x11-drv-cirrus
Requires:xorg-x11-drv-dummy
Requires:xorg-x11-drv-elographics
Requires:xorg-x11-drv-evdev
Requires:xorg-x11-drv-fbdev
Requires:xorg-x11-drv-fpit
Requires:xorg-x11-drv-glint
Requires:xorg-x11-drv-hyperpen
Requires:xorg-x11-drv-i128
Requires:xorg-x11-drv-i740
Requires:xorg-x11-drv-intel
Requires:xorg-x11-drv-keyboard
Requires:xorg-x11-drv-mach64
Requires:xorg-x11-drv-mga
Requires:xorg-x11-drv-modesetting
Requires:xorg-x11-drv-mouse
Requires:xorg-x11-drv-mutouch
Requires:xorg-x11-drv-nouveau
Requires:xorg-x11-drv-nv
Requires:xorg-x11-drv-openchrome
Requires:xorg-x11-drv-penmount
Requires:xorg-x11-drv-qxl
Requires:xorg-x11-drv-r128
Requires:xorg-x11-drv-rendition
Requires:xorg-x11-drv-s3virge
Requires:xorg-x11-drv-savage
Requires:xorg-x11-drv-siliconmotion
Requires:xorg-x11-drv-sis
Requires:xorg-x11-drv-sisusb
Requires:xorg-x11-drv-synaptics
Requires:xorg-x11-drv-tdfx
Requires:xorg-x11-drv-trident
Requires:xorg-x11-drv-v4l
Requires:xorg-x11-drv-vesa
Requires:xorg-x11-drv-vmmouse
Requires:xorg-x11-drv-vmware
Requires:xorg-x11-drv-void
Requires:xorg-x11-drv-voodoo
Requires:xorg-x11-drv-wacom
Requires:xorg-x11-drv-xgi
Requires:xorg-x11-fonts-misc
Requires:xorg-x11-font-utils
Requires:xorg-x11-glamor
Requires:xorg-x11-server-common
Requires:xorg-x11-server-utils
Requires:xorg-x11-server-Xorg
Requires:xorg-x11-utils
Requires:xorg-x11-xauth
Requires:xorg-x11-xinit
Requires:xorg-x11-xinit-session
Requires:xorg-x11-xkb-utils
Requires:xterm
Requires:fluxbox


%description
X11 Window System

%build
echo OK

%files
%defattr(-,root,root)

%changelog

%define debug_package %{nil}

Name:           draco-desktop
Version:        1.0
Release:        9.draco1
Summary:        Linux Desktop System
Group:          System Environment/Base
License:        GPLv2
Provides:	draco-desktop

BuildArch:noarch
Requires:desktop-file-utils
Requires:draco-firstboot
Requires:pinentry-gtk
Requires:plymouth-theme-rings
Requires:alsa-utils
Requires:draco-x11
Requires:wicd-gtk
Requires:gtk2-engines
Requires:gnome-icon-theme
Requires:firefox
Requires:Terminal
Requires:Thunar
Requires:powertray
Requires:DracoPKG
Requires:smplayer
Requires:smplayer-skins
Requires:hal-storage-addon

%description
Linux Desktop System

%build
echo OK

%files
%defattr(-,root,root)

%changelog

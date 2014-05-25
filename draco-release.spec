# Anaconda looks here for images
%define anaconda_image_prefix /usr/lib/anaconda-runtime

%define debug_package %{nil}
%define product_family DracoLinux
%define release_name Final
%define base_release_version 1
%define full_release_version 1.0

Name:           draco-release
Version:        %{full_release_version}
Release:        2%{dist}
Summary:        %{product_family} release file
Group:          System Environment/Base
License:        GPLv2
Obsoletes:      rawhide-release centos-release redhat-release-as redhat-release-es redhat-release-ws redhat-release-de comps rpmdb-redhat fedora-release redhat-release oraclelinux-release sl-release
Provides:	redhat-release
Provides:	system-release
Provides:	centos-release
Obsoletes:	indexhtml <= 2:5-1
Provides:	redhat-indexhtml
Provides:	centos-indexhtml
Provides:       system-bookmarks
Provides:	redhat-bookmarks
Obsoletes:	centos-indexhtml
Obsoletes:	redhat-bookmarks
Obsoletes:	system-gnome-theme
Provides:	system-gnome-theme
Conflicts:	anaconda-images <= 10
Provides:	system-logos = %{version}-%{release}
Obsoletes:	desktop-backgrounds-basic <= 60.0.1-1.el6
#Provides:	desktop-backgrounds-basic = %{version}-%{release}
Provides:	CentOS-logos, centos-logos
Conflicts:	redhat-artwork <= 5.0.5
Source0:        draco-release-1.0.tar.gz
Requires:	draco-repo
BuildArch: noarch

%description
%{product_family} release files

%prep
%setup -q

%build
echo OK

%install
rm -rf $RPM_BUILD_ROOT

# create /etc
mkdir -p $RPM_BUILD_ROOT/etc

# create /etc/system-release and /etc/redhat/release
echo "%{product_family} release %{full_release_version}%{?beta: %{beta}} (%{release_name})" > $RPM_BUILD_ROOT/etc/draco-release
ln -s draco-release $RPM_BUILD_ROOT/etc/redhat-release
ln -s draco-release $RPM_BUILD_ROOT/etc/system-release
ln -s draco-release $RPM_BUILD_ROOT/etc/centos-release

# write cpe to /etc/system/release-cpe
echo "cpe:/o:draco:linux:%{version}:%{?beta:%{beta}}%{!?beta:GA}" > $RPM_BUILD_ROOT/etc/system-release-cpe

# create /etc/issue and /etc/issue.net
cp $RPM_BUILD_ROOT/etc/redhat-release $RPM_BUILD_ROOT/etc/issue
echo "Kernel \r on an \m" >> $RPM_BUILD_ROOT/etc/issue
cp $RPM_BUILD_ROOT/etc/issue $RPM_BUILD_ROOT/etc/issue.net
echo >> $RPM_BUILD_ROOT/etc/issue

# copy yum repos to /etc/yum.repos.d
#mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
#for file in *.repo; do
#    install -m 644 $file $RPM_BUILD_ROOT/etc/yum.repos.d
#done

# copy GPG keys
mkdir -p -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
for file in RPM-GPG-KEY* ; do
    install -m 644 $file $RPM_BUILD_ROOT/etc/pki/rpm-gpg
done

# set up the dist tag macros
install -d -m 755 $RPM_BUILD_ROOT/etc/rpm
cat >> $RPM_BUILD_ROOT/etc/rpm/macros.dist << EOF
# dist macros.

%%draco %{base_release_version}
%%draco_ver %{base_release_version}
%%dist .draco%{base_release_version}
%%draco%{base_release_version} 1
EOF

mkdir -p ${RPM_BUILD_ROOT}%{_defaultdocdir}
ln -s /usr/share/doc/draco-release-1.5 ${RPM_BUILD_ROOT}%{_defaultdocdir}/redhat-release

# should be ifarch i386
mkdir -p $RPM_BUILD_ROOT/boot/grub
install -p -m 644 -D bootloader/splash.xpm.gz $RPM_BUILD_ROOT/boot/grub/splash.xpm.gz
# end i386 bits

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/redhat
for i in redhat-pixmaps/*; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps/redhat
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/
for i in backgrounds/*.png backgrounds/default.xml; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/backgrounds/
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/
install -p -m 644 backgrounds/desktop-backgrounds-default.xml $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/RHEL
for i in firstboot/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/RHEL
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/rings
for i in plymouth/rings/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/rings
done

mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML
echo "<html><head><meta http-equiv=\"refresh\" content=\"0; url=http://dracolinux.org\" /></head><body></body></html>" > $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/index.html
mkdir -p $RPM_BUILD_ROOT/usr/share/bookmarks/
echo "" > $RPM_BUILD_ROOT/usr/share/bookmarks/default-bookmarks.html

mkdir -p $RPM_BUILD_ROOT/etc/skel $RPM_BUILD_ROOT/root
cp -a skel/.mozilla $RPM_BUILD_ROOT/etc/skel/
cp -a skel/.mozilla $RPM_BUILD_ROOT/root/

cp -a skel/.config $RPM_BUILD_ROOT/etc/skel/
cp -a skel/.config $RPM_BUILD_ROOT/root/

cp skel/.gtkrc-2.0 $RPM_BUILD_ROOT/etc/skel/
cp skel/.gtkrc-2.0 $RPM_BUILD_ROOT/root/

mkdir -p $RPM_BUILD_ROOT/etc/gtk-2.0
cat gtkrc > $RPM_BUILD_ROOT/etc/gtk-2.0/gtkrc

mkdir -p $RPM_BUILD_ROOT/usr/share/themes/Draco/gtk-2.0
cat draco-gtkrc > $RPM_BUILD_ROOT/usr/share/themes/Draco/gtk-2.0/gtkrc

(cd anaconda; make DESTDIR=$RPM_BUILD_ROOT install)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc EULA GPL 
%attr(0644,root,root) /etc/redhat-release
%attr(0644,root,root) /etc/centos-release
%attr(0644,root,root) /etc/draco-release
/etc/gtk-2.0/gtkrc
/etc/system-release
%{_defaultdocdir}/HTML/index.html
/usr/share/bookmarks/default-bookmarks.html
%config %attr(0644,root,root) /etc/system-release-cpe
%config(noreplace) %attr(0644,root,root) /etc/issue
%config(noreplace) %attr(0644,root,root) /etc/issue.net
#%config %attr(0644,root,root) /etc/yum.repos.d/*
%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/*
/etc/skel/.mozilla/*
/etc/skel/.config/*
/etc/skel/.gtkrc-2.0
/root/.mozilla/*
/root/.config/*
/root/.gtkrc-2.0
/usr/share/themes/Draco/gtk-2.0/gtkrc
/etc/rpm/macros.dist
%_defaultdocdir/redhat-release
%{_datadir}/backgrounds/*
%{_datadir}/gnome-background-properties/*
%{_datadir}/firstboot/themes/RHEL/
%{_datadir}/plymouth/themes/rings/
%{_datadir}/pixmaps/*
%{_datadir}/anaconda/pixmaps/*
%{anaconda_image_prefix}/boot/*png
%{anaconda_image_prefix}/*.sh
%{anaconda_image_prefix}/*.jpg
%dir %{anaconda_image_prefix}
%dir %{anaconda_image_prefix}/boot
%dir %{_datadir}/anaconda
%dir %{_datadir}/anaconda/pixmaps/
/boot/grub/splash.xpm.gz

%changelog
* Sat Nov 30 2013 Karanbir Singh <kbsingh@centos.org> - 6.5.el6.centos.11.2
- Add CentOS-6.4 repo defs to CentOS-Vault.repo

* Tue Nov 26 2013 Karanbir Singh <kbsingh@centos.org> - 6.5.el6.centos.11.1
- Build for CentOS-6.5

* Mon Feb 25 2013 Karanbir Singh <kbsingh@centos.org> - 6.4.el6.centos.10
- Build for CentOS-6.4

* Mon Jun 25 2012 Karanbir Singh <kbsingh@centos.org> - 6-3.el6.centos.9
- Bump version to 6.3 as well

* Fri Jun 22 2012 Karanbir Singh <kbsingh@centos.org> - 6-3.el6.centos.8
- Build for CentOS 6.3

* Thu Dec  8 2011 Karanbir Singh <kbsingh@centos.org> - 6-2.el6.centos.org.7
- Build for CentOS-6.2

* Wed Aug 31 2011 Karanbir Singh <kbsingh@centos.org> - 6-1.el6.centos.5
- Build for CentOS 6.1

* Sat Jul  2 2011 Karanbir Singh <kbsingh@centos.org> - 6-0.el6.centos.5
- Add in Keys

* Wed Jun 29 2011 Karanbir Singh <kbsingh@centos.org> - 6-0.el6.centos.3
- we need the upstream release dir since other apps and vendors rely on it

* Tue Jun  7 2011 Karanbir Singh <kbsingh@centos.org> - 6-0.el6.centos.2
- Make sure we have a Provides for redhat-release

* Sat Feb 19 2011 Karanbir Singh <kbsingh@centos.org> - 6-0.el6.centos.1
- Adapt to CentOS Linux 6


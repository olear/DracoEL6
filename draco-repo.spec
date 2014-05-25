%define debug_package %{nil}

Name:           draco-repo
Version:        1.0
Release:        1%{dist}
Summary:        System repository
Group:          System Environment/Base
License:        GPLv2
Provides:	draco-repo
Source0:	draco.repo
BuildArch:	noarch
URL:		http://www.dracolinux.org
Packager:	Ole Andre Rodlie, <olear@dracolinux.org>
Vendor:		DracoLinux, http://dracolinux.org

%description
System repository

%build
echo OK

%install
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT/etc/yum.repos.d/draco.repo

%files
%defattr(-,root,root)
%config %attr(0644,root,root) /etc/yum.repos.d/draco.repo

%changelog

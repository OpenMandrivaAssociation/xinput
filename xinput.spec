Name:		xinput
Version:	1.3.0
Release:	%mkrel 2
Summary:	Runtime configuration and test of XInput devices
Group:		System/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/app/xinput  xorg/app/xinput
# cd xorg/app/xinput
# git-archive --format=tar --prefix=xinput-1.3.0/ xinput-1.3.0 | bzip2 -9 > xinput-1.3.0.tar.bz2
########################################################################
Source0: %{name}-%{version}.tar.bz2
License:	MIT
########################################################################
# git-format-patch xinput-1.3.0..origin/mandriva
Patch1: 0001-Apply-patch-from-existing-xinput-package-to-freede.patch
########################################################################
BuildRoot:	%{_tmppath}/%{name}-droot

BuildRequires:	x11-util-macros		>= 1.1.5
BuildRequires:	libx11-devel		>= 1.1.3
BuildRequires:	libxext-devel		>= 1.0.3

%description
Runtime configuration and test of XInput devices

%prep
%setup -q

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xinput
%{_mandir}/*/*
%doc README ChangeLog

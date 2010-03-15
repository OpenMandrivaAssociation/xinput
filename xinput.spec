Name:		xinput
Version:	1.5.1
Release:	%mkrel 1
Summary:	Runtime configuration and test of XInput devices
Group:		System/X11
URL:		http://xorg.freedesktop.org
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-droot
BuildRequires:	x11-util-macros		>= 1.1.5
BuildRequires:	libx11-devel		>= 1.1.3
BuildRequires:	libxext-devel		>= 1.0.3
BuildRequires:	libxi-devel		>= 1.1.3

%description
Runtime configuration and test of XInput devices

%prep
%setup -q

%build
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

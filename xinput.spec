Name:		xinput
Version:	1.6.4
Release:	1
Summary:	Runtime configuration and test of XInput devices
Group:		System/X11
URL:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(x11) >= 1.1.3
BuildRequires:	pkgconfig(xext) >= 1.0.3
BuildRequires:	pkgconfig(xi) >= 1.1.3
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)

%description
Runtime configuration and test of XInput devices.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xinput
%doc %{_mandir}/*/*
%doc README ChangeLog

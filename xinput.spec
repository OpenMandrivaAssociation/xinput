%define	name	xinput
%define version	1.2
%define release	%mkrel 10

Summary:	Runtime configuration and test of XInput devices
Name:		%{name}
Version:	%{version}
Release:	%{release}

Source0:	ftp://ftp.x.org/contrib/utilities/%{name}-%{version}.tar.bz2
Patch0:		xinput-1.2-loop.patch

License:	MIT
Group:		System/X11
BuildRequires:	imake
BuildRequires:	X11-devel
BuildRequires:	gccmakedep

%description
Runtime configuration and test of XInput devices

%prep
%setup -q
%patch0 -p1 -b .loop

%build
xmkmf -a
perl -p -i -e "s|CXXDEBUGFLAGS = .*|CXXDEBUGFLAGS = $RPM_OPT_FLAGS|" Makefile
perl -p -i -e "s|CDEBUGFLAGS = .*|CDEBUGFLAGS = $RPM_OPT_FLAGS|" Makefile
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std} MANDIR=%{_mandir}/man install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/xinput
%{_mandir}/*/*
%doc README COPYRIGHT ChangeLog



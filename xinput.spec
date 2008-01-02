Name:		xinput
Version:	1.3.0
Release:	%mkrel 1
Summary:	Runtime configuration and test of XInput devices
Group:		System/X11

##Only commenting original tarball until freedesktop tarball is made available
##Source0:	ftp://ftp.x.org/contrib/utilities/%{name}-%{version}.tar.bz2

# Note local tag xinput-1.3.0@mandriva suggested on upstream
# Tag at git checkout 82dfa529165657edc4e66e072d1515638e1edc66
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/app/xinput  xorg/app/xinput
# cd xorg/app/xinput
# git-archive --format=tar --prefix=xinput-1.3.0/ xinput-1.3.0@mandriva | bzip2 -9 > xinput-1.3.0.tar.bz2
########################################################################
Source0: %{name}-%{version}.tar.bz2
########################################################################
# git-format-patch xinput-1.3.0@mandriva..origin/mandriva+gpl
Patch1: 0001-Apply-patch-from-existing-xinput-package-to-freede.patch
########################################################################
License:	MIT
BuildRequires:	x11-util-macros
BuildRequires:	imake
BuildRequires:	X11-devel
BuildRequires:	gccmakedep
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

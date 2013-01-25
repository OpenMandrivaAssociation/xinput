Name:		xinput
Version:	1.6.0
Release:	4
Summary:	Runtime configuration and test of XInput devices
Group:		System/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRequires:	x11-util-macros		>= 1.1.5
BuildRequires:	libx11-devel		>= 1.1.3
BuildRequires:	libxext-devel		>= 1.0.3
BuildRequires:	libxi-devel		>= 1.1.3
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)

%description
Runtime configuration and test of XInput devices

%prep
%setup -q

%build
%configure2_5x
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


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.3-2mdv2011.0
+ Revision: 671326
- mass rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 1.5.2-1mdv2011.0
+ Revision: 556464
- new release

* Mon Mar 15 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.5.1-1mdv2010.1
+ Revision: 519807
- New version: 1.5.1

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.5.0-1mdv2010.1
+ Revision: 464709
- New version: 1.5.0

* Thu May 07 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.4.2-1mdv2010.0
+ Revision: 372940
- New version 1.4.2

* Thu Apr 30 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.4.1-1mdv2010.0
+ Revision: 369174
- New version 1.4.1

* Fri Jan 16 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.4.0-1mdv2009.1
+ Revision: 330223
- New version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.3.0-4mdv2009.0
+ Revision: 226046
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.3.0-3mdv2008.1
+ Revision: 166552
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.3.0-2mdv2008.1
+ Revision: 154709
- Minor fix to quote pkconfig version test.
  Add BuildRequires of libxi-devel.
- Rebase from tag xinput-1.3.0
  Updated BuildRequires and resubmit package.
- Update to xinput version that is available in the xorg/app/xinput
  X Org git repository.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.2-10mdv2008.1
+ Revision: 130232
- kill re-definition of %%buildroot on Pixel's request


* Tue Nov 28 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.2-10mdv2007.0
+ Revision: 87935
- added buildrequires for gccmakedep
- Fixed package for modular
- Fixed group (System/X11) (#27324)
- Import xinput

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.2-9mdk
- Rebuild

* Sat Dec 25 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2-8mdk
- fix buildrequires
- drop useless prefix tag
- cosmetics

* Thu Jul 01 2004 Frederic Lepied <flepied@mandrakesoft.com> 1.2-7mdk
- added patch from Dana Dahlstrom to correct loop processing.


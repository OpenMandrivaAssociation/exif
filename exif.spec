Summary:	Command line tools to access EXIF extensions in JPEG files
Name:		exif
Version:	0.6.21
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphics
URL:		http://sourceforge.net/projects/libexif
Source:		http://downloads.sourceforge.net/project/libexif/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(popt)

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

This package contains a command line frontend for the EXIF library.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall
%find_lang %{name}

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS ChangeLog README
%{_bindir}/*
%{_mandir}/man*/*


%changelog
* Fri Jul 13 2012 Oden Eriksson <oeriksson@mandriva.com> 0.6.21-1
+ Revision: 809122
- 0.6.21

* Sat May 26 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.6.20-3
+ Revision: 800786
- rebuild dropped reqs for popt (which used to be virt prov for libpopt0)
- cleaned up spec

* Wed Mar 28 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.6.20-2
+ Revision: 788031
- Rebuild in current environment
- Clean up spec file

* Sun Oct 09 2011 Andrey Bondrov <abondrov@mandriva.org> 0.6.20-1
+ Revision: 703870
- New version 0.6.20

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.19-3
+ Revision: 664159
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.19-2mdv2011.0
+ Revision: 605110
- rebuild

* Fri Nov 20 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.19-1mdv2010.1
+ Revision: 467651
- Update to new version 0.6.19
- Rediff wformat patch

* Wed Aug 12 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.6.17-2mdv2010.0
+ Revision: 415374
- fix -Wformat=error warnings

* Wed Nov 19 2008 Frederik Himpe <fhimpe@mandriva.org> 0.6.17-1mdv2009.1
+ Revision: 304468
- New version 0.6.17
- Fix license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.6.15-3mdv2009.0
+ Revision: 220733
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.6.15-2mdv2008.1
+ Revision: 149706
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Jun 21 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.6.15-1mdv2008.0
+ Revision: 42326
- New upstream: 0.6.15


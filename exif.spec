Summary:	Command line tools to access EXIF extensions in JPEG files
Name:		exif
Version:	0.6.17
Release:	%mkrel 1
License:	GPLv2+ and LGPLv2+
Group:		Graphics
URL:		http://sourceforge.net/projects/libexif
Source:		http://belnet.dl.sourceforge.net/sourceforge/libexif/%{name}-%{version}.tar.bz2
Requires:	popt
BuildRequires:	libexif-devel popt-devel pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

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
rm -rf %{buildroot}

%makeinstall
%find_lang %{name}

%clean
rm -fr %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS ChangeLog README
%{_bindir}/*
%{_mandir}/man*/*


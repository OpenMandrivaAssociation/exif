%define oversion  0_6_22

Summary:	Command line tools to access EXIF extensions in JPEG files
Name:		exif
Version:	0.6.22
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphics
Url:		https://libexif.github.io
Source0:	https://github.com/libexif/exif/releases/download/%{name}-%{oversion}-release/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(popt)

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

This package contains a command line frontend for the EXIF library.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS ChangeLog README
%{_bindir}/*
%{_mandir}/man*/*


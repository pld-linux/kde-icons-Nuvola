#$Revision: 1.1 $, $Date: 2004-08-18 23:14:44 $

%define		_name	nuvola

Summary:	KDE icons - Nuvola
Summary(pl):	Motyw ikon do KDE - Nuvola
Name:		kde-icons-Nuvola
Version:	1.0beta
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.icon-king.com/files/%{_name}-%{version}.tgz
# Source0-md5:	cc7b2b190e2c8756ad41349b51154c8c
URL:		http://www.kde-look.org/content/show.php?content=5358
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
KDE Icons Theme - Nuvola.

%description -l pl
Motyw ikon dla KDE - Nuvola.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

tar xfz %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*

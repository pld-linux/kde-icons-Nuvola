#$Revision: 1.2 $, $Date: 2004-09-01 07:17:25 $

%define		_name	nuvola

Summary:	KDE icons - Nuvola
Summary(pl):	Motyw ikon do KDE - Nuvola
Name:		kde-icons-Nuvola
Version:	1.0rc1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.icon-king.com/files/%{_name}-%{version}.tar.gz
# Source0-md5:	acb6e73b5bc61bc7ca5df87e7712ffc3
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

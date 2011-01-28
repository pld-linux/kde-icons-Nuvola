
%define		_name	nuvola

Summary:	KDE icons - Nuvola
Summary(pl.UTF-8):	Motyw ikon do KDE - Nuvola
Name:		kde-icons-Nuvola
Version:	1.0
Release:	1
Epoch:		1
License:	GPL
Group:		Themes
Source0:	http://www.icon-king.com/files/%{_name}-%{version}.tar.gz
# Source0-md5:	bf3e477716fe0b39de81c210d1b5a8d1
URL:		http://www.icon-king.com/
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
KDE Icons Theme - Nuvola.

%description -l pl.UTF-8
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

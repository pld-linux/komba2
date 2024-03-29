Summary:	Komba - a Samba-Share-browser
Summary(pl.UTF-8):	Komba - przeglądarka zasobów Samby
Name:		komba2
Version:	0.7.3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://zeus.fh-brandenburg.de/~schwanz/files/%{name}_KDE3-%{version}beta.tar.gz
# Source0-md5:	a96dc107b35cd07620667e25cf8f7c59
URL:		http://zeus.fh-brandenburg.de/~schwanz/php/komba.php3
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	komba

%define		_htmldir	/usr/share/doc/kde/HTML

%description
Komba is a Samba-Share-browser. It can mount an unmount shares from
win-network and look to other workgroups.

%description -l pl.UTF-8
Komba to przeglądarka zasobów udostępnionych przez Sambę. Może
montować i odmontowywać zasoby sieciowe oraz przeglądać inne gruby
sieciowe.

%prep
%setup -q

%build
KDEDIR="%{_prefix}"; export KDEDIR
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_applnkdir}/Applications $RPM_BUILD_ROOT%{_applnkdir}/Network

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/komba2
%{_applnkdir}/Network/komba2.desktop
%{_datadir}/apps/komba2
%{_pixmapsdir}/*/*/apps/*

Summary:	Komba - a Samba-Share-browser
Summary(pl):	Komba - przegl±darka zasobów Samby
Name:		komba2
Version:	0.7.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://zeus.fh-brandenburg.de/~schwanz/files/%{name}-%{version}.tar.gz
URL:		http://zeus.fh-brandenburg.de/~schwanz/php/komba.php3
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	komba

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir	/usr/share/doc/kde/HTML

%description
Komba is a Samba-Share-browser. It can mount an unmount shares from
win-network and look to other workgroups.

%description -l pl
Komba to przegl±darka zasobów udostêpnionych przez Sambê. Mo¿e
montowaæ i odmontowywaæ zasoby sieciowe oraz przegl±daæ inne gruby
sieciowe.

%prep
%setup -q

%build
KDEDIR="%{_prefix}"; export KDEDIR
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure2_13

touch configure.in aclocal.m4 Makefile.in stamp-h.in configure \
	komba2/Makefile.in config.status

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

(cd $RPM_BUILD_ROOT%{_applnkdir}
mv -f Internet Network
)

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/komba2
%{_applnkdir}/Network/komba2.desktop
%{_datadir}/apps/komba2
%{_pixmapsdir}/*/*/apps/*

Summary:	Crafted - an editor for Freecraft maps
Summary(pl.UTF-8):	Crafted - edytor do map Freecrafta
Name:		crafted
Version:	0.1.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	ecbd30b4d23ef6d204b99ee1220babc3
Patch0:		%{name}-acfix.patch
#URL:		http://freecraft.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crafted - an editor for Freecraft maps.

%description -l pl.UTF-8
Crafted - edytor do map Freecrafta.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

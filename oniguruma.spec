Summary:	Oniguruma - a regular expressions library
Summary(pl.UTF-8):	Oniguruma - biblioteka wyrażeń regularnych
Name:		oniguruma
Version:	5.9.6
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://www.geocities.jp/kosako3/oniguruma/archive/onig-%{version}.tar.gz
# Source0-md5:	d08f10ea5c94919780e6b7bed1ef9830
URL:		http://www.geocities.jp/kosako3/oniguruma/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The characteristics of this library is that different character
encoding for every regular expression object can be specified.

%description -l pl.UTF-8
Biblioteka Oniguruma charakteryzuje się tym, że można podać inne
kodowanie znaków dla każdego obiektu wyrażenia regularnego.

%package devel
Summary:	Header files for Oniguruma library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Oniguruma
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for Oniguruma library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki Oniguruma.

%package static
Summary:	Static Oniguruma library
Summary(pl.UTF-8):	Statyczna biblioteka Oniguruma
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Oniguruma library.

%description static -l pl.UTF-8
Statyczna biblioteka Oniguruma.

%prep
%setup -q -n onig-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc HISTORY README
%doc %lang(ja) README.ja
%attr(755,root,root) %{_libdir}/libonig.so.*.*.*
%attr(755,root,root) %ghost  %{_libdir}/libonig.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/onig-config
%attr(755,root,root) %{_libdir}/libonig.so
%{_libdir}/libonig.la
%{_includedir}/oniggnu.h
%{_includedir}/onigposix.h
%{_includedir}/oniguruma.h
%{_pkgconfigdir}/oniguruma.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libonig.a

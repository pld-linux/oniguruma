Summary:	Oniguruma - a regular expressions library
Summary(pl.UTF-8):	Oniguruma - biblioteka wyrażeń regularnych
Name:		oniguruma
Version:	6.9.0
Release:	1
License:	BSD
Group:		Libraries
# Source0Download: https://github.com/kkos/oniguruma/releases
Source0:	https://github.com/kkos/oniguruma/releases/download/v%{version}/onig-%{version}.tar.gz
# Source0-md5:	10fd7eee9a54ab1c2c3b99846888d00a
URL:		https://github.com/kkos/oniguruma
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.14
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
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies (and .pc exists)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libonig.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING HISTORY README.md index.html
%doc %lang(ja) README_japanese index_ja.html
%attr(755,root,root) %{_libdir}/libonig.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libonig.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/onig-config
%attr(755,root,root) %{_libdir}/libonig.so
%{_includedir}/oniggnu.h
%{_includedir}/onigposix.h
%{_includedir}/oniguruma.h
%{_pkgconfigdir}/oniguruma.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libonig.a

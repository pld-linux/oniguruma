Summary:	Oniguruma - a regular expressions library
Summary(pl):	Oniguruma - biblioteka wyra¿eñ regularnych
Name:		oniguruma
Version:	4.5.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.geocities.jp/kosako3/oniguruma/archive/onig-%{version}.tar.gz
# Source0-md5:	ba3dd9caeca80afff318a1897c46327f
URL:		http://www.geocities.jp/kosako3/oniguruma/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The characteristics of this library is that different character
encoding for every regular expression object can be specified.

%description -l pl
Biblioteka Oniguruma charakteryzuje siê tym, ¿e mo¿na podaæ inne
kodowanie znaków dla ka¿dego obiektu wyra¿enia regularnego.

%package devel
Summary:	Header files for Oniguruma library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for Oniguruma library.

%package static
Summary:	Static Oniguruma library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Oniguruma library.

%prep
%setup -q -n onig-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

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
%attr(755,root,root) %{_prefix}/lib/libonig.so.1.0.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/onig-config
%{_libdir}/libonig.la
%{_includedir}/oniggnu.h
%{_includedir}/onigposix.h
%{_includedir}/oniguruma.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libonig.a

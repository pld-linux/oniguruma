# TODO
# - shared library
#
# Conditional build:
%bcond_without	tests		# build without tests
#
Summary:	Oniguruma - a regular expressions library
Summary(pl):	Oniguruma - biblioteka wyra¿eñ regularnych
Name:		oniguruma
Version:	3.9.1
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://www.geocities.jp/kosako3/oniguruma/archive/onigd20051129.tar.gz
# Source0-md5:	5ff638b59a75ad343b9abf1db9d57c16
Patch0:		%{name}-DESTDIR.patch
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

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}
%{?with_tests:%{__make} ctest}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING HISTORY README
%doc %lang(ja) README.ja
%attr(755,root,root) %{_bindir}/onig-config
%{_includedir}/oniggnu.h
%{_includedir}/onigposix.h
%{_includedir}/oniguruma.h
%{_libdir}/libonig.a

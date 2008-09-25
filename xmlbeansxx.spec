%bcond_with	log4cxx
%bcond_with	gmpxx
Summary:	Library used by code generated with xmlbeansxx-generator
Summary(pl.UTF-8):	Biblioteka wykorzystywana przez kod wygenerowany przez xmlbeansxx-generator
Name:		xmlbeansxx
Version:	0.9.8
Release:	0.1
License:	Apache
Group:		Libraries
Source0:	http://dl.sourceforge.net/xmlbeansxx/%{name}-%{version}.tar.gz
# Source0-md5:	969ba90bd8113c712f1ce525883b1541
URL:		http://xmlbeansxx.touk.pl/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	cppunit-devel
%{?with_gmpxx:BuildRequires:	gmp-c++-devel}
BuildRequires:	libtool >= 2:1.4d
%{?with_log4cxx:BuildRequires:	log4cxx-devel >= 0.10.0}
BuildRequires:	maven
BuildRequires:	xerces-c-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmlbeansxx is a technology for accessing XML by binding it to C++
classes. It is inspired by the Apache XML Project (a.k.a. XMLBeans).
This package contains library used by code generated with
xmlbeansxx-generator. You may also need a xmlbeansxx-generator
package.

%description -l pl.UTF-8
xmlbeansxx jest technologią dostępu do danych zawartych w plikach
XML poprzez wiązanie danych XML z klasami C++. Biblioteka ta jest
wzorowana na bibliotece Apache XMLBeans. Ten pakiet zawiera biblioteki
wykorzystywane przez kod wygenerowany przy użyciu narzędzi z pakietu
xmlbeansxx-generator.

%package devel
Summary:	Header files for xmlbeansxx library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki xmlbeansxx
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Suggests:	%{name}-generator = %{version}-%{release}

%description devel
Header files for xmlbeansxx library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki xmlbeansxx

%package static
Summary:	Static xmlbeansxx library
Summary(pl.UTF-8):	Statyczna biblioteka xmlbeansxx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Suggests:	%{name}-generator = %{version}-%{release}

%description static
Static xmlbeansxx library.

%description static -l pl.UTF-8
Statyczna biblioteka xmlbeansxx.

%package generator
Summary:	xmlbeansxx C++ class generator
Summary(pl.UTF-8):	Generator klas C++
Group:		Development/Tools
BuildRequires:	jar
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	maven
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	bash
Requires:	jpackage-utils
Requires:	jre >= 1.4

%description generator
This package contains a java utility that generates C++ classes for
parsing xml files that matches given xsd schema

%description generator -l pl.UTF-8
Ten pakiet zaweira narzędzie napisane w języku Java służące do
generowania klas C++ obsługujące pliki XML odpowiadające danemu
schematowi xsd.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
  %{!?with_log4cxx:--disable-log4cxx} \
  %{!?with_gmpxx:--disable-gmpxx}
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
%attr(755,root,root) %{_libdir}/libxmlbeansxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlbeansxx.so.5

%files static
%defattr(644,root,root,755)
%{_libdir}/libxmlbeansxx.a

%files devel
%defattr(644,root,root,755)
%{_libdir}/libxmlbeansxx.la
%attr(755,root,root) %{_libdir}/libxmlbeansxx.so
%{_includedir}/%{name}

%files generator
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%attr(755,root,root) %{_bindir}/scompxx
%attr(755,root,root) %{_bindir}/xmlbeansxx-gen
%attr(755,root,root) %{_bindir}/xmlbeansxx-geninclude
%attr(755,root,root) %{_bindir}/xmlbeansxx-split

%{_datadir}/%{name}/xmlbeansxx-gen.jar

%attr(755,root,root) %{_datadir}/%{name}/bin/scompxx
%attr(755,root,root) %{_datadir}/%{name}/bin/xmlbeansxx-gen
%attr(755,root,root) %{_datadir}/%{name}/bin/xmlbeansxx-geninclude
%attr(755,root,root) %{_datadir}/%{name}/bin/xmlbeansxx-split
%attr(755,root,root) %{_datadir}/%{name}/bin/xmlvalidator
%{_datadir}/%{name}/bin/acx_pthread.m4
%{_datadir}/%{name}/lib

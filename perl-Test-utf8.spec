#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Test
%define		pnam	utf8
Summary:	Test::utf8 - handy UTF-8 tests
Summary(pl.UTF-8):	Test::utf8 - podręczne testy UTF-8
Name:		perl-Test-utf8
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	03e219b5a7d0645b313f557238c0f8b3
URL:		https://metacpan.org/dist/Test-utf8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Builder-Tester >= 0.09
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a collection of tests useful for dealing with UTF-8
strings in Perl.

This module has two types of tests: The validity tests check if a
string is valid and not corrupt, whereas the characteristics tests
will check that string has a given set of characteristics.

%description -l pl.UTF-8
Ten moduł to zbiór testów przydatnych przy obsłudze łańcuchów
znaków UTF-8 w Perlu.

Moduł ma dwa rodzaje testów: testy poprawności, sprawdzające, czy
łańcuch jest poprawny oraz testy charakterystyki, sprawdzające, czy
łancuch ma dany zbiór cech.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_vendorlib}/Test/utf8.pm
%{_mandir}/man3/Test::utf8.3pm*

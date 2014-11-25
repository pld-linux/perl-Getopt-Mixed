%define		pdir	Getopt
%define		pnam	Mixed
%include	/usr/lib/rpm/macros.perl
Summary:	Getopt::Mixed - getopt processing with both long and short options
Summary(pl.UTF-8):	Getopt::Mixed - obsługa długich i krótkich opcji
Name:		perl-Getopt-Mixed
Version:	1.10
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9d384322a4368b326efdf899bce5838a
URL:		http://search.cpan.org/dist/Getopt-Mixed/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	perl(Getopt::Mixed) = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Getopt::Mixed Perl module is intended to be the
"Getopt-to-end-all-Getop's". It combines flexibility and simplicity.
It supports both short options (introduced by "-") and long options
(introduced by "--"). Short options which do not take an argument can
be grouped together. Short options which do take an argument must be
the last option in their group, because everything following the
option will be considered to be its argument.

%description -l pl.UTF-8
Moduł Perla Getopt::Mixed został pomyślany jako zastępujący wszystkie
podprogramy do pobierania opcji. Łączy w sobie elastyczność i
prostotę. Obsługuje zarówno opcje krótkie (poprzedzone "-"), jak i
długie (poprzedzone "--"). Krótkie opcje bezargumentowe muszą być
ostatnimi w swojej grupie, gdyż wszystko, co następuje po takiej opcji
byłoby traktowane jako jej argument.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Getopt/Mixed.pm
%{_mandir}/man3/*

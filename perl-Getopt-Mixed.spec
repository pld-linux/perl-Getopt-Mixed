%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	Mixed
Summary:	Getopt::Mixed - getopt processing with both long and short options
Summary(pl):	Getopt::Mixed - obs³uga d³ugich i krótkich opcji
Name:		perl-Getopt-Mixed
Version:	1.008
Release:	11
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7d492669944f93809b7963f2c88865e7
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.005_03-14
Provides:	perl(Getopt::Mixed) = %version
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Getopt::Mixed Perl module is intended to be the
"Getopt-to-end-all-Getop's".  It combines flexibility and simplicity. 
It supports both short options (introduced by "-") and long options
(introduced by "--"). Short options which do not take an argument can
be grouped together. Short options which do take an argument must be
the last option in their group, because everything following the
option will be considered to be its argument.

%description -l pl
Modu³ Perla Getopt::Mixed zosta³ pomy¶lany jako zastêpuj±cy wszystkie
podprogramy do pobierania opcji. £±czy w sobie elastyczno¶æ i
prostotê. Obs³uguje zarówno opcje krótkie (poprzedzone "-"), jak i
d³ugie (poprzedzone "--"). Krótkie opcje bezargumentowe musz± byæ
ostatnimi w swojej grupie, gdy¿ wszystko, co nastêpuje po takiej opcji
by³oby traktowane jako jej argument.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Getopt/Mixed.pm
%{_mandir}/man3/*

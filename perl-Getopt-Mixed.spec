%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	Mixed
Summary:	Getopt::Mixed perl module
Summary(pl):	Modu³ perla Getopt::Mixed
Name:		perl-Getopt-Mixed
Version:	1.008
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7d492669944f93809b7963f2c88865e7
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.005_03-14
Provides:	perl(Getopt::Mixed) = %version
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt::Mixed - getopt processing with both long and short options.

%description -l pl
Modu³ perla Getopt::Mixed.

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

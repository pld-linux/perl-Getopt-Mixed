%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	Mixed
Summary:	Getopt::Mixed perl module
Summary(pl):	Modu³ perla Getopt::Mixed
Name:		perl-Getopt-Mixed
Version:	1.008
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.005_03-14
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
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Getopt/Mixed.pm
%{_mandir}/man3/*

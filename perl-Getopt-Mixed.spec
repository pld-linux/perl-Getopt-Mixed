%include	/usr/lib/rpm/macros.perl
Summary:	Getopt-Mixed perl module
Summary(pl):	Modu³ perla Getopt-Mixed
Name:		perl-Getopt-Mixed
Version:	1.008
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Getopt/Getopt-Mixed-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt-Mixed - getopt processing with both long and short options.

%description -l pl
Modu³ perla Getopt-Mixed.

%prep
%setup -q -n Getopt-Mixed-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Getopt/Mixed.pm
%{_mandir}/man3/*

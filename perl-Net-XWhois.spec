%include	/usr/lib/rpm/macros.perl
Summary:	Net-XWhois perl module
Summary(pl):	Modu³ perla Net-XWhois
Name:		perl-Net-XWhois
Version:	0.64
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-XWhois-%{version}.tar.gz
Patch0:		perl-Net-XWhois-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-XWhois - Whois Client Interface for Perl.

%description -l pl
Net-XWhois - klient whois dla perla.

%prep
%setup -q -n Net-XWhois-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}


gzip -9nf Changes TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,TODO}.gz

%{perl_sitelib}/Net/XWhois.pm
%{perl_sitearch}/auto/Net/XWhois

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}

%define	pdir	Net
%define	pnam	XWhois
%include	/usr/lib/rpm/macros.perl
Summary:	Net-XWhois perl module
Summary(pl):	Modu³ perla Net-XWhois
Name:		perl-Net-XWhois
Version:	0.82
Release:	3

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Net/XWhois.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

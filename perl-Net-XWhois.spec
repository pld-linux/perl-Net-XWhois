#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	XWhois
Summary:	Net::XWhois - whois Client Interface for Perl5
Summary(pl):	Net::XWhois - klient whois dla Perla 5
Name:		perl-Net-XWhois
Version:	0.90
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::XWhois class provides a generic client framework for doing
whois queries and parsing server response.

%description -l pl
Klasa Net::XWhois udostêpnia podstawowy szkielet klienta wykonuj±cego
zapytania whois i przetwarzaj±cego odpowiedzi serwera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/Net/XWhois.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

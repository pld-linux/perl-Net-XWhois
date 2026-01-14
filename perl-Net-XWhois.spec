#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Net
%define		pnam	XWhois
Summary:	Net::XWhois - whois client Interface for Perl5
Summary(pl.UTF-8):	Net::XWhois - klient whois dla Perla 5
Name:		perl-Net-XWhois
Version:	0.90
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1c0394d6a4b5bd05d8686b0a0dc18999
URL:		http://search.cpan.org/dist/Net-XWhois/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::XWhois class provides a generic client framework for doing
whois queries and parsing server response.

%description -l pl.UTF-8
Klasa Net::XWhois udostępnia podstawowy szkielet klienta wykonującego
zapytania whois i przetwarzającego odpowiedzi serwera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/Net/XWhois.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	XWhois
Summary:	Net::XWhois Perl module
Summary(cs):	Modul Net::XWhois pro Perl
Summary(da):	Perlmodul Net::XWhois
Summary(de):	Net::XWhois Perl Modul
Summary(es):	Módulo de Perl Net::XWhois
Summary(fr):	Module Perl Net::XWhois
Summary(it):	Modulo di Perl Net::XWhois
Summary(ja):	Net::XWhois Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Net::XWhois ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Net::XWhois
Summary(pl):	Modu³ perla Net::XWhois
Summary(pt_BR):	Módulo Perl Net::XWhois
Summary(pt):	Módulo de Perl Net::XWhois
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Net::XWhois
Summary(sv):	Net::XWhois Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Net::XWhois
Summary(zh_CN):	Net::XWhois Perl Ä£¿é
Name:		perl-Net-XWhois
Version:	0.90
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::XWhois - Whois Client Interface for Perl.

%description -l pl
Net::XWhois - klient whois dla perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
perl Makefile.PL
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
%{perl_sitelib}/Net/XWhois.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

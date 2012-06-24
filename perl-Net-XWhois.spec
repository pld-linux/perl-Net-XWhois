%include	/usr/lib/rpm/macros.perl
Summary:	Net-XWhois perl module
Summary(pl):	Modu� perla Net-XWhois
Name:		perl-Net-XWhois
Version:	0.64
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-XWhois-%{version}.tar.gz
Patch0:		perl-Net-XWhois-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
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

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/XWhois
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,TODO}.gz

%{perl_sitelib}/Net/XWhois.pm
%{perl_sitearch}/auto/Net/XWhois

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}

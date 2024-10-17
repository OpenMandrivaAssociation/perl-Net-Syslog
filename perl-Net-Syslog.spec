%define  upstream_name    Net-Syslog
%define  upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl extension for sending syslog messages directly to a remote syslogd
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Net::Syslog implements the intra-host syslog forwarding protocol.
It is not intended to replace the Sys::Syslog or
Unix::Syslog modules, but instead to provide a method of using syslog when a
local syslogd is unavailable or when you don't want to write syslog messages
to the local syslog.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Net/Syslog.pm
%{_mandir}/man*/*


%changelog
* Mon Oct 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 589353
- new version

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 404247
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.03-7mdv2009.0
+ Revision: 258134
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.03-6mdv2009.0
+ Revision: 246183
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 0.03-4mdv2008.1
+ Revision: 166681
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.03-4mdv2008.0
+ Revision: 25451
- rebuild

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.03-3mdv2008.0
+ Revision: 25197
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
	- URL

* Fri Feb 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdk
- initial Mandriva package


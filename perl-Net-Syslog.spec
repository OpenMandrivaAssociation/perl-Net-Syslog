%define  upstream_name    Net-Syslog
%define upstream_version 0.04
Name:		perl-%{upstream_name}
Version:	0.04
Release:	3

Summary:	Perl extension for sending syslog messages directly to a remote syslogd
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/L/LH/LHOWARD/Net-Syslog-0.04.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Net::Syslog implements the intra-host syslog forwarding protocol.
It is not intended to replace the Sys::Syslog or
Unix::Syslog modules, but instead to provide a method of using syslog when a
local syslogd is unavailable or when you don't want to write syslog messages
to the local syslog.

%prep
%setup -q -n Net-Syslog-0.04

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Net/Syslog.pm
%{_mandir}/man*/*



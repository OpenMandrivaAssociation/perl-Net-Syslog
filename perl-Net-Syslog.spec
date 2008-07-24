%define  module Net-Syslog

Summary:	Perl extension for sending syslog messages directly to a remote syslogd
Name:		perl-%{module}
Version:	0.03
Release:	%mkrel 6
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Net::Syslog - Perl extension for sending syslog messages directly to a remote
syslogd.

Net::Syslog implements the intra-host syslog forwarding protocol.
It is not intended to replace the Sys::Syslog or
Unix::Syslog modules, but instead to provide a method of using syslog when a
local syslogd is unavailable or when you don't want to write syslog messages
to the local syslog.


%prep

%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

%clean 
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Net/Syslog.pm
%{perl_vendorlib}/*/Net/Syslog/autosplit.ix
%{_mandir}/man*/*


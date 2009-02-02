#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	OWNet
Summary:	OWNet Light weight access to owserver
#Summary(pl.UTF-8):	
Name:		perl-OWNet
Version:	1.8
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AL/ALFILLE/OWNet-1.8.tar.gz
# Source0-md5:	c6ef2a8bcde363c820bbe00a9b5e2bab
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/OWNet/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OWFS is a suite of programs that allows easy access to Dallas Semiconductor's 1-wire bus and devices. OWFS provides a consistent naming scheme, safe multplexing of 1-wire traffice, multiple methods of access and display, and network access. The basic OWFS metaphor is a file-system, with the bus beinng the root directory, each device a subdirectory, and the the device properties (e.g. voltage, temperature, memory) a file.

1-wire is a protocol allowing simple connection of inexpensive devices. Each device has a unique ID number (used in it's OWFS address) and is individually addressable. The bus itself is extremely simple -- a data line and a ground. The data line also provides power. 1-wire devices come in a variety of packages -- chips, commercial boxes, and iButtons (stainless steel cans). 1-wire devices have a variety of capabilities, from simple ID to complex voltage, temperature, current measurements, memory, and switch control.

Connection to the 1-wire bus is either done by bit-banging a digital pin on the processor, or by using a bus master -- USB, serial, i2c, parallel. The heavy-weight OWFS programs: owserver owfs owhttpd owftpd and the heavy-weight perl module OW all link in the full OWFS library and can connect directly to the bus master(s) and/or to owserver.  

OWNet is a light-weight module. It connects only to an owserver, does not link in the OWFS library, and should be more portable..



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/*.pm
#%%{perl_vendorlib}/OWNet/
%{_mandir}/man3/*

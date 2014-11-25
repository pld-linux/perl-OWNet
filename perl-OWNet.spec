#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	OWNet
%include	/usr/lib/rpm/macros.perl
Summary:	OWNet Light weight access to owserver
Name:		perl-OWNet
Version:	1.8
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AL/ALFILLE/OWNet-%{version}.tar.gz
# Source0-md5:	c6ef2a8bcde363c820bbe00a9b5e2bab
URL:		http://search.cpan.org/dist/OWNet/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OWNet is a light-weight module. It connects only to an owserver, does
not link in the OWFS library, and should be more portable..

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

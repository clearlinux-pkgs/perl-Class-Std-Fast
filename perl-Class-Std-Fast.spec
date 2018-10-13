#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Std-Fast
Version  : 0.0.8
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/A/AC/ACID/Class-Std-Fast-v0.0.8.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AC/ACID/Class-Std-Fast-v0.0.8.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libc/libclass-std-fast-perl/libclass-std-fast-perl_0.0.8-2.debian.tar.xz
Summary  : faster but less secure than Class::Std
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Class-Std-Fast-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Std)

%description
Class::Std::Fast version 0.0.8
This module provides a faster but less secure version of Class::Std

%package dev
Summary: dev components for the perl-Class-Std-Fast package.
Group: Development
Provides: perl-Class-Std-Fast-devel = %{version}-%{release}

%description dev
dev components for the perl-Class-Std-Fast package.


%package license
Summary: license components for the perl-Class-Std-Fast package.
Group: Default

%description license
license components for the perl-Class-Std-Fast package.


%prep
%setup -q -n Class-Std-Fast-v0.0.8
cd ..
%setup -q -T -D -n Class-Std-Fast-v0.0.8 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Class-Std-Fast-v0.0.8/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Class-Std-Fast
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Class-Std-Fast/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/Class/Std/Fast.pm
/usr/lib/perl5/vendor_perl/5.26.1/Class/Std/Fast/Storable.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Std::Fast.3
/usr/share/man/man3/Class::Std::Fast::Storable.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Class-Std-Fast/deblicense_copyright

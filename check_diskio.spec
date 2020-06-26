################################################################################
# File version information:
# $Id$
# $Revision$
# $HeadURL$
# $Date$
################################################################################

%define version          3.2.8
%define release          2
%define sourcename       check_diskio
%define packagename      nagios-plugins-check-diskio
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package %{nil}

Summary:   Nagios plugin to monitor the amount of disk I/O
Name:      %{packagename}
Version:   %{version}
Obsoletes: check_diskio
Release:   %{release}%{?dist}
License:   GPLv3+
Packager:  Matteo Corti <matteo@corti.li>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{packagename}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:       https://trac.id.ethz.ch/projects/nagios_plugins/wiki/check_diskio
Source:    https://trac.id.ethz.ch/projects/nagios_plugins/downloads/%{sourcename}-%{version}.tar.gz

# Fedora build requirement (not needed for EPEL{4,5})
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(Number::Format)
BuildRequires: perl(Readonly)
BuildRequires: perl(File::Spec)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(English)
BuildRequires: perl(Carp)
BuildRequires: perl(Array::Unique)

Requires:  nagios-plugins
Requires:  perl(Array::Unique)
Requires:  perl(List::MoreUtils)

%description
Nagios plugin to monitor the amount of disk I/O

%prep
%setup -q -n %{sourcename}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor \
    INSTALLSCRIPT=%{nagiospluginsdir} \
    INSTALLVENDORSCRIPT=%{nagiospluginsdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name "*.pod" -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc AUTHORS Changes NEWS README INSTALL TODO COPYING COPYRIGHT
%{nagiospluginsdir}/%{sourcename}
%{_mandir}/man1/%{sourcename}.1*

%changelog
* Fri Jun 26 2020 Matteo Corti <matteo.corti@id.ethz.ch> - 3.2.8-2
- Added dependency to List::MoreUtils

* Fri Jun 26 2020 Matteo Corti <matteo.corti@id.ethz.ch> - 3.2.8-1
- Added dependency to Array::Unique

* Tue Jun  2 2015 Matteo Corti <matteo.corti@id.ethz.ch> - 3.2.8-0
- Updated to 3.2.8

* Sat Nov 29 2014 Matteo Corti <matteo@corti.li> - 3.2.7-0
- Updated to 3.2.7 (fixes CVE-2014-8994)

* Thu Jan 30 2014 Matteo Corti <matteo.corti@id.ethz.ch> - 3.2.6-0
- Updated to 3.2.6 (bug fix)

* Wed Nov  9 2011 Matteo Corti <matteo.corti@id.ethz.ch> - 3.2.4-0
- 3.X kernel support

* Fri Oct 22 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 3.2.3-0
- Fixed a bug in the statistics parsing

* Tue Jul  6 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 3.2.2-0
- Updated to 3.2.2 (does not ignore devices specified with -d /dev)

* Wed Jun 30 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 3.2.1-0
- Updated to 3.2.1 (UNKNOWN if not able to check LVM)

* Tue May 25 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 3.2.0-0
- updated to 3.2.0 (partion numbers are stripped only if the
  --strip-partition-number option is specified)

* Sun Apr 18 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 3.1.1-0
- Updated to 3.1.1 (--debug option and fix for different
  /proc/diskstats formats)

* Thu Feb 18 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 3.1.0-0
- Updated to 3.1.0 and fixed build on 64 systems

* Tue Jun  9 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.3-0
- fix for HP Smart Array Cards

* Sun May 17 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.2-0
- update to 3.0.2 (UOM fix)

* Fri May 15 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.1-0
- embedded perl -> package variables

* Tue Jan 20 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.0-0
- multiple devices and LVM

* Sun Oct 26 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.2.1-0
- added dependency on Class::Accessor::Fast

* Thu Apr 10 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.2.0-0
- --device can be specified as a mount point

* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.2-0
- fixed missing usage message

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.1-0
- ePN compatibility

* Thu Nov 22 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.0-0
- upgraded to 2.1.0

* Wed Oct 31 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0.1-0
- upgraded to 2.0.1 (bug fix)

* Tue Oct 30 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0.0-0
- upgraded to 2.0.0

* Mon Sep 24 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.0-0
- First RPM package

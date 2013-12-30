%def_disable static

Name: libsample
Version: 0.1
Release: alt1

Summary: Sample library specfile
License: LGPLv2+
Group: System/Libraries
Url: http://www.altlinux.org/SampleSpecs/library

Source: ftp://sample.com/download/%name-%version.tar.bz2

%description
This specfile is provided as sample specfile for packages with libraries.
It contains most of usual tags and constructions used in such specfiles.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%prep
%setup

%build
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README NEWS
%_libdir/*.so.*

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libdir/lib%name.a
%endif

%changelog
* Sun Sep 32 3001 Sample Packager <sample@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus




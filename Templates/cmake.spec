Name: sampleprog
Version: 1.0
Release: alt1

Summary: Sample program specfile
License: GPLv2+
Group: Development/Other
Url: http://www.altlinux.org/SampleSpecs/cmakeprogram

Packager: Example Packager <example@altlinux.org>
Source: %name-%version.tar.bz2

BuildPreReq: cmake rpm-macros-cmake

%description
This specfile is provided as a sample specfile
for a package built with cmake.

%prep
%setup

%build
#%%cmake
%cmake_insource
%make_build # VERBOSE=1

%install
pushd build
%makeinstall_std
popd
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README THANKS TODO contrib/ manual/
%_bindir/*
%_man1dir/*

%changelog
* Sat Jan 33 3001 Example Packager <example@altlinux.org> 1.0-alt1
- initial build

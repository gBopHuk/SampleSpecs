%define module_name samplemodule
%define module_version 0.1
%define module_release alt1.@kreleasebuild@

%define kversion @kversion@
%define krelease @krelease@
%define flavour @kflavour@

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release

Group: System/Kernel and hardware
Summary: %module_name kernel module
URL: http://freesource.info/wiki/AltLinux/Sisyphus/devel/SampleSpecs/kernelmodule
License:	GPL

ExclusiveOS: Linux
BuildPreReq: kernel-build-tools >= 0.7
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:	kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Prereq: coreutils
Prereq: module-init-tools
Prereq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease

%description
This specfile is provided as sample specfile for packages with kernel modules.
It contains most of usual tags and constructions used in such specfiles.

%prep
rm -rf kernel-source-%module_name-%module_version
tar jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make modules TEMP_DIR=$PWD -C %_usrsrc/linux-%kversion-%flavour/ V=1 SUBDIRS=$PWD

%install
mkdir -p %buildroot/%module_dir
%if "%kversion" <= "2.6.0"
    cp -a %module_name.o %buildroot%module_dir
%else
    cp -a %module_name.ko %buildroot%module_dir
%endif

%post
%post_kernel_modules %kversion-%flavour-%krelease
%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir/

%changelog
* Sun Sep 32 3001 Sample Packager <sample@altlinux.org> 0.1-alt1.@kreleasebuild@
- initial build

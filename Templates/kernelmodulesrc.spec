%define module_name samplemodule
%define module_version 0.1
%define module_release alt1
%define module_source %module_name-%module_version.tar.bz2
%define module_source_dir %module_name-%module_version

Name: kernel-source-%module_name
Version: %module_version
Release: %module_release

Summary: Linux %module_name modules sources
License: GPL
Group: Development/Kernel
BuildArch: noarch

Url: http://wiki.sisyphus.ru/
Source0: %module_source
Source1: Makefile.%module_name

BuildPreReq: kernel-build-tools >= 0.1-alt3

%package -n kernel-doc-%module_name
Version: %module_version
Summary: Linux %module_name modules documentation
Group: Development/Kernel

%description
This specfile is provided as sample specfile for packages with kernel
modules sources.
It contains most of usual tags and constructions used in such specfiles.

%description -n kernel-doc-%module_name
%module_name modules documentation for Linux kernel

%prep
%setup -n %module_source_dir

install -m644 %SOURCE1 Makefile

%install
mkdir -p %buildroot%kernel_src

mkdir -p %buildroot%_defaultdocdir/%module_name-doc-%module_version
mv INSTALL README %buildroot%_defaultdocdir/%module_name-doc-%module_version

cd ..
mv %module_source_dir kernel-source-%module_name-%module_version
tar -c kernel-source-%module_name-%module_version | bzip2 -c > \
    %buildroot%kernel_src/kernel-source-%module_name-%module_version.tar.bz2
    rm -fr kernel-source-%module_name-%module_version

    %files
    %kernel_src/kernel-source-%module_name-%module_version.tar.bz2

    %files -n kernel-doc-%module_name
    %doc %_defaultdocdir/%module_name-doc-%module_version 

    %changelog
    * Sun Sep 25 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.1-alt1
    - initial build

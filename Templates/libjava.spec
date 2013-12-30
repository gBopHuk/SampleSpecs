Name: sample-javalib
Version: 1.1.0
Release: alt1

Summary: Sample java library
License: Apache Software License
Group: Development/Java
Url: http://wiki.sisyphus.ru

Source: %name-%version-src.tar.gz

# Common dependencies
BuildPreReq: /proc rpm-build-java jpackage-utils
BuildRequires: java-devel-default 

# if ant is used for build
BuildRequires: ant junit

# Example dependency
BuildRequires: example-javalib
Requires: example-javalib

BuildArch: noarch

%description
This specfile is an example of java library/program packaging.

%package javadoc
Summary: Javadoc for %name
Group: Development/Documentation
Requires: java-common

%description javadoc
Javadoc for %name.

%package manual
Summary: Manual for %name
Group: Documentation

%description manual
Documentation for %name

%package demo
Summary: Demo for %name
Group: Development/Java
Requires: %name=%verison-%release

%description demo
Demonstrations and samples for %name.

%prep
%setup -n %name-%version
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.zip" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;


%build
export CLASSPATH=$(build-classpath junit example-javalib)
%ant \
	-Dbuild.sysclasspath=only \
		dist

%install
# jars
install -d -m 755 %buildroot%_javadir
install -m 644 dist/%name-%version.jar %buildroot%_javadir/
ln -s %name-%version.jar %buildroot%_javadir/%name.jar

# javadoc
install -d -m 755 %buildroot%_javadocdir/%name
cp -pr dist/docs/api/* %buildroot%_javadocdir/%name
rm -rf dist/docs/api

# demo
install -d -m 755 %buildroot%_datadir/%name
cp -pr dist/examples %buildroot%_datadir/%name

%files
%doc README.txt RELEASE-NOTES.txt LICENSE.txt
%_javadir/*

%files javadoc
%doc %_javadocdir/%name

%files manual
%doc dist/docs/*

%files demo
%_datadir/%name

%changelog
* Tue Jul 22 2008 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- jpackage compatible changes: removed obsolete macroses

* Sun Sep 25 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt1
- Initial build

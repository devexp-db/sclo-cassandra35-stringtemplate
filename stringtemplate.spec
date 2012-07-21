Summary: A Java template engine
Name: stringtemplate
Version: 3.2.1
Release: 4%{?dist}
URL: http://www.stringtemplate.org/
Source0: http://www.stringtemplate.org/download/stringtemplate-%{version}.tar.gz
# Build jUnit tests + make the antlr2 generated code before preparing sources
Patch0: stringtemplate-3.1-build-junit.patch
License: BSD
Group: Development/Libraries
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: ant-antlr, ant-junit
BuildRequires: antlr
# Standard deps
BuildRequires: java-devel >= 1:1.6.0
BuildRequires: jpackage-utils
Requires: java >= 1:1.6.0
Requires: jpackage-utils

%description
StringTemplate is a java template engine (with ports for 
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation
Requires:       java-javadoc

%description    javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0

%build
rm -rf lib target
ant jar
ant javadocs -Dpackages= -Djavadocs.additionalparam=

%install
rm -rf $RPM_BUILD_ROOT
install -D build/stringtemplate.jar $RPM_BUILD_ROOT%{_datadir}/java/stringtemplate.jar
(cd $RPM_BUILD_ROOT%{_datadir}/java/ && ln -s stringtemplate.jar stringtemplate-%{version}.jar)
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pR docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -Dpm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap org.antlr %{name} %{version} JPP %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_maven_depmap

%postun
%update_maven_depmap

%check
ant test

%files
%defattr(-,root,root)
%doc LICENSE.txt README.txt
%{_datadir}/java/*.jar
%{_mavenpomdir}/JPP-%{name}.pom
%config(noreplace) %{_mavendepmapfragdir}/%{name}

%files javadoc
%defattr(-,root,root)
%{_javadocdir}/%{name}

%changelog
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 29 2010 Miloš Jakubíček <xjakub@fi.muni.cz> - 3.2.1-1
- Update to 3.2.1
- Supply maven POM files
- Drop stringtemplate-3.1-disable-broken-test.patch (merged upstream)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Apr 05 2008 Colin Walters <walters@redhat.com> - 3.1-1
- First version

%{?scl:%scl_package stringtemplate}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}stringtemplate
Version:	3.2.1
Release:	13%{?dist}
Summary:	A Java template engine
License:	BSD
URL:		http://www.stringtemplate.org/
Source0:	http://www.stringtemplate.org/download/%{pkg_name}-%{version}.tar.gz
# Build jUnit tests + make the antlr2 generated code before preparing sources
Patch0:		%{pkg_name}-3.1-build-junit.patch

BuildRequires:	%{?scl_prefix_java_common}ant-antlr
BuildRequires:	%{?scl_prefix_java_common}ant-junit
BuildRequires:	%{?scl_prefix_java_common}antlr-tool
BuildRequires:	%{?scl_prefix_java_common}javapackages-local

Requires:	%{?scl_prefix_java_common}antlr-tool
%{?scl:Requires: %scl_runtime}

BuildArch:	noarch

%description
StringTemplate is a java template engine (with ports for 
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package javadoc
Summary:	API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%patch0

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_file org.antlr:stringtemplate %{pkg_name}
%{?scl:EOF}

%build
rm -rf lib target
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
ant jar
ant javadocs -Dpackages= -Djavadocs.additionalparam=

%mvn_artifact pom.xml build/%{pkg_name}.jar
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install -J docs/api
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt README.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Dec 08 2016 Tomas Repik <trepik@redhat.com> - 3.2.1-13
- scl conversion, add_maven_depmap migration

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 05 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.2.1-10
- Fix for F21 XMvn changes (#1107380)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 3.2.1-8
- Use Requires: java-headless rebuild (#1067528)

* Wed Aug 14 2013 Mat Booth <fedora@matbooth.co.uk> - 3.2.1-7
- Fix FTBFS #993386

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 1 2013 Conrad Meyer <konrad@tylerc.org> - 3.2.1-5
- Add missing dep on antlr-tool (#904979)

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

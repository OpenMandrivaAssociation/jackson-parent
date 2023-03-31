%{?_javapackages_macros:%_javapackages_macros}
Name:          jackson-parent
Version:       2.4.1
Release:       1.4
Summary:       Parent pom for all Jackson components
Group:		Development/Java
License:       ASL 2.0
URL:           https://github.com/FasterXML/jackson-parent
Source0:       https://github.com/FasterXML/jackson-parent/archive/%{name}-%{version}.tar.gz
# jackson-parent package don't include the license file
# reported @ https://github.com/FasterXML/jackson-parent/issues/1
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires: mvn(com.fasterxml:oss-parent:pom:)
BuildRequires: mvn(junit:junit)
BuildRequires: maven-local
BuildRequires: replacer
BuildArch:     noarch

%description
Project for parent pom for all Jackson components.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt README.md

%changelog
* Wed Jul 02 2014 gil cattaneo <puntogil@libero.it> 2.4.1-1
- initial rpm

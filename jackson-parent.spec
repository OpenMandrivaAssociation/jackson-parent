Name:		jackson-parent
Version:	2.23
Release:	1
Summary:	Parent POM for Jackson components
Group:		Development/Java
License:	ASL 2.0
URL:		https://github.com/FasterXML/jackson-parent
Source0:	https://github.com/FasterXML/jackson-parent/archive/%{name}-%{version}.tar.gz
Source1:	https://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:	noarch
BuildRequires:	python
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	mvn(com.fasterxml:oss-parent:pom::)
BuildRequires:	fasterxml-oss-parent >= 81
BuildSystem:	maven
BuildOption:	-N validate

%description
Parent POM for the Jackson components.
2.23 selects FasterXML oss-parent 81. Release 2.22 selected 79.
The managed plugin versions come from that oss-parent.

%prep
%setup -q -n jackson-parent-jackson-parent-%{version}
cp -p %{SOURCE1} .

%files -f .mfiles
%doc LICENSE-2.0.txt README.md

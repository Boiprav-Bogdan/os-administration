Name:		count_files
Version:	1.0
Release:	1%{?dist}
Summary:	Count files in /etc
License:	MIT
BuildArch:	noarch
Requires:	bash
Source0:	count_files.sh

%description
This is a script that counts files in /etc.

%prep

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}/%{_bindir}/count_files.sh

%files
%{_bindir}/count_files.sh

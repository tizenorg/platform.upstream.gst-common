Name:           gst-common
Version:        20130618
Release:        0
License:        LGPL-2.0
Summary:        Gstreamer Common Files
Group:          Multimedia/Development
Source:         %{name}-%{version}.tar.bz2
Source1001: 	gst-common.manifest

%description
Gstreamer Common Files.

%prep
%setup -q
cp %{SOURCE1001} .

%build
rm -rf .gitignore

%install
mkdir -p %{buildroot}/%{_datadir}/gst-common
cp -a . %{buildroot}/%{_datadir}/gst-common

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_datadir}/gst-common

%changelog

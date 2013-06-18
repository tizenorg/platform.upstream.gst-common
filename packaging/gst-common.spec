Name:           gst-common
Version:        20130618
Release:        0
License:        LGPL-2.0
Summary:        Gstreamer Common Files
Group:          Multimedia/Development
Source:         %{name}-%{version}.tar.bz2

%description
Gstreamer Common Files.

%prep
%setup -q

%build

%install
mkdir %{buildroot}/%{_datadir}/gst-common
cp -a . %{buildroot}/%{_datadir}/gst-common

%files
%defattr(-,root,root)
%{_datadir}/gst-common

%changelog

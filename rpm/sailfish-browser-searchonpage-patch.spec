Name:       sailfish-browser-searchonpage-patch

# >> macros
BuildArch: noarch
# << macros

Summary:    Search text on page in Browser
Version:    0.0.2
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   sailfish-browser >= 1.1.23.2

%description
A sailfish-browser patch enabling search text on page


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfish-browser-searchonpage-patch
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfish-browser-searchonpage-patch
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfish-browser-searchonpage-patch
# >> files
# << files

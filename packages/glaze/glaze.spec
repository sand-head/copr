# Maintained at https://github.com/sand-head/copr
%global forgeurl https://github.com/stephenberry/glaze
%global _description %{expand:
%{summary}.}

Name:           glaze
Version:        7.1.1
Release:        %autorelease
Summary:        Header-only C++23 JSON and serialization library

License:        MIT
URL:            %{forgeurl}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.21
BuildRequires:  gcc-c++

BuildArch:      noarch

%description %{_description}

%prep
%autosetup -n %{name}-%{version}

%build
%cmake \
    -Dglaze_DEVELOPER_MODE=OFF \
    -Dbuild_testing=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_includedir}/glaze/
%{_datadir}/glaze/

%changelog
%autochangelog

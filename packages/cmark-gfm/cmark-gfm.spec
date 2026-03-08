%global forgeurl https://github.com/github/cmark-gfm
%global _description %{expand:
GitHub's fork of cmark, adding GitHub Flavored Markdown extensions to the
upstream CommonMark reference implementation.}

Name:           cmark-gfm
Version:        0.29.0.gfm.13
Release:        %autorelease
Summary:        GitHub Flavored Markdown parsing and rendering library

License:        BSD-2-Clause AND MIT
URL:            %{forgeurl}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.0
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description %{_description}

%package libs
Summary:        Shared libraries for cmark-gfm

%description libs
Shared libraries for the cmark-gfm CommonMark parsing and rendering library
with GitHub Flavored Markdown extensions.

%package devel
Summary:        Development files for cmark-gfm
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Headers, pkg-config files, and CMake targets for developing against cmark-gfm.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake \
    -DCMARK_SHARED=ON \
    -DCMARK_STATIC=OFF \
    -DCMARK_TESTS=OFF
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets libs

%files
%license COPYING
%{_bindir}/cmark-gfm
%{_mandir}/man1/cmark-gfm.1*

%files libs
%license COPYING
%{_libdir}/libcmark-gfm.so.%{version}
%{_libdir}/libcmark-gfm-extensions.so.%{version}

%files devel
%doc README.md
%{_includedir}/cmark-gfm.h
%{_includedir}/cmark-gfm_export.h
%{_includedir}/cmark-gfm_version.h
%{_includedir}/cmark-gfm-core-extensions.h
%{_includedir}/cmark-gfm-extension_api.h
%{_libdir}/libcmark-gfm.so
%{_libdir}/libcmark-gfm-extensions.so
%{_libdir}/pkgconfig/libcmark-gfm.pc
%{_libdir}/cmake/cmark-gfm.cmake
%{_libdir}/cmake/cmark-gfm-release.cmake
%{_libdir}/cmake-gfm-extensions/cmark-gfm-extensions.cmake
%{_libdir}/cmake-gfm-extensions/cmark-gfm-extensions-release.cmake
%{_mandir}/man3/cmark-gfm.3*

%changelog
%autochangelog

%global forgeurl https://github.com/vicinaehq/vicinae
%global _description %{expand:
%{summary}.}

Name:           vicinae
Version:        0.19.3
Release:        %autorelease
Summary:        A focused launcher for your desktop

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++ >= 15
BuildRequires:  ninja-build
BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(absl_base)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmark-gfm-devel
BuildRequires:  minizip-devel
BuildRequires:  glaze-devel
BuildRequires:  desktop-file-utils

Requires:       nodejs

%description %{_description}

%prep
%autosetup -n %{name}-%{version}

%build
pushd src/typescript/api
npm ci --legacy-peer-deps
popd

pushd src/typescript/extension-manager
npm ci --legacy-peer-deps
popd

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DVICINAE_GIT_TAG=v%{version} \
    -DVICINAE_GIT_COMMIT_HASH=d2f38c2b1 \
    -DVICINAE_PROVENANCE=fedora \
    -DINSTALL_NODE_MODULES=OFF \
    -DUSE_SYSTEM_PROTOBUF=ON \
    -DUSE_SYSTEM_ABSEIL=ON \
    -DUSE_SYSTEM_CMARK_GFM=ON \
    -DUSE_SYSTEM_LAYER_SHELL=ON \
    -DUSE_SYSTEM_GLAZE=ON \
    -DUSE_SYSTEM_QT_KEYCHAIN=ON \
    -DLIBQALCULATE_BACKEND=ON \
    -DWAYLAND_LAYER_SHELL=ON \
    -DTYPESCRIPT_EXTENSIONS=ON

%cmake_build

%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/vicinae.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/vicinae-url-handler.desktop

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/vicinae
%{_bindir}/vicinae-snippet
%{_libexecdir}/vicinae/
%{_datadir}/applications/vicinae.desktop
%{_datadir}/applications/vicinae-url-handler.desktop
%{_datadir}/icons/hicolor/512x512/apps/vicinae.png
%{_datadir}/vicinae/
%{_userunitdir}/vicinae.service

%changelog
%autochangelog

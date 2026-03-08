%global forgeurl https://github.com/vicinaehq/vicinae
%global _description %{expand:
%{summary}.}

Name:           vicinae
Version:        0.20.3
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
BuildRequires:  desktop-file-utils
BuildRequires:  glaze
BuildRequires:  libicu-devel
BuildRequires:  minizip-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(absl)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcmark-gfm)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  wayland-devel

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
    -DVICINAE_GIT_COMMIT_HASH=e550ea4ff6ced8d1747df4608e1612b28a9d48a4 \
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
%{_libexecdir}/vicinae/
%{_sysconfdir}/chromium/native-messaging-hosts/com.vicinae.vicinae.json
%{_prefix}/lib/modules-load.d/vicinae.conf
%{_prefix}/lib/mozilla/native-messaging-hosts/com.vicinae.vicinae.json
%{_prefix}/lib/udev/rules.d/70-vicinae.rules
%{_datadir}/applications/vicinae.desktop
%{_datadir}/applications/vicinae-url-handler.desktop
%{_datadir}/icons/hicolor/512x512/apps/vicinae.png
%{_datadir}/vicinae/
%{_userunitdir}/vicinae.service

%changelog
%autochangelog

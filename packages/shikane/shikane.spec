%global forgeurl https://github.com/hw0lff/shikane
%global _description %{expand:
%{summary}.}

Name:           shikane
Version:        1.0.1
Release:        %autorelease
Summary:        Dynamic output configuration tool for Wayland

License:        MIT
URL:            %{forgeurl}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  rust-packaging >= 21
BuildRequires:  cargo
BuildRequires:  pandoc
BuildRequires:  make

Requires:       wayland-protocols

ExclusiveArch:  %{rust_arches}

%description %{_description}

%prep
%autosetup -n %{name}-%{version}
%cargo_prep

%build
%cargo_build
./scripts/build-docs.sh man

%install
%cargo_install

install -Dm644 build/man/shikane.1.gz %{buildroot}%{_mandir}/man1/shikane.1.gz
install -Dm644 build/man/shikane.5.gz %{buildroot}%{_mandir}/man5/shikane.5.gz
install -Dm644 build/man/shikanectl.1.gz %{buildroot}%{_mandir}/man1/shikanectl.1.gz

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/shikane
%{_bindir}/shikanectl
%{_mandir}/man1/shikane.1*
%{_mandir}/man5/shikane.5*
%{_mandir}/man1/shikanectl.1*

%changelog
%autochangelog

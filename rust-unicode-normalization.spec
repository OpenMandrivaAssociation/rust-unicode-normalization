%bcond_without check
%global debug_package %{nil}

%global crate unicode-normalization

Name:           rust-%{crate}
Version:        0.1.17
Release:        3
Summary:        Functions for normalization of Unicode strings, including Canonical and Compatible Decomposition and Recomposition, as described in Unicode Standard Annex #15

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unicode-normalization
Source:         %{crates_source}
# Initial patched metadata
# * Exclude unneeded scripts, https://github.com/unicode-rs/unicode-normalization/pull/30
Patch0:		unicode-normalization-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(tinyvec/alloc) >= 1.0.0 with crate(tinyvec/alloc) < 2.0.0)
BuildRequires:  (crate(tinyvec/default) >= 1.0.0 with crate(tinyvec/default) < 2.0.0)
%endif

%global _description %{expand:
Functions for normalization of Unicode strings, including Canonical and
Compatible Decomposition and Recomposition, as described in Unicode Standard
Annex #15.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(unicode-normalization) = 0.1.17
Requires:       cargo
Requires:       (crate(tinyvec/default) >= 1.0.0 with crate(tinyvec/default) < 2.0.0)
Requires:	(crate(tinyvec/alloc) >= 1.0.0 with crate(tinyvec/alloc) < 2.0.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(unicode-normalization/default) = 0.1.17
Requires:       cargo
Requires:       crate(unicode-normalization) = 0.1.17
Requires:       crate(unicode-normalization/std) = 0.1.17

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(unicode-normalization/std) = 0.1.17
Requires:       cargo
Requires:       crate(unicode-normalization) = 0.1.17

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

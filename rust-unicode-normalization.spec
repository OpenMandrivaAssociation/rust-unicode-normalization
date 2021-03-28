%bcond_without check
%global debug_package %{nil}

%global crate unicode-normalization

Name:           rust-%{crate}
Version:        0.1.17
Release:        1
Summary:        Functions for normalization of Unicode strings

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/unicode-normalization
Source:         %{crates_source}
# Initial patched metadata
# * Exclude unneeded scripts, https://github.com/unicode-rs/unicode-normalization/pull/30
Patch0:         unicode-normalization-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Functions for normalization of Unicode strings, including Canonical and
Compatible Decomposition and Recomposition, as described in Unicode Standard
Annex #15.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE COPYRIGHT
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Josh Stone <jistone@redhat.com> - 0.1.12-1
- Update to 0.1.12

* Fri Nov 22 2019 Josh Stone <jistone@redhat.com> - 0.1.11-1
- Update to 0.1.11

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 0.1.9-1
- Update to 0.1.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 11:26:29 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-3
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Josh Stone <jistone@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Sat Nov 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-3
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Thu May 03 2018 Josh Stone <jistone@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-3
- Rebuild for rust-packaging v5

* Sun Nov 05 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-2
- Exclude unneeded files

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-2
- Port to use rust-packaging

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Initial package

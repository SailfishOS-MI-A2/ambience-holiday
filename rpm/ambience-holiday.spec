Name: ambience-holiday

Summary: Holiday Ambience
Version: 0.1
Release:    1
Group:      System/GUI/Other
License:    TBD
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qt5-qmake
%if %{with l10n}
BuildRequires: %{name}-all-translations
#!BuildIgnore: %{name}-all-translations-pack
%define _all_translations_version %(rpm -q --queryformat "%{version}-%{release}" %{name}-all-translations)
Requires: %{name}-all-translations >= %{_all_translations_version}
%endif
BuildRequires:  ambienced >= 0.26.32
BuildRequires:  ambienced-devel >= 0.26.32

%_ambience_requires
%_ambience_requires_tones

%description
Holiday Ambience for Sailfish OS 3.x.x

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%files
%_ambience_files

%post
%_ambience_post

%postun
%_ambience_trigger_update

%_ambience_tones_package Holiday

%_ambience_translation_package Holiday

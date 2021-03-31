#define snapshot 20200916
#define commit cc1ac2452e41873741c8b5f3fcafa29ae3ce5a30

Name:		kalk
Version:	0.2
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Calculator for Plasma Mobile
Source0:	https://invent.kde.org/plasma-mobile/kalk/-/archive/v%{version}/kalk-v%{version}.tar.bz2
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5UnitConversion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	bison
BuildRequires:	flex

%description
Calculator for Plasma Mobile

%prep
%autosetup -p1 -n kalk-v%{version}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/kalk
%{_datadir}/applications/org.kde.kalk.desktop
%{_datadir}/icons/hicolor/scalable/apps/kalk.svg
%{_datadir}/metainfo/org.kde.kalk.appdata.xml

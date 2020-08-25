%define snapshot 20200825
%define commit 44a24136cb99c17142364f0b647319d6d1aa7b99

Name:		kalk
Version:	0.1.1
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Calculator for Plasma Mobile
Source0:	https://invent.kde.org/plasma-mobile/kalk/-/archive/master/kalk-master.tar.bz2
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
BuildRequires:	bison
BuildRequires:	flex

%description
Calculator for Plasma Mobile

%prep
%autosetup -p1 -n kalk-master
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

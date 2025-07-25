#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Name:		kalk
Version:	25.04.3
Release:	%{?git:0.%{git}.}1
Summary:	Calculator for Plasma Mobile made in Qt6 and KF6
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/kalk/-/archive/%{gitbranch}/kalk-%{gitbranchd}.tar.bz2#/kalk-%{git}.tar.bz2
%else
%define stable %(if [ "$(echo %{version}|cut -d. -f3)" -ge 50 ]; then echo -n un; fi; echo -n stable)
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/kalk-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:  cmake(Qt6)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6UnitConversion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig(mpfr)
BuildRequires:	pkgconfig(gmp)
BuildRequires:  pkgconfig(libqalculate)

Requires: kf6-kirigami
Requires: %{_lib}KF6Kirigami
# This is wrong but looks like qt6qml devel contains needed qml() components.
#Requires: cmake(Qt6Qml)
Requires: kf6-qqc2-desktop-style

%rename plasma6-kalk

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Calculator for Plasma Mobile

%files -f %{name}.lang
%{_bindir}/kalk
%{_datadir}/applications/org.kde.kalk.desktop
%{_datadir}/metainfo/org.kde.kalk.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.kalk.svg

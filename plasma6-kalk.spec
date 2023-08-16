Name:		plasma6-kalk
Version:	23.07.90
Release:	1
Summary:	Calculator for Plasma Mobile made in Qt6 and KF6
Source0:	https://invent.kde.org/plasma-mobile/kalk/-/archive/v%{version}/kalk-v%{version}.tar.bz2
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:  cmake(Qt6)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6UnitConversion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig(mpfr)
BuildRequires:	pkgconfig(gmp)

%description
Calculator for Plasma Mobile

%prep
%autosetup -n kalk-v%{version} -p1
%cmake  \
        -G Ninja \
        -DBUILD_WITH_QT6:BOOL=ON \

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kalk

%files -f kalk.lang
%{_bindir}/kalk
%{_datadir}/applications/org.kde.kalk.desktop
%{_datadir}/metainfo/org.kde.kalk.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.kalk.svg

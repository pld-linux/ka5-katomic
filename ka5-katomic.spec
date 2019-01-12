%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		katomic
Summary:	katomic
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	734809810e96ccb116f75583ff08b6c0
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-knewstuff-devel >= 5.30.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAtomic is a fun educational game built around molecular geometry. It
employs simplistic two-dimensional looks at different chemical
elements.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/katomic.knsrc
%attr(755,root,root) %{_bindir}/katomic
%{_desktopdir}/org.kde.katomic.desktop
%{_iconsdir}/hicolor/128x128/apps/katomic.png
%{_iconsdir}/hicolor/16x16/apps/katomic.png
%{_iconsdir}/hicolor/22x22/apps/katomic.png
%{_iconsdir}/hicolor/32x32/apps/katomic.png
%{_iconsdir}/hicolor/48x48/apps/katomic.png
%{_iconsdir}/hicolor/64x64/apps/katomic.png
%{_datadir}/katomic
%attr(755,root,root) %{_datadir}/kconf_update/katomic-levelset-upd.pl
%{_datadir}/kconf_update/katomic-levelset.upd
%{_datadir}/kxmlgui5/katomic
%{_datadir}/metainfo/org.kde.katomic.appdata.xml


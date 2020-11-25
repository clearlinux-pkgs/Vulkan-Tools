#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Vulkan-Tools
Version  : 1.2.162
Release  : 35
URL      : https://github.com/KhronosGroup/Vulkan-Tools/archive/v1.2.162/Vulkan-Tools-1.2.162.tar.gz
Source0  : https://github.com/KhronosGroup/Vulkan-Tools/archive/v1.2.162/Vulkan-Tools-1.2.162.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: Vulkan-Tools-bin = %{version}-%{release}
Requires: Vulkan-Tools-license = %{version}-%{release}
BuildRequires : Vulkan-Headers-data
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Headers-dev Vulkan-Loader-dev Vulkan-Tools
BuildRequires : Vulkan-Loader-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : glslang-bin
BuildRequires : glslang-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : python3

%description
# Vulkan Ecosystem Components
This project provides Khronos official Vulkan Tools and Utilities for Windows, Linux, Android, and MacOS.

%package bin
Summary: bin components for the Vulkan-Tools package.
Group: Binaries
Requires: Vulkan-Tools-license = %{version}-%{release}

%description bin
bin components for the Vulkan-Tools package.


%package license
Summary: license components for the Vulkan-Tools package.
Group: Default

%description license
license components for the Vulkan-Tools package.


%prep
%setup -q -n Vulkan-Tools-1.2.162
cd %{_builddir}/Vulkan-Tools-1.2.162

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1606323976
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DBUILD_WSI_MIR_SUPPORT=OFF \
-DGLSLANG_INSTALL_DIR=/usr \
-DBUILD_WSI_DIRECTFB_SUPPORT=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1606323976
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Vulkan-Tools
cp %{_builddir}/Vulkan-Tools-1.2.162/LICENSE.txt %{buildroot}/usr/share/package-licenses/Vulkan-Tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/Vulkan-Tools-1.2.162/windows-runtime-installer/VulkanRT-License.txt %{buildroot}/usr/share/package-licenses/Vulkan-Tools/884fc355c7334e66b002ff40965b6f9904805d0e
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vkcube
/usr/bin/vkcubepp
/usr/bin/vulkaninfo

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Vulkan-Tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/Vulkan-Tools/884fc355c7334e66b002ff40965b6f9904805d0e

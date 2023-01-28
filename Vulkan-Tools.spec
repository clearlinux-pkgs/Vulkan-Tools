#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Vulkan-Tools
Version  : 1.3.240
Release  : 104
URL      : https://github.com/KhronosGroup/Vulkan-Tools/archive/v1.3.240/Vulkan-Tools-1.3.240.tar.gz
Source0  : https://github.com/KhronosGroup/Vulkan-Tools/archive/v1.3.240/Vulkan-Tools-1.3.240.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: Vulkan-Tools-bin = %{version}-%{release}
Requires: Vulkan-Tools-license = %{version}-%{release}
BuildRequires : Vulkan-Headers-data
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Headers-dev Vulkan-Loader-dev Vulkan-Tools
BuildRequires : Vulkan-Loader-dev
BuildRequires : buildreq-cmake
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules wayland
BuildRequires : glslang-bin
BuildRequires : glslang-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcb)
BuildRequires : python3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n Vulkan-Tools-1.3.240
cd %{_builddir}/Vulkan-Tools-1.3.240

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1674946911
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake .. -DBUILD_WSI_MIR_SUPPORT=OFF \
-DGLSLANG_INSTALL_DIR=/usr \
-DBUILD_WSI_DIRECTFB_SUPPORT=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1674946911
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Vulkan-Tools
cp %{_builddir}/Vulkan-Tools-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/Vulkan-Tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/Vulkan-Tools-%{version}/windows-runtime-installer/VulkanRT-License.txt %{buildroot}/usr/share/package-licenses/Vulkan-Tools/84fbabc68c29007b8b7762962b0bba1137648f5e || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vkcube
/usr/bin/vkcube-wayland
/usr/bin/vkcubepp
/usr/bin/vulkaninfo

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Vulkan-Tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/Vulkan-Tools/84fbabc68c29007b8b7762962b0bba1137648f5e

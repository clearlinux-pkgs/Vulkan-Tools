#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: 250a666
#
Name     : Vulkan-Tools
Version  : 1.3.269
Release  : 121
URL      : https://github.com/KhronosGroup/Vulkan-Tools/archive/v1.3.269/Vulkan-Tools-1.3.269.tar.gz
Source0  : https://github.com/KhronosGroup/Vulkan-Tools/archive/v1.3.269/Vulkan-Tools-1.3.269.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: Vulkan-Tools-bin = %{version}-%{release}
Requires: Vulkan-Tools-license = %{version}-%{release}
BuildRequires : Vulkan-Headers-data
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : buildreq-cmake
BuildRequires : glslang-bin
BuildRequires : glslang-dev
BuildRequires : googletest-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcb)
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KhronosGroup/Vulkan-Tools
This project provides Vulkan tools and utilities that can assist development by enabling developers to verify their applications correct use of the Vulkan API.

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
%setup -q -n Vulkan-Tools-1.3.269
cd %{_builddir}/Vulkan-Tools-1.3.269

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698075145
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake .. -DBUILD_WSI_MIR_SUPPORT=OFF \
-DGLSLANG_INSTALL_DIR=/usr \
-DBUILD_WSI_DIRECTFB_SUPPORT=OFF
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DBUILD_WSI_MIR_SUPPORT=OFF \
-DGLSLANG_INSTALL_DIR=/usr \
-DBUILD_WSI_DIRECTFB_SUPPORT=OFF
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1698075145
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Vulkan-Tools
cp %{_builddir}/Vulkan-Tools-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/Vulkan-Tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/Vulkan-Tools-%{version}/windows-runtime-installer/VulkanRT-License.txt %{buildroot}/usr/share/package-licenses/Vulkan-Tools/019db59a3c8808deb65bc3a9c3b59b8ed8c0c762 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/vkcube
/V3/usr/bin/vkcubepp
/V3/usr/bin/vulkaninfo
/usr/bin/vkcube
/usr/bin/vkcubepp
/usr/bin/vulkaninfo

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Vulkan-Tools/019db59a3c8808deb65bc3a9c3b59b8ed8c0c762
/usr/share/package-licenses/Vulkan-Tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890

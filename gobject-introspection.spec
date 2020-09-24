#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gobject-introspection
Version  : 1.66.0
Release  : 37
URL      : https://github.com/GNOME/gobject-introspection/archive/1.66.0/gobject-introspection-1.66.0.tar.gz
Source0  : https://github.com/GNOME/gobject-introspection/archive/1.66.0/gobject-introspection-1.66.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: gobject-introspection-bin = %{version}-%{release}
Requires: gobject-introspection-data = %{version}-%{release}
Requires: gobject-introspection-lib = %{version}-%{release}
Requires: gobject-introspection-license = %{version}-%{release}
Requires: gobject-introspection-man = %{version}-%{release}
Requires: glibc-bin
BuildRequires : Mako
BuildRequires : bison
BuildRequires : buildreq-meson
BuildRequires : cairo-dev
BuildRequires : flex
BuildRequires : glib-dev
BuildRequires : glibc-bin
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-gobject)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : python3-dev

%description
GObject Introspection
=====================
The goal of the project is to describe the APIs and collect them in
a uniform, machine readable format.

%package bin
Summary: bin components for the gobject-introspection package.
Group: Binaries
Requires: gobject-introspection-data = %{version}-%{release}
Requires: gobject-introspection-license = %{version}-%{release}

%description bin
bin components for the gobject-introspection package.


%package data
Summary: data components for the gobject-introspection package.
Group: Data

%description data
data components for the gobject-introspection package.


%package dev
Summary: dev components for the gobject-introspection package.
Group: Development
Requires: gobject-introspection-lib = %{version}-%{release}
Requires: gobject-introspection-bin = %{version}-%{release}
Requires: gobject-introspection-data = %{version}-%{release}
Provides: gobject-introspection-devel = %{version}-%{release}
Requires: gobject-introspection = %{version}-%{release}

%description dev
dev components for the gobject-introspection package.


%package lib
Summary: lib components for the gobject-introspection package.
Group: Libraries
Requires: gobject-introspection-data = %{version}-%{release}
Requires: gobject-introspection-license = %{version}-%{release}

%description lib
lib components for the gobject-introspection package.


%package license
Summary: license components for the gobject-introspection package.
Group: Default

%description license
license components for the gobject-introspection package.


%package man
Summary: man components for the gobject-introspection package.
Group: Default

%description man
man components for the gobject-introspection package.


%prep
%setup -q -n gobject-introspection-1.66.0
cd %{_builddir}/gobject-introspection-1.66.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600273399
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gobject-introspection
cp %{_builddir}/gobject-introspection-1.66.0/COPYING %{buildroot}/usr/share/package-licenses/gobject-introspection/80fe7119545c554233bbac373a7d8b0104e45cd1
cp %{_builddir}/gobject-introspection-1.66.0/COPYING.GPL %{buildroot}/usr/share/package-licenses/gobject-introspection/dfac199a7539a404407098a2541b9482279f690d
cp %{_builddir}/gobject-introspection-1.66.0/COPYING.LGPL %{buildroot}/usr/share/package-licenses/gobject-introspection/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/g-ir-annotation-tool
/usr/bin/g-ir-compiler
/usr/bin/g-ir-generate
/usr/bin/g-ir-inspect
/usr/bin/g-ir-scanner

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/DBus-1.0.typelib
/usr/lib64/girepository-1.0/DBusGLib-1.0.typelib
/usr/lib64/girepository-1.0/GIRepository-2.0.typelib
/usr/lib64/girepository-1.0/GL-1.0.typelib
/usr/lib64/girepository-1.0/GLib-2.0.typelib
/usr/lib64/girepository-1.0/GModule-2.0.typelib
/usr/lib64/girepository-1.0/GObject-2.0.typelib
/usr/lib64/girepository-1.0/Gio-2.0.typelib
/usr/lib64/girepository-1.0/Vulkan-1.0.typelib
/usr/lib64/girepository-1.0/cairo-1.0.typelib
/usr/lib64/girepository-1.0/fontconfig-2.0.typelib
/usr/lib64/girepository-1.0/freetype2-2.0.typelib
/usr/lib64/girepository-1.0/libxml2-2.0.typelib
/usr/lib64/girepository-1.0/win32-1.0.typelib
/usr/lib64/girepository-1.0/xfixes-4.0.typelib
/usr/lib64/girepository-1.0/xft-2.0.typelib
/usr/lib64/girepository-1.0/xlib-2.0.typelib
/usr/lib64/girepository-1.0/xrandr-1.3.typelib
/usr/share/gir-1.0/*.gir
/usr/share/gir-1.0/gir-1.2.rnc
/usr/share/gobject-introspection-1.0/Makefile.introspection
/usr/share/gobject-introspection-1.0/gdump.c
/usr/share/gobject-introspection-1.0/tests/annotation.c
/usr/share/gobject-introspection-1.0/tests/annotation.h
/usr/share/gobject-introspection-1.0/tests/drawable.c
/usr/share/gobject-introspection-1.0/tests/drawable.h
/usr/share/gobject-introspection-1.0/tests/everything.c
/usr/share/gobject-introspection-1.0/tests/everything.h
/usr/share/gobject-introspection-1.0/tests/foo.c
/usr/share/gobject-introspection-1.0/tests/foo.h
/usr/share/gobject-introspection-1.0/tests/gimarshallingtests.c
/usr/share/gobject-introspection-1.0/tests/gimarshallingtests.h
/usr/share/gobject-introspection-1.0/tests/gitestmacros.h
/usr/share/gobject-introspection-1.0/tests/regress.c
/usr/share/gobject-introspection-1.0/tests/regress.h
/usr/share/gobject-introspection-1.0/tests/utility.c
/usr/share/gobject-introspection-1.0/tests/utility.h
/usr/share/gobject-introspection-1.0/tests/warnlib.c
/usr/share/gobject-introspection-1.0/tests/warnlib.h

%files dev
%defattr(-,root,root,-)
/usr/include/gobject-introspection-1.0/giarginfo.h
/usr/include/gobject-introspection-1.0/gibaseinfo.h
/usr/include/gobject-introspection-1.0/gicallableinfo.h
/usr/include/gobject-introspection-1.0/giconstantinfo.h
/usr/include/gobject-introspection-1.0/gienuminfo.h
/usr/include/gobject-introspection-1.0/gifieldinfo.h
/usr/include/gobject-introspection-1.0/gifunctioninfo.h
/usr/include/gobject-introspection-1.0/giinterfaceinfo.h
/usr/include/gobject-introspection-1.0/giobjectinfo.h
/usr/include/gobject-introspection-1.0/gipropertyinfo.h
/usr/include/gobject-introspection-1.0/giregisteredtypeinfo.h
/usr/include/gobject-introspection-1.0/girepository.h
/usr/include/gobject-introspection-1.0/girffi.h
/usr/include/gobject-introspection-1.0/gisignalinfo.h
/usr/include/gobject-introspection-1.0/gistructinfo.h
/usr/include/gobject-introspection-1.0/gitypeinfo.h
/usr/include/gobject-introspection-1.0/gitypelib.h
/usr/include/gobject-introspection-1.0/gitypes.h
/usr/include/gobject-introspection-1.0/giunioninfo.h
/usr/include/gobject-introspection-1.0/giversion.h
/usr/include/gobject-introspection-1.0/giversionmacros.h
/usr/include/gobject-introspection-1.0/givfuncinfo.h
/usr/lib64/libgirepository-1.0.so
/usr/lib64/pkgconfig/gobject-introspection-1.0.pc
/usr/lib64/pkgconfig/gobject-introspection-no-export-1.0.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib64/gobject-introspection/giscanner/__init__.py
/usr/lib64/gobject-introspection/giscanner/_giscanner.cpython-38-x86_64-linux-gnu.so
/usr/lib64/gobject-introspection/giscanner/_version.py
/usr/lib64/gobject-introspection/giscanner/annotationmain.py
/usr/lib64/gobject-introspection/giscanner/annotationparser.py
/usr/lib64/gobject-introspection/giscanner/ast.py
/usr/lib64/gobject-introspection/giscanner/cachestore.py
/usr/lib64/gobject-introspection/giscanner/ccompiler.py
/usr/lib64/gobject-introspection/giscanner/codegen.py
/usr/lib64/gobject-introspection/giscanner/docmain.py
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/_doc.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/_index.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/_method.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/_methods.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/_properties.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/_signals.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/_staticmethods.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/_vfuncs.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/base.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/callback.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/class.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/default.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/enum.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/function.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/interface.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/method.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/devdocs/Gjs/namespace.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/callback.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/class.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/constructor.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/default.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/enum.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/field.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/function.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/interface.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/method.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/namespace.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/property.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/record.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/signal.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/C/vfunc.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/callback.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/class.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/constructor.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/default.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/enum.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/field.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/function.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/interface.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/method.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/namespace.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/property.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/record.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/signal.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Gjs/vfunc.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/callback.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/class.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/constructor.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/default.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/enum.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/field.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/function.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/interface.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/method.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/namespace.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/property.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/record.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/signal.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/Python/vfunc.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/base.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/class.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/mallard/namespace.tmpl
/usr/lib64/gobject-introspection/giscanner/docwriter.py
/usr/lib64/gobject-introspection/giscanner/dumper.py
/usr/lib64/gobject-introspection/giscanner/gdumpparser.py
/usr/lib64/gobject-introspection/giscanner/girparser.py
/usr/lib64/gobject-introspection/giscanner/girwriter.py
/usr/lib64/gobject-introspection/giscanner/introspectablepass.py
/usr/lib64/gobject-introspection/giscanner/libtoolimporter.py
/usr/lib64/gobject-introspection/giscanner/maintransformer.py
/usr/lib64/gobject-introspection/giscanner/mdextensions.py
/usr/lib64/gobject-introspection/giscanner/message.py
/usr/lib64/gobject-introspection/giscanner/msvccompiler.py
/usr/lib64/gobject-introspection/giscanner/pkgconfig.py
/usr/lib64/gobject-introspection/giscanner/scannermain.py
/usr/lib64/gobject-introspection/giscanner/sectionparser.py
/usr/lib64/gobject-introspection/giscanner/shlibs.py
/usr/lib64/gobject-introspection/giscanner/sourcescanner.py
/usr/lib64/gobject-introspection/giscanner/testcodegen.py
/usr/lib64/gobject-introspection/giscanner/transformer.py
/usr/lib64/gobject-introspection/giscanner/utils.py
/usr/lib64/gobject-introspection/giscanner/xmlwriter.py
/usr/lib64/libgirepository-1.0.so.1
/usr/lib64/libgirepository-1.0.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gobject-introspection/80fe7119545c554233bbac373a7d8b0104e45cd1
/usr/share/package-licenses/gobject-introspection/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f
/usr/share/package-licenses/gobject-introspection/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/g-ir-compiler.1
/usr/share/man/man1/g-ir-generate.1
/usr/share/man/man1/g-ir-scanner.1

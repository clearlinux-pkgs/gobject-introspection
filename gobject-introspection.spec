#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gobject-introspection
Version  : 1.54.1
Release  : 20
URL      : https://github.com/GNOME/gobject-introspection/archive/1.54.1.tar.gz
Source0  : https://github.com/GNOME/gobject-introspection/archive/1.54.1.tar.gz
Summary  : GObject Introspection
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: gobject-introspection-bin
Requires: gobject-introspection-data
Requires: gobject-introspection-lib
Requires: gobject-introspection-doc
Requires: glibc-bin
BuildRequires : Mako
BuildRequires : bison
BuildRequires : docbook-xml
BuildRequires : flex
BuildRequires : glib-dev
BuildRequires : glibc-bin
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-gobject)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libffi)
BuildRequires : python-dev
BuildRequires : python3-dev

%description
GObject Introspection
=====================
The goal of the project is to describe the APIs and collect them in
a uniform, machine readable format.

%package bin
Summary: bin components for the gobject-introspection package.
Group: Binaries
Requires: gobject-introspection-data

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
Requires: gobject-introspection-lib
Requires: gobject-introspection-bin
Requires: gobject-introspection-data
Provides: gobject-introspection-devel
Requires: glibc-bin

%description dev
dev components for the gobject-introspection package.


%package doc
Summary: doc components for the gobject-introspection package.
Group: Documentation

%description doc
doc components for the gobject-introspection package.


%package lib
Summary: lib components for the gobject-introspection package.
Group: Libraries
Requires: gobject-introspection-data

%description lib
lib components for the gobject-introspection package.


%prep
%setup -q -n gobject-introspection-1.54.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517684209
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%autogen --disable-static --with-python=python3
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1517684209
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/g-ir-annotation-tool
/usr/bin/g-ir-compiler
/usr/bin/g-ir-doc-tool
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
/usr/include/gobject-introspection-1.0/giversionmacros.h
/usr/include/gobject-introspection-1.0/givfuncinfo.h
/usr/lib64/libgirepository-1.0.so
/usr/lib64/pkgconfig/gobject-introspection-1.0.pc
/usr/lib64/pkgconfig/gobject-introspection-no-export-1.0.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/gobject-introspection/giscanner/__init__.py
/usr/lib64/gobject-introspection/giscanner/__pycache__/__init__.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/annotationmain.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/annotationparser.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/ast.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/cachestore.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/ccompiler.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/codegen.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/docmain.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/docwriter.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/dumper.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/gdumpparser.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/girparser.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/girwriter.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/introspectablepass.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/libtoolimporter.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/maintransformer.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/message.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/msvccompiler.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/scannermain.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/sectionparser.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/shlibs.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/sourcescanner.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/testcodegen.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/transformer.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/utils.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/__pycache__/xmlwriter.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/_giscanner.so
/usr/lib64/gobject-introspection/giscanner/annotationmain.py
/usr/lib64/gobject-introspection/giscanner/annotationparser.py
/usr/lib64/gobject-introspection/giscanner/ast.py
/usr/lib64/gobject-introspection/giscanner/cachestore.py
/usr/lib64/gobject-introspection/giscanner/ccompiler.py
/usr/lib64/gobject-introspection/giscanner/codegen.py
/usr/lib64/gobject-introspection/giscanner/collections/__init__.py
/usr/lib64/gobject-introspection/giscanner/collections/__pycache__/__init__.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/collections/__pycache__/counter.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/collections/__pycache__/ordereddict.cpython-36.pyc
/usr/lib64/gobject-introspection/giscanner/collections/counter.py
/usr/lib64/gobject-introspection/giscanner/collections/ordereddict.py
/usr/lib64/gobject-introspection/giscanner/docmain.py
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/callback.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/class.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/constructor.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/default.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/enum.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/field.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/function.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/interface.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/method.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/namespace.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/property.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/record.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/signal.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/C/vfunc.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/callback.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/class.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/constructor.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/default.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/enum.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/field.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/function.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/interface.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/method.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/namespace.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/property.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/record.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/signal.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Gjs/vfunc.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/callback.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/class.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/constructor.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/default.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/enum.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/field.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/function.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/interface.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/method.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/namespace.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/property.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/record.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/signal.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/Python/vfunc.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/base.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/class.tmpl
/usr/lib64/gobject-introspection/giscanner/doctemplates/namespace.tmpl
/usr/lib64/gobject-introspection/giscanner/docwriter.py
/usr/lib64/gobject-introspection/giscanner/dumper.py
/usr/lib64/gobject-introspection/giscanner/gdumpparser.py
/usr/lib64/gobject-introspection/giscanner/girparser.py
/usr/lib64/gobject-introspection/giscanner/girwriter.py
/usr/lib64/gobject-introspection/giscanner/introspectablepass.py
/usr/lib64/gobject-introspection/giscanner/libtoolimporter.py
/usr/lib64/gobject-introspection/giscanner/maintransformer.py
/usr/lib64/gobject-introspection/giscanner/message.py
/usr/lib64/gobject-introspection/giscanner/msvccompiler.py
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

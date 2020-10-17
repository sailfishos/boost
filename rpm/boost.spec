%ifarch ppc64le
  %bcond_with mpich
%else
  %bcond_without mpich
%endif

%ifnarch %{ix86} x86_64
  %bcond_with quadmath
%else
  %bcond_without quadmath
%endif

Name: boost
Summary: The free peer-reviewed portable C++ source libraries
# Update libboost_thread-mt.so on each version change
Version: 1.66.0
Release: 1
License: Boost and MIT and Python

URL: http://www.boost.org
Source0: %{name}-%{version}.tar.bz2
Source1: ver.py
Source2: libboost_thread-mt.so

# Patches from opensuse
Patch0: boost-no_segfault_in_Regex_filter.patch
Patch1: boost-no_type_punning.patch
Patch2: boost-strict_aliasing.patch
Patch3: boost-thread.patch
Patch4: boost-use_std_xml_catalog.patch
Patch5: boost-aarch64-flags.patch
Patch6: boost-disable-pch-on-aarch64.patch
Patch7: boost-visibility.patch
Patch8: dynamic_linking.patch

# boost-rpmoptflags-only.patch, boost-pool_check_overflow.patch - included in Fedora patches

# Patches from fedora
# https://svn.boost.org/trac/boost/ticket/6150
Patch11: boost-1.50.0-fix-non-utf8-files.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=828856
# https://bugzilla.redhat.com/show_bug.cgi?id=828857
# https://svn.boost.org/trac/boost/ticket/6701
Patch12: boost-1.58.0-pool.patch

# https://svn.boost.org/trac/boost/ticket/5637
Patch13: boost-1.57.0-mpl-print.patch

# https://svn.boost.org/trac/boost/ticket/9038
Patch14: boost-1.58.0-pool-test_linking.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1190039
Patch17: boost-1.66.0-build-optflags.patch

# Prevent gcc.jam from setting -m32 or -m64.
Patch18: boost-1.66.0-address-model.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1318383
Patch19: boost-1.66.0-no-rpath.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1541035
Patch20: boost-1.66.0-bjam-build-flags.patch

#These two are gcc8 fixes, so disabled for now
# https://bugzilla.redhat.com/show_bug.cgi?id=1545092
#Patch21: boost-1.66.0-spirit-abs-overflow.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1585515
#Patch22: boost-1.66.0-compute.patch

BuildRequires: m4
BuildRequires: libstdc++-devel
BuildRequires: bzip2-devel
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(icu-uc)
%if %{with quadmath}
BuildRequires: libquadmath-devel
%endif
BuildRequires: chrpath

BuildRequires: fdupes

# python subpackage was removed in the great python2 purge
Obsoletes: %{name}-python <= 1.66.0
# removed because it contained only license files
Obsoletes: %{name}-doc <= 1.66.0

%bcond_with tests
%bcond_with docs_generated

%description
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been included in the C++ 2011 standard and
others have been proposed to the C++ Standards Committee for inclusion
in future standards.)

%package atomic
Summary: Run-Time component of boost atomic library

%description atomic

Run-Time support for Boost.Atomic, a library that provides atomic data
types and operations on these data types, as well as memory ordering
constraints required for coordinating multiple threads through atomic
variables.

%package chrono
Summary: Run-Time component of boost chrono library

%description chrono

Run-Time support for Boost.Chrono, a set of useful time utilities.

%package container
Summary: Run-Time component of boost container library

%description container

Boost.Container library implements several well-known containers,
including STL containers. The aim of the library is to offers advanced
features not present in standard containers or to offer the latest
standard draft features for compilers that comply with C++03.

%package date-time
Summary: Run-Time component of boost date-time library

%description date-time

Run-Time support for Boost Date Time, set of date-time libraries based
on generic programming concepts.

%package exception
Summary: Run-Time component of boost exception library

%description exception

Run-Time support for Boost Exception, set of libraries to ease the design 
of exception class hierarchies and to help write exception handling and 
error reporting code.

%package filesystem
Summary: Run-Time component of boost filesystem library

%description filesystem

Run-Time support for the Boost Filesystem Library, which provides
portable facilities to query and manipulate paths, files, and
directories.

%package graph
Summary: Run-Time component of boost graph library

%description graph

Run-Time support for the BGL graph library.  BGL interface and graph
components are generic, in the same sense as the the Standard Template
Library (STL).

%package iostreams
Summary: Run-Time component of boost iostreams library

%description iostreams

Run-Time support for Boost.IOStreams, a framework for defining streams,
stream buffers and i/o filters.

%package locale
Summary: Run-Time component of boost locale library
Requires: boost-chrono = %{version}-%{release}
Requires: boost-system = %{version}-%{release}
Requires: boost-thread = %{version}-%{release}

%description locale

Run-Time support for Boost.Locale, a set of localization and Unicode
handling tools.

%package log
Summary: Run-Time component of boost logging library

%description log

Boost.Log library aims to make logging significantly easier for the
application developer.  It provides a wide range of out-of-the-box
tools along with public interfaces for extending the library.


%package math
Summary: Math functions for boost TR1 library
%if %{with quadmath}
Requires: libquadmath
%endif

%description math

Run-Time support for C99 and C++ TR1 C-style Functions from math
portion of Boost.TR1.

%package program-options
Summary:  Run-Time component of boost program_options library

%description program-options

Run-Time support of boost program options library, which allows program
developers to obtain (name, value) pairs from the user, via
conventional methods such as command line and configuration file.

%package random
Summary: Run-Time component of boost random library

%description random

Run-Time support for boost random library.

%package regex
Summary: Run-Time component of boost regular expression library

%description regex

Run-Time support for boost regular expression library.

%package serialization
Summary: Run-Time component of boost serialization library

%description serialization

Run-Time support for serialization for persistence and marshaling.

%package signals
Summary: Run-Time component of boost signals and slots library

%description signals

Run-Time support for managed signals & slots callback implementation.

%package stacktrace
Summary: Run-time component of boost stacktrace library

%description stacktrace

Run-time component of the Boost stacktrace library.

%package system
Summary: Run-Time component of boost system support library

%description system

Run-Time component of Boost operating system support library, including
the diagnostics support that will be part of the C++0x standard
library.

%package test
Summary: Run-Time component of boost test library

%description test

Run-Time support for simple program testing, full unit testing, and for
program execution monitoring.

%package thread
Summary: Run-Time component of boost thread library

%description thread

Run-Time component Boost.Thread library, which provides classes and
functions for managing multiple threads of execution, and for
synchronizing data between the threads or providing separate copies of
data specific to individual threads.

%package timer
Summary: Run-Time component of boost timer library
Requires: boost-chrono = %{version}-%{release}
Requires: boost-system = %{version}-%{release}

%description timer

"How long does my C++ code take to run?"
The Boost Timer library answers that question and does so portably,
with as little as one #include and one additional line of code.

%package type_erasure
Summary: Run-Time component of boost type erasure library
Requires: boost-chrono = %{version}-%{release}
Requires: boost-system = %{version}-%{release}

%description type_erasure

The Boost.TypeErasure library provides runtime polymorphism in C++
that is more flexible than that provided by the core language.

%package wave
Summary: Run-Time component of boost C99/C++ pre-processing library

%description wave

Run-Time support for the Boost.Wave library, a Standards conforming,
and highly configurable implementation of the mandated C99/C++
pre-processor functionality.

%package devel
Summary: The Boost C++ headers and shared development libraries
Requires: pkgconfig(icu-uc)
Requires: boost-atomic = %{version}-%{release}
Requires: boost-chrono = %{version}-%{release}
Requires: boost-container = %{version}-%{release}
Requires: boost-date-time = %{version}-%{release}
Requires: boost-exception = %{version}-%{release}
Requires: boost-filesystem = %{version}-%{release}
Requires: boost-graph = %{version}-%{release}
Requires: boost-iostreams = %{version}-%{release}
Requires: boost-locale = %{version}-%{release}
Requires: boost-log = %{version}-%{release}
Requires: boost-math = %{version}-%{release}
%if %{with quadmath}
Requires: libquadmath-devel
%endif
Requires: boost-program-options = %{version}-%{release}
Requires: boost-random = %{version}-%{release}
Requires: boost-regex = %{version}-%{release}
Requires: boost-serialization = %{version}-%{release}
Requires: boost-signals = %{version}-%{release}
Requires: boost-stacktrace = %{version}-%{release}
Requires: boost-system = %{version}-%{release}
Requires: boost-test = %{version}-%{release}
Requires: boost-thread = %{version}-%{release}
Requires: boost-timer = %{version}-%{release}
Requires: boost-type_erasure = %{version}-%{release}
Requires: boost-wave = %{version}-%{release}

%description devel
Headers and shared object symbolic links for the Boost C++ libraries.

%package static
Summary: The Boost C++ static development libraries
Requires: boost-devel = %{version}-%{release}
Provides: boost-devel-static = %{version}-%{release}

%description static
Static Boost C++ libraries.

%package jam
Summary: A low-level build tool

%description jam
Boost.Jam (BJam) is the low-level build engine tool for Boost.Build.
Historically, Boost.Jam is based on on FTJam and on Perforce Jam but has grown
a number of significant features and is now developed independently

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
./bootstrap.sh --with-toolset=gcc --with-icu --without-libraries=python

./b2 headers

# N.B. When we build the following with PCH, parts of boost (math
# library in particular) end up being built second time during
# installation.  Unsure why that is, but all sub-builds need to be
# built with pch=off to avoid this.

echo ============================= build serial ==================
./b2 -d+2 -q %{?_smp_mflags} --layout=tagged --without-python \
	--without-mpi --without-graph_parallel --build-dir=serial \
	--without-context --without-coroutine --without-fiber \
	variant=release threading=single,multi debug-symbols=on pch=off \
	stage

# See libs/thread/build/Jamfile.v2 for where this file comes from.
if [ $(find serial -type f -name has_atomic_flag_lockfree \
		-print -quit | wc -l) -ne 0 ]; then
	DEF=D
else
	DEF=U
fi

m4 -${DEF}HAS_ATOMIC_FLAG_LOCKFREE -DVERSION=%{version} \
	%{SOURCE2} > $(basename %{SOURCE2})

echo ============================= build Boost.Build ==================
(cd tools/build
 ./bootstrap.sh --with-toolset=gcc)


%install
rm -rf $RPM_BUILD_ROOT

echo ============================= install serial ==================
./b2 -d+2 -q %{?_smp_mflags} --layout=tagged --without-python \
	--without-mpi --without-graph_parallel --build-dir=serial \
	--without-context --without-coroutine --without-fiber \
	--prefix=$RPM_BUILD_ROOT%{_prefix} \
	--libdir=$RPM_BUILD_ROOT%{_libdir} \
	variant=release threading=single,multi debug-symbols=on pch=off \
	install

# Override DSO symlink with a linker script.  See the linker script
# itself for details of why we need to do this.
[ -f $RPM_BUILD_ROOT%{_libdir}/libboost_thread-mt.so ] # Must be present
rm -f $RPM_BUILD_ROOT%{_libdir}/libboost_thread-mt.so
install -p -m 644 $(basename %{SOURCE2}) $RPM_BUILD_ROOT%{_libdir}/

%fdupes %{buildroot}/
%fdupes %{buildroot}/%{_libdir}/
%fdupes %{buildroot}/%{_datadir}/


# MPI subpackages don't need the ldconfig magic.  They are hidden by
# default, in MPI back-end-specific directory, and only show to the
# user after the relevant environment module has been loaded.
# rpmlint will report that as errors, but it is fine.

%post atomic -p /sbin/ldconfig

%postun atomic -p /sbin/ldconfig

%post chrono -p /sbin/ldconfig

%postun chrono -p /sbin/ldconfig

%post container -p /sbin/ldconfig

%postun container -p /sbin/ldconfig

%post date-time -p /sbin/ldconfig

%postun date-time -p /sbin/ldconfig

%post exception -p /sbin/ldconfig

%postun exception -p /sbin/ldconfig

%post filesystem -p /sbin/ldconfig

%postun filesystem -p /sbin/ldconfig

%post graph -p /sbin/ldconfig

%postun graph -p /sbin/ldconfig

%post iostreams -p /sbin/ldconfig

%postun iostreams -p /sbin/ldconfig

%post locale -p /sbin/ldconfig

%postun locale -p /sbin/ldconfig

%post log -p /sbin/ldconfig

%postun log -p /sbin/ldconfig

%post math -p /sbin/ldconfig

%postun math -p /sbin/ldconfig

%post program-options -p /sbin/ldconfig

%postun program-options -p /sbin/ldconfig

%post random -p /sbin/ldconfig

%postun random -p /sbin/ldconfig

%post regex -p /sbin/ldconfig

%postun regex -p /sbin/ldconfig

%post serialization -p /sbin/ldconfig

%postun serialization -p /sbin/ldconfig

%post signals -p /sbin/ldconfig

%postun signals -p /sbin/ldconfig

%post stacktrace -p /sbin/ldconfig

%postun stacktrace -p /sbin/ldconfig

%post system -p /sbin/ldconfig

%postun system -p /sbin/ldconfig

%post test -p /sbin/ldconfig

%postun test -p /sbin/ldconfig

%post thread -p /sbin/ldconfig

%postun thread -p /sbin/ldconfig

%post timer -p /sbin/ldconfig

%postun timer -p /sbin/ldconfig

%post type_erasure -p /sbin/ldconfig

%postun type_erasure -p /sbin/ldconfig

%post wave -p /sbin/ldconfig

%postun wave -p /sbin/ldconfig

%files atomic
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_atomic*.so.*

%files chrono
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_chrono*.so.*

%files container
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_container*.so.*

%files date-time
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_date_time*.so.*

%files exception
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_exception*.so.*

%files filesystem
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_filesystem*.so.*

%files graph
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_graph.so.*
%{_libdir}/libboost_graph-mt.so.*

%files iostreams
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_iostreams*.so.*

%files locale
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_locale*.so.*

%files log
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_log*.so.*

%files math
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_math*.so.*

%files test
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_prg_exec_monitor*.so.*
%{_libdir}/libboost_test_exec_monitor*.so.*
%{_libdir}/libboost_unit_test_framework*.so.*

%files program-options
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_program_options*.so.*

%files random
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_random*.so.*

%files regex
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_regex*.so.*

%files serialization
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_serialization*.so.*
%{_libdir}/libboost_wserialization*.so.*

%files signals
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_signals*.so.*

%files stacktrace
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_stacktrace_addr2line*.so.*
%{_libdir}/libboost_stacktrace_basic*.so.*
%{_libdir}/libboost_stacktrace_noop*.so.*

%files system
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_system*.so.*

%files thread
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_thread*.so.*

%files timer
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_timer*.so.*

%files type_erasure
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_type_erasure*.so.*

%files wave
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_wave*.so.*

%files devel
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/libboost_*.so
%defattr(0644, root, root, 0755) 
%{_includedir}/%{name}

%files static
%defattr(-, root, root, -)
%license LICENSE_1_0.txt
%{_libdir}/*.a

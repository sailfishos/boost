# All arches have mpich
%bcond_without mpich

%ifnarch %{ix86} x86_64
  %bcond_with quadmath
%else
  %bcond_without quadmath
%endif

%ifnarch x86_64
  %bcond_with stacktrace_from_exception
%else
  %bcond_without stacktrace_from_exception
%endif

Name: boost
Summary: The free peer-reviewed portable C++ source libraries
# Update libboost_thread.so on each version change
Version: 1.91.0
Release: 1
License: Boost and MIT and Python

URL: https://github.com/sailfishos/boost
Source0: %{name}-%{version}.tar.bz2

# Patches from opensuse
Patch1: boost-thread.patch
Patch2: boost-no_type_punning.patch
Patch4: boost-pool_check_overflow.patch
Patch5: boost-strict_aliasing.patch
Patch6: boost-use_std_xml_catalog.patch
Patch7: boost-aarch64-flags.patch
Patch8: dynamic_linking.patch
Patch9: boost-no-exception.patch

# boost-remove-cmakedir.patch, boost-rpmoptflags-only.patch - included in Fedora patches

# Patches from fedora

# https://bugzilla.redhat.com/show_bug.cgi?id=1541035
Patch101: boost-1.81.0-build-optflags.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1318383
Patch102: boost-1.90.0-no-rpath.patch

# https://lists.boost.org/Archives/boost/2020/04/248812.php
Patch103: boost-1.73.0-cmakedir.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1541035
Patch104: boost-1.78.0-b2-build-flags.patch

# PR https://github.com/boostorg/interval/pull/30
# Fixes narrowing conversions for ppc -
#   https://github.com/boostorg/interval/issues/29
Patch105: boost-1.76.0-fix-narrowing-conversions-for-ppc.patch

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

Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0

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

%package charconv
Summary: Run-time component of boost charconv library
License: BSL-1.0 AND (BSL-1.0 OR Apache-2.0 WITH LLVM-exception)

%description charconv

Run-time support for Boost.Charconv, an implementation of <charconv>
in C++11.

%package chrono
Summary: Run-Time component of boost chrono library
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0

%description chrono

Run-Time support for Boost.Chrono, a set of useful time utilities.

%package container
Summary: Run-Time component of boost container library

%description container

Boost.Container library implements several well-known containers,
including STL containers. The aim of the library is to offers advanced
features not present in standard containers or to offer the latest
standard draft features for compilers that don't comply with the
latest C++ standard.

%package contract
Summary: Run-time component of boost contract library

%description contract

Run-time support for boost contract library.
Contract programming for C++. All contract programming features are supported:
Subcontracting, class invariants, postconditions (with old and return values),
preconditions, customizable actions on assertion failure (e.g., terminate
or throw), optional compilation and checking of assertions, etc,
from Lorenzo Caminiti.

%package context
Summary: Run-time component of boost context switching library

%description context

Run-time support for Boost.Context, a foundational library that
provides a sort of cooperative multitasking on a single thread.

%package coroutine
Summary: Run-time component of boost coroutine library
Requires: boost-context = %{version}-%{release}

%description coroutine
Run-time support for Boost.Coroutine, a library that provides
generalized subroutines which allow multiple entry points for
suspending and resuming execution.

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
Requires: boost-atomic = %{version}-%{release}
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0

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

%package json
Summary: Run-time component of boost json library
Requires: boost-container = %{version}-%{release}

%description json

Run-time support for Boost.Json, a portable C++ library which provides
containers and algorithms that implement JavaScript Object Notation, or
simply "JSON"

%package locale
Summary: Run-Time component of boost locale library
Requires: boost-chrono = %{version}-%{release}
Requires: boost-thread = %{version}-%{release}
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0

%description locale

Run-Time support for Boost.Locale, a set of localization and Unicode
handling tools.

%package log
Summary: Run-Time component of boost logging library
Requires: boost-atomic = %{version}-%{release}
Requires: boost-chrono = %{version}-%{release}
Requires: boost-filesystem = %{version}-%{release}
Requires: boost-regex = %{version}-%{release}
Requires: boost-thread = %{version}-%{release}

%description log

Boost.Log library aims to make logging significantly easier for the
application developer.  It provides a wide range of out-of-the-box
tools along with public interfaces for extending the library.


%package math
Summary: Run-time component of boost math toolkit
%if %{with quadmath}
Requires: libquadmath
%endif

%description math

Run-time support for Boost.Math, including floating-point utilities,
specific width floating-point types, mathematical constants,
statistical distributions, special functions, and more.

%package nowide
Summary: Standard library functions with UTF-8 API on Windows

%description nowide

Run-time support for Boost.Nowide.

%package process
Summary:  Run-time component of boost process library

%description process

Run-time support of the Boost.Process library, for managing system
processes.

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

%package stacktrace
Summary: Run-time component of boost stacktrace library

%description stacktrace

Run-time component of the Boost stacktrace library.

%package test
Summary: Run-Time component of boost test library

%description test

Run-Time support for simple program testing, full unit testing, and for
program execution monitoring.

%package thread
Summary: Run-Time component of boost thread library
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0

%description thread

Run-Time component Boost.Thread library, which provides classes and
functions for managing multiple threads of execution, and for
synchronizing data between the threads or providing separate copies of
data specific to individual threads.

%package timer
Summary: Run-Time component of boost timer library
Requires: boost-chrono = %{version}-%{release}
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0

%description timer

"How long does my C++ code take to run?"
The Boost Timer library answers that question and does so portably,
with as little as one #include and one additional line of code.

%package type_erasure
Summary: Run-Time component of boost type erasure library
Requires: boost-chrono = %{version}-%{release}
Requires: boost-thread = %{version}-%{release}
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0

%description type_erasure

The Boost.TypeErasure library provides runtime polymorphism in C++
that is more flexible than that provided by the core language.

%package url
Summary: Run-Time component of boost URL library

%description url

Run-Time component of the boost URL library.

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
Requires: boost-charconv = %{version}-%{release}
Requires: boost-chrono = %{version}-%{release}
Requires: boost-container = %{version}-%{release}
Requires: boost-contract = %{version}-%{release}
Requires: boost-context = %{version}-%{release}
Requires: boost-coroutine = %{version}-%{release}
Requires: boost-date-time = %{version}-%{release}
Requires: boost-exception = %{version}-%{release}
Requires: boost-filesystem = %{version}-%{release}
Requires: boost-graph = %{version}-%{release}
Requires: boost-iostreams = %{version}-%{release}
Requires: boost-json = %{version}-%{release}
Requires: boost-locale = %{version}-%{release}
Requires: boost-log = %{version}-%{release}
Requires: boost-math = %{version}-%{release}
Requires: boost-nowide = %{version}-%{release}
Requires: boost-process = %{version}-%{release}
%if %{with quadmath}
Requires: libquadmath-devel
%endif
Requires: boost-program-options = %{version}-%{release}
Requires: boost-random = %{version}-%{release}
Requires: boost-regex = %{version}-%{release}
Requires: boost-serialization = %{version}-%{release}
Requires: boost-stacktrace = %{version}-%{release}
Requires: boost-test = %{version}-%{release}
Requires: boost-thread = %{version}-%{release}
Requires: boost-timer = %{version}-%{release}
Requires: boost-type_erasure = %{version}-%{release}
Requires: boost-url = %{version}-%{release}
Requires: boost-wave = %{version}-%{release}
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0

%description devel
Headers and shared object symbolic links for the Boost C++ libraries.

%package static
Summary: The Boost C++ static development libraries
Requires: boost-devel = %{version}-%{release}
Provides: boost-devel-static = %{version}-%{release}

%description static
Static Boost C++ libraries.

%package b2
Summary: A low-level build tool

%description b2
B2 (formerly Boost.Jam) is the low-level build engine tool for Boost.Build.
Historically, B2 was based on on FTJam and on Perforce Jam but has grown
a number of significant features and is now developed independently.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
./bootstrap.sh --with-toolset=gcc --with-icu --without-libraries=python  --prefix=$RPM_BUILD_ROOT%{_prefix}

./b2 headers

# N.B. When we build the following with PCH, parts of boost (math
# library in particular) end up being built second time during
# installation.  Unsure why that is, but all sub-builds need to be
# built with pch=off to avoid this.

echo ============================= build serial ==================
./b2 -d+2 -q %{?_smp_mflags} --without-python \
	--without-mpi --without-graph_parallel --build-dir=serial \
	--without-fiber \
	--without-cobalt \
	variant=release threading=multi debug-symbols=on pch=off \
%if !%{with stacktrace_from_exception}
	boost.stacktrace.from_exception=off \
%endif
	stage

echo ============================= build Boost.Build ==================
(cd tools/build
 ./bootstrap.sh --with-toolset=gcc  --prefix=$RPM_BUILD_ROOT%{_prefix})


%install
rm -rf $RPM_BUILD_ROOT

echo ============================= install serial ==================
./b2 -d+2 -q %{?_smp_mflags} --without-python \
	--without-mpi --without-graph_parallel --build-dir=serial \
	--without-fiber \
	--prefix=$RPM_BUILD_ROOT%{_prefix} \
	--libdir=$RPM_BUILD_ROOT%{_libdir} \
	variant=release threading=multi debug-symbols=on pch=off \
%if !%{with stacktrace_from_exception}
	boost.stacktrace.from_exception=off \
%endif
	install

cat > $RPM_BUILD_ROOT%{_libdir}/libboost_system.so << EOT
/* GNU ld script

There is no runtime library for Boost.System.
This empty linker script exists to support Fedora packages which use
-lboost_system when linking and so require a library with that name.

This linker script will be remove in a future Fedora release.
*/
EOT
chmod 644 $RPM_BUILD_ROOT%{_libdir}/libboost_system.so

%fdupes %{buildroot}/
%fdupes %{buildroot}/%{_libdir}/
%fdupes %{buildroot}/%{_datadir}/


# MPI subpackages don't need the ldconfig magic.  They are hidden by
# default, in MPI back-end-specific directory, and only show to the
# user after the relevant environment module has been loaded.
# rpmlint will report that as errors, but it is fine.

%post atomic -p /sbin/ldconfig

%postun atomic -p /sbin/ldconfig

%post charconv -p /sbin/ldconfig

%postun charconv -p /sbin/ldconfig

%post chrono -p /sbin/ldconfig

%postun chrono -p /sbin/ldconfig

%post container -p /sbin/ldconfig

%postun container -p /sbin/ldconfig

%post contract -p /sbin/ldconfig

%postun contract -p /sbin/ldconfig

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

%post json -p /sbin/ldconfig

%postun json -p /sbin/ldconfig

%post locale -p /sbin/ldconfig

%postun locale -p /sbin/ldconfig

%post log -p /sbin/ldconfig

%postun log -p /sbin/ldconfig

%post math -p /sbin/ldconfig

%postun math -p /sbin/ldconfig

%post nowide -p /sbin/ldconfig

%postun nowide -p /sbin/ldconfig

%post process -p /sbin/ldconfig

%postun process -p /sbin/ldconfig

%post program-options -p /sbin/ldconfig

%postun program-options -p /sbin/ldconfig

%post random -p /sbin/ldconfig

%postun random -p /sbin/ldconfig

%post regex -p /sbin/ldconfig

%postun regex -p /sbin/ldconfig

%post serialization -p /sbin/ldconfig

%postun serialization -p /sbin/ldconfig

%post stacktrace -p /sbin/ldconfig

%postun stacktrace -p /sbin/ldconfig

%post test -p /sbin/ldconfig

%postun test -p /sbin/ldconfig

%post thread -p /sbin/ldconfig

%postun thread -p /sbin/ldconfig

%post timer -p /sbin/ldconfig

%postun timer -p /sbin/ldconfig

%post type_erasure -p /sbin/ldconfig

%postun type_erasure -p /sbin/ldconfig

%post url -p /sbin/ldconfig

%postun url -p /sbin/ldconfig

%post wave -p /sbin/ldconfig

%postun wave -p /sbin/ldconfig

%files atomic
%license LICENSE_1_0.txt
%{_libdir}/libboost_atomic*.so.*

%files charconv
%license LICENSE_1_0.txt
%{_libdir}/libboost_charconv.so.*

%files chrono
%license LICENSE_1_0.txt
%{_libdir}/libboost_chrono*.so.*

%files container
%license LICENSE_1_0.txt
%{_libdir}/libboost_container*.so.*

%files contract
%license LICENSE_1_0.txt
%{_libdir}/libboost_contract*.so.*

%files context
%license LICENSE_1_0.txt
%{_libdir}/libboost_context.so.*

%files coroutine
%license LICENSE_1_0.txt
%{_libdir}/libboost_coroutine.so.*

%files date-time
%license LICENSE_1_0.txt
%{_libdir}/libboost_date_time*.so.*

%files exception
%license LICENSE_1_0.txt
%{_libdir}/libboost_exception*.so.*

%files filesystem
%license LICENSE_1_0.txt
%{_libdir}/libboost_filesystem*.so.*

%files graph
%license LICENSE_1_0.txt
%{_libdir}/libboost_graph*.so.*

%files iostreams
%license LICENSE_1_0.txt
%{_libdir}/libboost_iostreams*.so.*

%files json
%license LICENSE_1_0.txt
%{_libdir}/libboost_json*.so.*

%files locale
%license LICENSE_1_0.txt
%{_libdir}/libboost_locale*.so.*

%files log
%license LICENSE_1_0.txt
%{_libdir}/libboost_log*.so.*

%files math
%license LICENSE_1_0.txt
%{_libdir}/libboost_math*.so.*

%files nowide
%license LICENSE_1_0.txt
%{_libdir}/libboost_nowide*.so.*

%files process
%license LICENSE_1_0.txt
%{_libdir}/libboost_process.so.*

%files test
%license LICENSE_1_0.txt
%{_libdir}/libboost_prg_exec_monitor*.so.*
%{_libdir}/libboost_test_exec_monitor*.so.*
%{_libdir}/libboost_unit_test_framework*.so.*

%files program-options
%license LICENSE_1_0.txt
%{_libdir}/libboost_program_options*.so.*

%files random
%license LICENSE_1_0.txt
%{_libdir}/libboost_random*.so.*

%files regex
%license LICENSE_1_0.txt
%{_libdir}/libboost_regex*.so.*

%files serialization
%license LICENSE_1_0.txt
%{_libdir}/libboost_serialization*.so.*
%{_libdir}/libboost_wserialization*.so.*

%files stacktrace
%license LICENSE_1_0.txt
%{_libdir}/libboost_stacktrace_addr2line*.so.*
%{_libdir}/libboost_stacktrace_basic*.so.*
%{_libdir}/libboost_stacktrace_noop*.so.*
%if %{with stacktrace_from_exception}
%{_libdir}/libboost_stacktrace_from_exception.so.*
%endif

%files thread
%license LICENSE_1_0.txt
%{_libdir}/libboost_thread*.so.*

%files timer
%license LICENSE_1_0.txt
%{_libdir}/libboost_timer*.so.*

%files type_erasure
%license LICENSE_1_0.txt
%{_libdir}/libboost_type_erasure*.so.*

%files url
%license LICENSE_1_0.txt
%{_libdir}/libboost_url*.so.*

%files wave
%license LICENSE_1_0.txt
%{_libdir}/libboost_wave*.so.*

%files devel
%license LICENSE_1_0.txt
%{_libdir}/libboost_*.so
%defattr(0644, root, root, 0755) 
%{_includedir}/%{name}
%{_libdir}/cmake

%files static
%license LICENSE_1_0.txt
%{_libdir}/*.a

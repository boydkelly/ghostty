# -*- mode: spec; package-name: ghostty; version: 0; -*-

# Ghostty - A fast, GPU-accelerated terminal emulator
# Fedora spec file for tip (development) build
#
# This spec intentionally keeps dependencies minimal while following
# the version conventions and changelog macros used by the official
# ghostty.spec.rpkg.

Name:           ghostty
Version:        0.0.0            # “tip” version
Release:        1%{?dist}
Summary:        Fast terminal emulator using modern graphics APIs
License:        BSD-2-Clause
URL:            https://github.com/ghostty-org/ghostty
Source0:        https://github.com/ghostty-org/ghostty/releases/download/tip/ghostty-source.tar.gz

# Minimal set of build dependencies for a tip build
BuildRequires:  gtk4-devel
BuildRequires:  gtk4-layer-shell-devel
BuildRequires:  libadwaita-devel
BuildRequires:  gettext
BuildRequires:  zig

# The %global definitions align with rpmmacros used by the upstream
%global _product_license BSD-2-Clause
%global _product_url %{url}
%global _product_source0 %{Source0}

%description
Ghostty is a fast, cross‑platform terminal emulator that leverages
GPU‑accelerated graphics through GTK4 and libadwaita.  This spec builds
the latest development tip from the official GitHub releases.

%prep
%autosetup -n ghostty-source-%{version}

%build
# Build using zig with ReleaseFast optimisation and installation prefix /usr
%zig_build -p %{_prefix} -Doptimize=ReleaseFast

%install
# Install the built binary and documentation files
mkdir -p %{buildroot}%{_bindir}
install ghostty%{_bindir}/ghostty

# Install README and other documentation files
%doc README.md

%changelog
* %b %d %Y Maintainer <you@example.com> - Version 0.0.0-1
- New custom spec for tip build with minimal dependencies.
- Uses %{Source0} as upstream source.
- Follows rpmmacros version conventions.

%global _debuginfo_package %{nil}
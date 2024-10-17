Name:		texlive-penrose
Version:	57508
Release:	2
Summary:	A TikZ library for producing Penrose tilings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/penrose
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/penrose.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/penrose.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/penrose.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a TikZ library for drawing Penrose tiles.
It currently supports the kite/dart, rhombus, and pentagon tile
sets. There are two main methods for their placement: one that
automatically generates a tiling, and one that allows for "by
hand" placement. Furthermore, the tiles themselves can be
deformed and will still (hopefully!) fit together in the
correct fashion.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/penrose
%{_texmfdistdir}/tex/latex/penrose
%doc %{_texmfdistdir}/doc/latex/penrose

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

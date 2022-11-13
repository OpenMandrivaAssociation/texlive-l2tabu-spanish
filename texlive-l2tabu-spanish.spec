Name:		texlive-l2tabu-spanish
Version:	15878
Release:	1
Summary:	Spanish translation of "Obsolete packages and commands"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2tabu/spanish
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-spanish.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-spanish.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A Spanish translation of the l2tabu practical guide to LaTeX2e
by Mark Trettin. A list of obsolete packages, commands and
usages.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/l2tabu-spanish/README
%doc %{_texmfdistdir}/doc/latex/l2tabu-spanish/l2tabues.pdf
%doc %{_texmfdistdir}/doc/latex/l2tabu-spanish/l2tabues.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}

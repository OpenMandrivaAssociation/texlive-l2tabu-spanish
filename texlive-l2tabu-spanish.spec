Name:		texlive-l2tabu-spanish
Version:	1.1
Release:	1
Summary:	Spanish translation of "Obsolete packages and commands"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2tabu/spanish
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-spanish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-spanish.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}

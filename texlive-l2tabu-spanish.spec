# revision 15878
# category Package
# catalog-ctan /info/l2tabu/spanish
# catalog-date 2008-08-22 10:50:40 +0200
# catalog-license pd
# catalog-version 1.1
Name:		texlive-l2tabu-spanish
Version:	1.1
Release:	6
Summary:	Spanish translation of "Obsolete packages and commands"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2tabu/spanish
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-spanish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-spanish.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 753067
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718795
- texlive-l2tabu-spanish
- texlive-l2tabu-spanish
- texlive-l2tabu-spanish
- texlive-l2tabu-spanish


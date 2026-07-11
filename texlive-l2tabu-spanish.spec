%global tl_name l2tabu-spanish
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Spanish translation of Obsolete packages and commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/l2tabu/spanish
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-spanish.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-spanish.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A Spanish translation of the l2tabu practical guide to LaTeX2e by Mark
Trettin. A list of obsolete packages, commands and usages.


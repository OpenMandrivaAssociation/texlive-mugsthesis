%global tl_name mugsthesis
%global tl_revision 75301

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Thesis class complying with Marquette University Graduate School requirements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mugsthesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mugsthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mugsthesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mugsthesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle offers a thesis class, based on memoir, that complies with
Marquette University Graduate School requirements.


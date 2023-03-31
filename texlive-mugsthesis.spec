Name:		texlive-mugsthesis
Version:	64259
Release:	2
Summary:	Thesis class complying with Marquette University Graduate School requirements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mugsthesis
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mugsthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mugsthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mugsthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle offers a thesis class, based on memoir, that
complies with Marquette University Graduate School
requirements.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mugsthesis
%{_texmfdistdir}/tex/latex/mugsthesis
%doc %{_texmfdistdir}/doc/latex/mugsthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

%global tl_name first-latex-doc
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A document for absolute LaTeX beginners
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/first-latex-doc
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/first-latex-doc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/first-latex-doc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The document leads a reader, who knows nothing about LaTeX, through the
production of a two page document. The user who has completed that first
document, and wants to carry on, will find recommendations for
tutorials.


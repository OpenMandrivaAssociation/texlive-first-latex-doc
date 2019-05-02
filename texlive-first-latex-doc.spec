Name:		texlive-first-latex-doc
Version:	20190228
Release:	1
Summary:	A document for absolute LaTeX beginners
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/first-latex-doc
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/first-latex-doc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/first-latex-doc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The document leads a reader, who knows nothing about LaTeX,
through the production of a two page document. The user who has
completed that first document, and wants to carry on, will find
recommendations for tutorials.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/first-latex-doc

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}

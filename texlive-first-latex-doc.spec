# revision 15878
# category Package
# catalog-ctan /info/first-latex-doc
# catalog-date 2009-11-09 22:22:13 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-first-latex-doc
Version:	20091109
Release:	2
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
%doc %{_texmfdistdir}/doc/latex/first-latex-doc/README
%doc %{_texmfdistdir}/doc/latex/first-latex-doc/first-latex-doc.pdf
%doc %{_texmfdistdir}/doc/latex/first-latex-doc/first-latex-doc.tex
%doc %{_texmfdistdir}/doc/latex/first-latex-doc/latex-first.png
%doc %{_texmfdistdir}/doc/latex/first-latex-doc/latex-first.tex
%doc %{_texmfdistdir}/doc/latex/first-latex-doc/latex-second-a.png
%doc %{_texmfdistdir}/doc/latex/first-latex-doc/latex-second-a.tex
%doc %{_texmfdistdir}/doc/latex/first-latex-doc/latex-second-b.png
%doc %{_texmfdistdir}/doc/latex/first-latex-doc/latex-second-b.tex
%doc %{_texmfdistdir}/doc/latex/first-latex-doc/latex-second-c.png
%doc %{_texmfdistdir}/doc/latex/first-latex-doc/latex-second-c.tex
%doc %{_texmfdistdir}/doc/latex/first-latex-doc/latex-second-d.tex
%doc %{_texmfdistdir}/doc/latex/first-latex-doc/latex-second-e.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}

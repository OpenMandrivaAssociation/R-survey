%global packname  survey
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          3.29.5
Release:          1
Summary:          analysis of complex survey samples
Group:            Sciences/Mathematics
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/survey_3.29-5.tar.gz
Requires:         R-foreign R-survival R-MASS R-splines R-KernSmooth
Requires:         R-hexbin R-mitools R-lattice R-RSQLite R-RODBC R-quantreg
Requires:         R-Matrix R-multicore R-CompQuadForm
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-foreign R-survival R-MASS R-splines R-KernSmooth
BuildRequires:    R-hexbin R-mitools R-lattice R-RSQLite R-RODBC R-quantreg
BuildRequires:    R-Matrix R-multicore R-CompQuadForm

%description
Summary statistics, two-sample tests, generalised linear models,
cumulative link models, Cox models, loglinear models, and general maximum
pseudolikelihood estimation for multistage stratified, cluster-sampled,
unequally weighted survey samples. Variances by Taylor series
linearisation or replicate weights. Post-stratification, calibration, and
raking. Two-phase subsampling designs. Graphics. Predictive margins by
direct standardization. PPS sampling without replacement. Principal
components, factor analysis.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/disclaimer
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/porting*
%doc %{rlibdir}/%{packname}/*.pdf
%doc %{rlibdir}/%{packname}/BUGS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/COPYING
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/api.db
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help

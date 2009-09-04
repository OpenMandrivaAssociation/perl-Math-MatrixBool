%define module	Math-MatrixBool
%define name	perl-%{module}
%define version 5.7
%define release %mkrel 9

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Matrix of Booleans
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp.perl.org/pub/CPAN/modules/by-module/Math/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Bit::Vector)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Easy manipulation of matrices of booleans (Boolean Algebra).

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README.txt
%{perl_vendorlib}/Math
%{_mandir}/*/*


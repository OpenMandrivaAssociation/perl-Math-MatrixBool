%define upstream_name	 Math-MatrixBool
%define upstream_version 5.8

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Matrix of Booleans
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp.perl.org/pub/CPAN/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Bit::Vector)

BuildArch:	noarch

%description
Easy manipulation of matrices of booleans (Boolean Algebra).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README.txt
%{perl_vendorlib}/Math
%{_mandir}/*/*


%changelog
* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 5.800.0-1mdv2010.1
+ Revision: 461328
- update to 5.8

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 5.7-9mdv2010.0
+ Revision: 430500
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 5.7-8mdv2009.0
+ Revision: 241724
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.7-6mdv2008.0
+ Revision: 86613
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 5.7-5mdv2007.0
- Rebuild

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 5.7-4mdk
- Fix According to perl Policy
	- Source URL
	- BuildRequires

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 5.7-3mdk
- spec cleanup
- %%mkrel
- better URL

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 5.7-2mdk
- fix buildrequires in a backward compatible way

* Tue Sep 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 5.7-1mdk 
- first mdk release


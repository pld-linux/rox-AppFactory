%define _name AppFactory
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	ROX-AppFactory automates the creation of ROX wrappers
Summary(pl):	ROX-AppFactory automatyzuje proces tworzenia wrapperów ROXa
Name:		rox-%{_name}
Version:	1.0.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tgz
Patch0:		%{name}-libxml-includes.patch
Patch1:		%{name}-paths-fix.patch
URL:		http://www.kerofin.demon.co.uk/rox/utils.html#appfactory
BuildRequires:	gtk+-devel
BuildRequires:	libxml2-devel
BuildRequires:	rox-CLib-devel >= 0.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_appsdir	%{_libdir}/ROX-apps

%description
ROX-AppFactory is a program for automating the creation of ROX
wrappers for programs.

%description -l pl
ROX-AppFactory jest programem automatyzuj±cym proces tworzenia
wrapperów ROXa.

%prep
%setup -q -n %{_name}
%patch0 -p1
%patch1 -p1

%build
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,%{_platform},Resources} \
  $RPM_BUILD_ROOT%{_appsdir}/%{_name}/pixmaps


rm -f ../install
install App* rox_run $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install %{_platform}/AppFactory $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}
install pixmaps/*xpm $RPM_BUILD_ROOT%{_appsdir}/%{_name}/pixmaps
install Resources/*.{dtd,xpm,py} $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Resources

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/Versions
%attr(755,root,root) %{_appsdir}/%{_name}/*[Rr]un
%attr(755,root,root) %{_appsdir}/%{_name}/Resources/*.py
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/pixmaps
%{_appsdir}/%{_name}/Help
%{_appsdir}/%{_name}/Resources/*dtd
%{_appsdir}/%{_name}/Resources/*.xpm
%dir %{_appsdir}/%{_name}
%dir %{_appsdir}/%{_name}/Resources

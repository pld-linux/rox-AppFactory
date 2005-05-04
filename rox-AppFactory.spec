%define _name AppFactory
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	ROX-AppFactory automates the creation of ROX wrappers
Summary(pl):	ROX-AppFactory automatyzuje proces tworzenia wrapperów ROXa
Name:		rox-%{_name}
Version:	2.1.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tar.gz
# Source0-md5:	d2d343ac40e4dd184a09995c3778f644
#Patch0:	%{name}-paths-fix.patch
Patch1:		%{name}-ROX-apps-paths.patch
Patch2:		%{name}-ROX-CLib2-includes.patch
Patch3:		%{name}-aclocal.patch
URL:		http://www.kerofin.demon.co.uk/rox/appfactory.html
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	rox-CLib2-devel >= 2.1.4
Requires:	rox >= 2.2.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
ROX-AppFactory is a program for automating the creation of ROX
wrappers for programs.

%description -l pl
ROX-AppFactory jest programem automatyzuj±cym proces tworzenia
wrapperów ROXa.

%prep
%setup -q -n %{_name}
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cd src
%{__autoconf}
cd ..
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,%{_platform},Resources} \
	$RPM_BUILD_ROOT%{_appsdir}/%{_name}/pixmaps

install .DirIcon AppRun *.xml rox_run $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install %{_platform}/AppFactory $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}
install pixmaps/*.xpm $RPM_BUILD_ROOT%{_appsdir}/%{_name}/pixmaps
install Resources/*.{dtd,png,xpm,py} $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Resources

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/{Changes,Versions}
%attr(755,root,root) %{_appsdir}/%{_name}/*[Rr]un
%attr(755,root,root) %{_appsdir}/%{_name}/Resources/*.py
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%{_appsdir}/%{_name}/.DirIcon
%{_appsdir}/%{_name}/*.xml
%{_appsdir}/%{_name}/pixmaps
%{_appsdir}/%{_name}/Help
%{_appsdir}/%{_name}/Resources/*.dtd
%{_appsdir}/%{_name}/Resources/*.png
%{_appsdir}/%{_name}/Resources/*.xpm
%dir %{_appsdir}/%{_name}
%dir %{_appsdir}/%{_name}/Resources

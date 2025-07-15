%define _name AppFactory
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	ROX-AppFactory automates the creation of ROX wrappers
Summary(pl.UTF-8):	ROX-AppFactory automatyzuje proces tworzenia wrapperów ROXa
Name:		rox-%{_name}
Version:	2.1.3
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tar.gz
# Source0-md5:	d2d343ac40e4dd184a09995c3778f644
Source1:	%{name}.desktop
#Patch0:	%{name}-paths-fix.patch
Patch1:		%{name}-ROX-apps-paths.patch
Patch2:		%{name}-ROX-CLib2-includes.patch
Patch3:		%{name}-aclocal.patch
URL:		http://www.kerofin.demon.co.uk/rox/appfactory.html
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	rox-CLib2-devel >= 2.1.5-2
Requires:	rox >= 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_roxdir	%{_libdir}/rox

%description
ROX-AppFactory is a program for automating the creation of ROX
wrappers for programs.

%description -l pl.UTF-8
ROX-AppFactory jest programem automatyzującym proces tworzenia
wrapperów ROXa.

%prep
%setup -q -n %{_name}
#%patch0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
cd src
%{__autoconf}
cd ..
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_roxdir}/%{_name}/{Help,%{_platform},pixmaps,Resources} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install .DirIcon AppRun *.xml rox_run $RPM_BUILD_ROOT%{_roxdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Help
install %{_platform}/AppFactory $RPM_BUILD_ROOT%{_roxdir}/%{_name}/%{_platform}
install pixmaps/*.xpm $RPM_BUILD_ROOT%{_roxdir}/%{_name}/pixmaps
install Resources/*.{dtd,png,xpm,py} $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Resources
install .DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

sed -e "s,/lib/,/%{_lib}/," %{SOURCE1} > $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/{Changes,Versions}
%attr(755,root,root) %{_roxdir}/%{_name}/*[Rr]un
%attr(755,root,root) %{_roxdir}/%{_name}/Resources/*.py
%attr(755,root,root) %{_roxdir}/%{_name}/%{_platform}
%{_roxdir}/%{_name}/.DirIcon
%{_roxdir}/%{_name}/*.xml
%{_roxdir}/%{_name}/pixmaps
%{_roxdir}/%{_name}/Help
%{_roxdir}/%{_name}/Resources/*.dtd
%{_roxdir}/%{_name}/Resources/*.png
%{_roxdir}/%{_name}/Resources/*.xpm
%dir %{_roxdir}/%{_name}
%dir %{_roxdir}/%{_name}/Resources
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

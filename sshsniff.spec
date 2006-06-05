Summary:	sshsniff
Name:		sshsniff
Version:	0.1
Release:	0.1
License:	?
Group:		Development/Debuggers
Source0:	http://blackdevil.iwarp.com/sshsniff.tar.gz
# Source0-md5:	8d438a04e5a3e9b94f80f319921e158c
ExclusiveArch:	%{ix86} arm m68k
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sshsniff is a systemcall traffic logger. It allows the logging of any
in- and outgoing traffic from a given pid and it's childs.  that also
allows the sniffing of an ssh client and/or server of a possibly
compromised host. You can also use it for other processes which use
the SYS_read and SYS_write syscalls.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README

Summary:	sshsniff - systemcall traffic logger
Summary(pl.UTF-8):   sshsniff - program do logowania danych przechodzących przez wywołania systemowe
Name:		sshsniff
Version:	0.1
Release:	0.1
License:	?
Group:		Development/Debuggers
# Source0Download: http://blackdevil.iwarp.com/sshsniff.tar.gz
Source0:	%{name}.tar.gz
# Source0-md5:	8d438a04e5a3e9b94f80f319921e158c
Patch0:		%{name}-config.patch
ExclusiveArch:	%{ix86} arm m68k
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sshsniff is a systemcall traffic logger. It allows the logging of any
in- and outgoing traffic from a given pid and it's childs. That also
allows the sniffing of an SSH client and/or server of a possibly
compromised host. You can also use it for other processes which use
the SYS_read and SYS_write syscalls.

%description -l pl.UTF-8
sshsniff to program do logowania danych przechodzących przez wywołania
systemowe. Pozwala logować dowolny ruch przychodzący i wychodzący
procesu o podanym pidzie i jego potomków. Umożliwia także śledzenie
klienta lub serwera SSH prawdopodobnie przejętego hosta. Można go
używać także dla innych procesów używających wywołań systemowych
SYS_read i SYS_write.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir}}
install %{name} $RPM_BUILD_ROOT%{_sbindir}
install %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sshsniff.conf
%attr(755,root,root) %{_sbindir}/sshsniff

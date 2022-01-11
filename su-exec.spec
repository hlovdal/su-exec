Name:           su-exec
Version:        0.4
Release:        1%{?dist}
Summary:        Switch user and group id, setgroups and exec
License:        MIT
URL:            https://github.com/frebib/su-exec

# curl -L https://github.com/frebib/su-exec/archive/v0.4.tar.gz -o su-exec-0.4.tar.gz
# Source0:        su-exec-0.4.tar.gz
Source0:        https://github.com/frebib/su-exec/archive/v%{version}.tar.gz

%description
This is a simple tool that will simply execute a program with different
privileges. The program will be exceuted directly and not run as a child,
like su and sudo does, which avoids TTY and signal issues (see below).

Notice that su-exec depends on being run by the root user, non-root
users do not have permission to change uid/gid.

%prep
tar zxvf %{SOURCE0}
mv su-exec-%{version}/* .

%build
make

%install
rm -rf $RPM_BUILD_ROOT
strip su-exec
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_mandir}/man8/su-exec.1.gz
%{_bindir}/su-exec

%changelog
* Tue Jan 11 2022 Håkon Løvdal <kode@denkule.no> - 0.4-1
- Created spec file.

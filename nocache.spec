Summary:	Minimize filesystem caching effects
Summary(pl.UTF-8):	Minimalizowanie efektów buforowania systemu plików
Name:		nocache
Version:	1.1
Release:	1
License:	BSD
Group:		Base
#Source0Download: https://github.com/Feh/nocache/releases
Source0:	https://github.com/Feh/nocache/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a9d37fb73036a02b0e910985dd9ed643
URL:		https://github.com/Feh/nocache
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The nocache tool tries to minimize the effect an application has on
the Linux file system cache. This is done by intercepting the open and
close system calls and calling posix_fadvise with the
POSIX_FADV_DONTNEED parameter. Because the library remembers which
pages (ie., 4K-blocks of the file) were already in file system cache
when the file was opened, these will not be marked as "don't need",
because other applications might need that, although they are not
actively used (think: hot standby).

Use case: backup processes that should not interfere with the present
state of the cache.

%description -l pl.UTF-8
Narzędzie nocache próbuje zminimalizować wpływ buforowania systemu
plików w pamięci podręcznej na aplikację. Dokonuje tego poprzez
przechwycenie wywołań systemowych open i close i wywoływanie funkcji
posix_fadvise z parametrem POSIX_FADV_DONTNEED. Ponieważ biblioteka
zapamiętuje, które strony (tj. 4kB bloki pliku) były już w pamięci
podręcznej systemu plików przy otwieraniu pliku, te strony nie są
oznaczane jako niepotrzebne, ponieważ inne aplikacje mogą ich
potrzebować, mimo że nie są aktualnie używane.

Przypadek użycia: procesy kopii zapasowych, które nie powinny wpływać
na bieżący stan pamięci podręcznej.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS+="%{rpmcppflags} %{rpmcflags}" \
	LDFLAGS+="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX= \
	LIBDIR=%{_libdir} \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/cachedel
%attr(755,root,root) %{_bindir}/cachestats
%attr(755,root,root) %{_bindir}/nocache
%attr(755,root,root) %{_libdir}/nocache.so
%{_mandir}/man1/cachedel.1*
%{_mandir}/man1/cachestats.1*
%{_mandir}/man1/nocache.1*

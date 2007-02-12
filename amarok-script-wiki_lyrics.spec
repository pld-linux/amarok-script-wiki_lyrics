# NOTE
# - could use QtRuby, Ruby/GTK or Ruby/Tk, but as only -tk was available on AC,
#   used that dependency.
%define		scriptname	wiki_lyrics
Summary:	A collection of lyrics scripts for amaroK
Summary(pl.UTF-8):	Zestaw skryptów do tekstów utworów dla amaroKa
Name:		amarok-script-wiki_lyrics
Version:	0.9.1
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://kde-apps.org/content/files/35151-%{scriptname}-%{version}.amarokscript.tar.bz2
# Source0-md5:	36ab13187af3c171b359d0e5756ff611
URL:		http://www.lyriki.com/
BuildRequires:	sed >= 4.0
Requires:	amarok >= 1.4
Requires:	ruby-modules >= 1.8
Requires:	ruby-tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_scriptdir %{_datadir}/apps/amarok/scripts

%description
A collection of lyrics scripts to interface with various sites and,
optionally, submit content to Lyriki.com or LyricWiki.org (wikis for
lyrics). All of these scripts can query the other ones when they can't
provide the lyrics for a song.

Supported sites:
- Lyriki (www.lyriki.com)
- LyricWiki (www.lyricwiki.org)
- AZ Lyrics (www.azlyrics.com)
- Jamendo (www.jamendo.com)
- Leos Lyrics (www.leoslyrics.com)
- Lyrc (lyrc.com.ar)
- Not Popular (www.notpopular.com)
- Sing365 (www.sing365.com)
- Terra Letras (letras.terra.com.br)

%description -l pl.UTF-8
Zestaw współpracujących z różnymi serwisami skryptów do pobierania
tekstów utworów i opcjonalnie umieszczania treści na Lyriki.com lub
LyricWiki.org (wiki dla tekstów utworów). Wszystkie te skrypty mogą
odpytywać inne jeśli nie znajdą tekstu piosenki.

Obsługiwane serwisy:
- Lyriki (www.lyriki.com)
- LyricWiki (www.lyricwiki.org)
- AZ Lyrics (www.azlyrics.com)
- Jamendo (www.jamendo.com)
- Leos Lyrics (www.leoslyrics.com)
- Lyrc (lyrc.com.ar)
- Not Popular (www.notpopular.com)
- Sing365 (www.sing365.com)
- Terra Letras (letras.terra.com.br)

%prep
%setup -q -n %{scriptname}
rm -f *.bat
rm -f *.kdev*

%{__sed} -i -e '1s,#!/usr/bin/env ruby,#!%{_bindir}/ruby,' *.rb

mkdir pkg
mv README *.spec *.rb pkg

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}
cp -a pkg/* $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO
%dir %{_scriptdir}/%{scriptname}
# README must be here in %files, not in %doc
%{_scriptdir}/%{scriptname}/README
%attr(755,root,root) %{_scriptdir}/%{scriptname}/*.rb
%{_scriptdir}/%{scriptname}/*.spec

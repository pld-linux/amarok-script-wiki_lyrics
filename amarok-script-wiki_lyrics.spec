# NOTE
# - could use QtRuby, Ruby/GTK or Ruby/Tk, but as only -tk was available on AC,
#   used that dependency.
%define		scriptname	wiki_lyrics
Summary:	A collection of lyrics scripts for amaroK
Summary(pl.UTF-8):	Zestaw skryptów do tekstów utworów dla amaroKa
Name:		amarok-script-wiki_lyrics
Version:	0.12.5
Release:	2
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.kde-apps.org/CONTENT/content-files/35151-wiki_lyrics-%{version}.amarokscript.tar.bz2
# Source0-md5:	85b9596a4e2d1c56185ef17740c15eb8
URL:		http://www.lyriki.com/Help:Wiki-Lyrics_Script
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
- Lyriki <www.lyriki.com>
- LyricWiki <www.lyricwiki.org>
- AZ Lyrics <www.azlyrics.com>
- Baidu MP3 <mp3.baidu.com>
- Dark Lyrics <www.darklyrics.com>
- Giitaayan <www.giitaayan.com>
- Jamendo <www.jamendo.com>
- Leos Lyrics <www.leoslyrics.com>
- Lyrc <lyrc.com.ar>
- Lyrics Download <www.lyricsdownload.com>
- Lyrics Mania <www.lyricsmania.com>
- Not Popular <www.notpopular.com>
- Seek Lyrics <www.seeklyrics.com>
- Sing365 <www.sing365.com>
- Terra Letras <letras.terra.com.br>

%description -l pl.UTF-8
Zestaw współpracujących z różnymi serwisami skryptów do pobierania
tekstów utworów i opcjonalnie umieszczania treści na Lyriki.com lub
LyricWiki.org (wiki dla tekstów utworów). Wszystkie te skrypty mogą
odpytywać inne jeśli nie znajdą tekstu piosenki.

Obsługiwane serwisy:
- Lyriki <www.lyriki.com>
- LyricWiki <www.lyricwiki.org>
- AZ Lyrics <www.azlyrics.com>
- Baidu MP3 <mp3.baidu.com>
- Dark Lyrics <www.darklyrics.com>
- Giitaayan <www.giitaayan.com>
- Jamendo <www.jamendo.com>
- Leos Lyrics <www.leoslyrics.com>
- Lyrc <lyrc.com.ar>
- Lyrics Download <www.lyricsdownload.com>
- Lyrics Mania <www.lyricsmania.com>
- Not Popular <www.notpopular.com>
- Seek Lyrics <www.seeklyrics.com>
- Sing365 <www.sing365.com>
- Terra Letras <letras.terra.com.br>

%prep
%setup -q -n %{scriptname}
rm *.kdev*
rm -rf win tests
rm {docs,amarok}/COPYING # GPL v2
rm i18n/README # note about when editing files

%{__sed} -i -e '1s,#!/usr/bin/env ruby,#!%{_bindir}/ruby,' *.rb amarok/*.rb cli/*.rb

# ELF 32-bit LSB executable, Intel 80386
# TODO: package separately if it's really needed
rm -f itrans/itrans

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}
cp -a . $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}
rm -rf $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/ChangeLog docs/TODO docs/HOWTO.txt docs/README
%dir %{_scriptdir}/%{scriptname}

%{_scriptdir}/%{scriptname}/*.rb

%dir %{_scriptdir}/%{scriptname}/cli
%{_scriptdir}/%{scriptname}/cli/*.rb

%dir %{_scriptdir}/%{scriptname}/gui
%{_scriptdir}/%{scriptname}/gui/*.rb

%dir %{_scriptdir}/%{scriptname}/i18n
%{_scriptdir}/%{scriptname}/i18n/*.rb

%dir %{_scriptdir}/%{scriptname}/utils
%{_scriptdir}/%{scriptname}/utils/*.rb

%dir %{_scriptdir}/%{scriptname}/itrans
%{_scriptdir}/%{scriptname}/itrans/*

%dir %{_scriptdir}/%{scriptname}/amarok
# README must be here in %files, not in %doc
%{_scriptdir}/%{scriptname}/amarok/README
%{_scriptdir}/%{scriptname}/amarok/amarok.rb
%{_scriptdir}/%{scriptname}/amarok/amaroklyricsscript.rb
%{_scriptdir}/%{scriptname}/amarok/pluginadapter.rb
%{_scriptdir}/%{scriptname}/amarok/plugins.rb
%attr(755,root,root) %{_scriptdir}/%{scriptname}/amarok/pluginsmanager.rb
%{_scriptdir}/%{scriptname}/amarok/wikipluginadapter.rb
%{_scriptdir}/%{scriptname}/amarok/*.spec

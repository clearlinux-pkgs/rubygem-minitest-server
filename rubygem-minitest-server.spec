#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-minitest-server
Version  : 1.0.2
Release  : 6
URL      : https://rubygems.org/downloads/minitest-server-1.0.2.gem
Source0  : https://rubygems.org/downloads/minitest-server-1.0.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc

%description
= minitest-server
home :: https://github.com/seattlerb/minitest-server
rdoc :: http://docs.seattlerb.org/minitest-server

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n minitest-server-1.0.2
gem spec %{SOURCE0} -l --ruby > rubygem-minitest-server.gemspec

%build
gem build rubygem-minitest-server.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
minitest-server-1.0.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/minitest-server-1.0.2 && rake --trace test TESTOPTS="-v" && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/minitest-server-1.0.2.gem
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/Server/cdesc-Server.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/Server/client-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/Server/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/Server/path-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/Server/quit-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/Server/report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/Server/result-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/Server/run-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/Server/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/Server/stop-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/ServerReporter/cdesc-ServerReporter.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/ServerReporter/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/ServerReporter/record-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/ServerReporter/report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/ServerReporter/sanitize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/ServerReporter/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/cdesc-Minitest.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/Minitest/plugin_server_init-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/page-History_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/page-Manifest_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/minitest-server-1.0.2/ri/page-README_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/gems/minitest-server-1.0.2/.autotest
/usr/lib64/ruby/gems/2.2.0/gems/minitest-server-1.0.2/.gemtest
/usr/lib64/ruby/gems/2.2.0/gems/minitest-server-1.0.2/History.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/minitest-server-1.0.2/Manifest.txt
/usr/lib64/ruby/gems/2.2.0/gems/minitest-server-1.0.2/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/minitest-server-1.0.2/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/minitest-server-1.0.2/lib/minitest/server.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-server-1.0.2/lib/minitest/server_plugin.rb
/usr/lib64/ruby/gems/2.2.0/gems/minitest-server-1.0.2/test/minitest/test_server.rb
/usr/lib64/ruby/gems/2.2.0/specifications/minitest-server-1.0.2.gemspec

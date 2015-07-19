%define debug_package   %{nil}
%define import_path     github.com/godbus/dbus
%define gosrc %{go_dir}/src/pkg/%{import_path}

Name:           golang-godbus
Version:        1
Release:        5
Summary:        Go client bindings for D-Bus
License:        BSD
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/v%{version}.tar.gz
BuildRequires:  golang
Requires:       golang
Group:		Development/Other
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/_examples) = %{version}-%{release}
Provides:       golang(%{import_path}/introspect) = %{version}-%{release}
Provides:       golang(%{import_path}/prop) = %{version}-%{release}

%description
Simple library that implements native Go client bindings for the
D-Bus message bus system.

Features include:
Complete native implementation of the D-Bus message protocol
Go-like API (channels for signals / asynchronous method calls, Goroutine-safe
connections)
Subpackages that help with the introspection / property interfaces.

%prep
%setup -n dbus-%{version}

%build

%install
for d in . _examples introspect prop; do
    install -d -p %{buildroot}/%{gosrc}/$d
    cp -av $d/*.go %{buildroot}/%{gosrc}/$d
done

%check

%files
%doc LICENSE README.markdown
%dir %attr(755,root,root) %{gosrc}
%dir %attr(755,root,root) %{gosrc}/_examples
%dir %attr(755,root,root) %{gosrc}/introspect
%dir %attr(755,root,root) %{gosrc}/prop
%{gosrc}/*.go
%{gosrc}/_examples/*.go
%{gosrc}/introspect/*.go
%{gosrc}/prop/*.go

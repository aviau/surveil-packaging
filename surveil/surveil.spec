name:      surveil
Version:   0.7.0
Release:   1
Summary:   Surveil API

Group:     Network
License:   Apache
URL:       https://github.com/stackforge/surveil
Source0:   http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python-setuptools

Requires: python-pecan>=0.5.0
Requires: python-pymongo>=2.7.2
Requires: python-requests
Requires: python-wsme
Requires: python-oslo-config
Requires: python-oslo-middleware
Requires: python-oslo-policy>=0.3.0
Requires: python-keystonemiddleware
Requires: python-paste-deploy
Requires: python-influxdb==2.0.1
Requires: python-six

# use to remove the dependency added by rpmbuild on python(abi)
AutoReqProv: no

%description
Monitoring as a Service for OpenStack

%package os-interface
Summary:  Surveil interface for OpenStack
#Requires: python-pika
Requires: python-surveilclient==0.6.0

%description os-interface
Surveil Interface with OpenStack

%prep
%setup -q

# Remove bundled egg-info
rm -rf surveil.egg-info

%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

echo %{buildroot}/%{python_sitelib}
rm -rf  %{buildroot}/%{python_sitelib}/surveil*.egg-info*

%files
%{python_sitelib}/surveil
%{_bindir}/surveil-api
%{_bindir}/surveil-pack-upload
%{_bindir}/surveil-init
%{_bindir}/surveil-os-discovery

%files os-interface
%{_bindir}/surveil-rabbitMQ-consumer


%pre


%post


%changelog
* Wed Jun 10 2015 Alexandre Viau <alexandre@alexandreviau.net> 1
- Initial Package

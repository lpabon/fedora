%global _confdir %{_sysconfdir}/swift

Summary  : GlusterFS Integration with OpenStack Object Storage (Swift)
Name     : glusterfs-openstack-swift
Version  : 1.10.0
Release  : 1%{?dist}
Group    : Applications/File
URL      : http://launchpad.net/gluster-swift
Source0  : https://launchpad.net/gluster-swift/havana/1.10.0-0/+download/gluster_swift-1.10.0.tar.gz
License  : ASL 2.0
BuildArch: noarch
BuildRequires: python-setuptools
BuildRequires: python2-devel
Requires : memcached
Requires : openssl
Requires : openstack-swift = 1.10.0
Requires : openstack-swift-account = 1.10.0
Requires : openstack-swift-container = 1.10.0
Requires : openstack-swift-object = 1.10.0
Requires : openstack-swift-proxy = 1.10.0
Requires : glusterfs-api >= 3.4.1
Obsoletes: glusterfs-swift-plugin <= 3.4.0
Obsoletes: glusterfs-swift <= 3.4.0
Obsoletes: glusterfs-ufo <= 3.4.0
Obsoletes: glusterfs-swift-container <= 3.4.0
Obsoletes: glusterfs-swift-object <= 3.4.0
Obsoletes: glusterfs-swift-proxy <= 3.4.0
Obsoletes: glusterfs-swift-account <= 3.4.0

%description
Gluster-Swift integrates GlusterFS as an alternative back end for OpenStack
Object Storage (Swift) leveraging the existing front end OpenStack Swift code.
GlusterFS volumes are used to store objects in files, containers are
maintained as top-level directories of volumes, where accounts are mapped
one-to-one to gluster volumes.

%prep
%setup -q -n gluster_swift-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

mkdir -p      %{buildroot}/%{_confdir}/
cp -r etc/*   %{buildroot}/%{_confdir}/

%files
%defattr(-,root,root)
%{python_sitelib}/gluster
%{python_sitelib}/gluster_swift-%{version}-*.egg-info
%{_bindir}/gluster-swift-gen-builders
%{_bindir}/gluster-swift-print-metadata
%exclude %{python_sitelib}/test
%exclude %{python_sitelib}/gluster/__init__.*

%dir %{_confdir}
%config(noreplace) %{_confdir}/account-server.conf-gluster
%config(noreplace) %{_confdir}/container-server.conf-gluster
%config(noreplace) %{_confdir}/object-server.conf-gluster
%config(noreplace) %{_confdir}/swift.conf-gluster
%config(noreplace) %{_confdir}/proxy-server.conf-gluster
%config(noreplace) %{_confdir}/fs.conf-gluster

%changelog
* Wed Nov 06 2013 Luis Pabon <lpabon@redhat.com> - 1.10.0-1
- Havana release

* Wed Sep 04 2013 Luis Pabon <lpabon@redhat.com> - 1.9.1-1
- Submit to Fedora Project

* Wed Aug 21 2013 Luis Pabon <lpabon@redhat.com> - 1.8.0-7
- Update RPM spec file to support SRPMS

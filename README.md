puppet-openstack
================

An easiest way to deploy OpenStack muti-node.

### Overview
This open source project will help you to deploy OpenStack muti-node in a simple way. Only for OpenStack Havana on Ubuntu 12.04 LTS.

### How to use?
* Clone this repo on all of the node:
```
git clone https://github.com/nofdev/puppet-openstack.git
```

* Install the Puppet master on the Puppet master server:
```
python setup.py puppetmaster
```

* Install the Puppet agent on the Puppet agent server:
```
python setup.py puppetagent
```

* Modify the site.pp for your enviroment on Puppet master:
```
vi /etc/puppet/manifests/site.pp
```

* Install the OpenStack Controller node on the Controller server:
```
python setup.py gen-cert openstack_controller
python setup.py deploy openstack_controller
```

* Install the OpenStack Compute node on the Compute server(n is a number):
```
python setup.py gen-cert openstack_compute n
python setup.py deploy openstack_compute n
```


###Or using shell script if your python version > 2.7
* Clone this repo on all of the node:
```
git clone https://github.com/nofdev/puppet-openstack.git
```

* Install the Puppet master on the Puppet master server:
```
bash scripts/puppet-installer.sh master
```

* Install the Puppet agent on the Puppet agent server:
```
bash scripts/puppet-installer.sh agent
```

* Modify the site.pp for your enviroment on Puppet master:
```
vi /etc/puppet/manifests/site.pp
```

* Install the OpenStack Controller node on the Controller server:
```
bash scripts/controller-installer.sh gen-cert openstack_controller
bash scripts/bash controller-installer.sh deploy openstack_controller
```

* Install the OpenStack Compute node on the Compute server:
```
bash scripts/compute-installer.sh gen-cert openstack_compute[n]
bash scripts/compute-installer.sh deploy openstack_compute[n]
```

### Networking

* Each of the machines running the Openstack services should have a minimum of 2 NICS.
  * One for the public/internal network
    - This nic should be assigned an IP address
  * One of the virtual machine network
    - This nic should not have an ipaddress assigned
* If machines only have one NIC, it is necessary to manually create a bridge called br100 that bridges into the ip address specified on that NIC.
* All interfaces that are used to bridge traffic for the internal network need to have promiscuous mode set.
* Below is an example of setting promiscuous mode on an interface on Ubuntu.

```
#/etc/network/interfaces
auto eth1
iface eth1 inet manual
    up ifconfig $IFACE 0.0.0.0 up
    up ifconfig $IFACE promisc
```

### Volumes

Every Compute node that is configured to be a cinder volume service must have a volume group called `cinder-volumes`.

###Dependencies
- puppetlabs/glance (>= 3.0.0 <4.0.0)
- puppetlabs/horizon (>= 3.0.0 <4.0.0)
- puppetlabs/keystone (>= 3.0.0 <4.0.0)
- puppetlabs/nova (>= 3.0.0 <4.0.0)
- puppetlabs/cinder (>= 3.0.0 <4.0.0)
- puppetlabs/swift (>= 3.0.0 <4.0.0)
- puppetlabs/neutron (>= 3.0.0 <4.0.0)
- puppetlabs/ceilometer (>= 3.0.0 <4.0.0)
- puppetlabs/heat (>= 3.0.0 <4.0.0)

###About Puppet modules
This program use the puppetlabs-openstack offical Puppet modules and dependency. If install failed, Please copy the modules/* to your Puppet modules directory.

###Author
jiasir (Taio Jia) <jiasir@icloud.com>

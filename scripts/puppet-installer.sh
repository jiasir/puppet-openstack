#!/usr/bin/env bash
#########################################
# Function:		Deploy puppet master or agent
# Usage:		bash puppet-installer.sh {master|agent}
# Author:		jiasir(Taio)
# E-Mail:		jiasir@icloud.com
# Version:		1.0
#########################################

#
# This is only for Ubuntu 12.04 LTS.
#

if [[ $1 == "" || $1 == "--help" || $1 != "master" || $1 != "agent" ]]; then
	echo "Usage: bash $0 {master|agent}"
	exit 1
fi

noti_reboot_sys() {
	echo "Please reboot your system."
}

# Generate locales to resolv the perl issue.
sudo locale-gen en_US en_US.UTF-8 zh_CN.UTF-8
sudo dpkg-reconfigure locales

WGET=$(dpkg -l | grep wget | wc -l)

# Install wget if you dont have it.
if [[ $WGET == "0" ]]; then
	sudo apt-get -y install wget
fi

# Download and install the "puppetlabs-release" package for Ubuntu 12.04.
wget https://apt.puppetlabs.com/puppetlabs-release-precise.deb
sudo dpkg -i puppetlabs-release-precise.deb

# Install the Ubuntu Cloud Archive for Havana
sudo apt-get -y install python-software-properties
sudo add-apt-repository cloud-archive:havana

# Update the package database and upgrade your system.
sudo apt-get update
sudo apt-get -y dist-upgrade

# Install puppet master or agent.
if [[ $1 == "master" ]]; then
	wget https://apt.puppetlabs.com/puppetlabs-release-precise.deb
	sudo dpkg -i puppetlabs-release-precise.deb
	sudo apt-get update
	sudo apt-get -y install puppetmaster-passenger
	sudo apt-get -y install puppetmaster
	sudo puppet module install puppetlabs-openstack --version 3.0.0
elif [[ $1 == "agent" ]]; then
	wget https://apt.puppetlabs.com/puppetlabs-release-precise.deb
	sudo dpkg -i puppetlabs-release-precise.deb
	sudo apt-get update
	sudo apt-get -y install puppet
fi

# Copy the site.pp file to /etc/puppet/manifests and install modules.
if [[ $1 == "master" ]]; then
	if [[ -f ../pp/site.pp ]]; then
		cp ../pp/site.pp /etc/puppet/manifests
		echo "Puppet master has been deployed."
		echo "Please modify /etc/puppet/manifests/site.pp"
		noti_reboot_sys
		exit 0
	else
		echo "Cannot found site.pp at ../pp/site.pp"
		exit 1
	fi
else
	echo "Puppet agent has been deployed."
	noti_reboot_sys
	exit 0
fi
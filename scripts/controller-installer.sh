#!/usr/bin/env bash
#########################################
# Function:		Deploy OpenStack Controller node
# Usage:		bash controller-installer.sh {gen-cert|deploy} <openstack_controller>
# Author:		jiasir(Taio)
# E-Mail:		jiasir@icloud.com
# Version:		1.0
#########################################

#
# This is only for Ubuntu 12.04 LTS.
#

usage() {
	echo "Usage: bash $0 {gen-cert|deploy} <openstack_controller>"
}

if [[ $1 == "" || $1 == "--help" || $1 != "gen-cert" || $1 != "deploy" ]]; then
	usage
	exit 1
fi

if [[ $2 != "openstack_controller" ]]; then
	usage
	exit 1
fi

# Generate Puppet cert and Deploy OpenStack Controller node.
if [[ $1 == "gen-cert" && $2 == "openstack_controller" ]]; then
	sudo puppet agent -t --certname $2
	echo "Please go to the Puppet master to sign this cert: \"$2\". And run \"bash $0 deploy openstack_controller\""
elif [[ $1 == "deploy" && $2 == "openstack_controller" ]]; then
	sudo puppet agent -t --certname $2
fi
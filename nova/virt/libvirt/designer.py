# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (C) 2013 Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Policy based configuration of libvirt objects

This module provides helper APIs for populating the config.py
classes based on common operational needs / policies
"""

from nova.virt import netutils


def set_vif_guest_frontend_config(conf, mac, model, driver):
    """Populate a LibvirtConfigGuestInterface instance
    with guest frontend details"""
    conf.mac_addr = mac
    if model is not None:
        conf.model = model
    if driver is not None:
        conf.driver_name = driver


def set_vif_host_backend_bridge_config(conf, brname, tapname=None):
    """Populate a LibvirtConfigGuestInterface instance
    with host backend details for a software bridge"""
    conf.net_type = "bridge"
    conf.source_dev = brname
    if tapname:
        conf.target_dev = tapname
    conf.script = ""


def set_vif_host_backend_ethernet_config(conf, tapname):
    """Populate a LibvirtConfigGuestInterface instance
    with host backend details for an externally configured
    host device.

    NB use of this configuration is discouraged by
    libvirt project and will mark domains as 'tainted'"""

    conf.net_type = "ethernet"
    conf.target_dev = tapname
    conf.script = ""


def set_vif_host_backend_ovs_config(conf, brname, interfaceid, tapname=None):
    """Populate a LibvirtConfigGuestInterface instance
    with host backend details for an OpenVSwitch bridge"""

    conf.net_type = "bridge"
    conf.source_dev = brname
    conf.vporttype = "openvswitch"
    conf.add_vport_param("interfaceid", interfaceid)
    if tapname:
        conf.target_dev = tapname
    conf.script = ""


def set_vif_host_backend_filter_config(conf, name,
                                       primary_addr,
                                       dhcp_server=None,
                                       ra_server=None,
                                       allow_same_net=False,
                                       ipv4_cidr=None,
                                       ipv6_cidr=None):
    """Populate a LibvirtConfigGuestInterface instance
    with host backend details for traffic filtering"""

    conf.filtername = name
    conf.add_filter_param("IP", primary_addr)

    if dhcp_server:
        conf.add_filter_param("DHCPSERVER", dhcp_server)

    if ra_server:
        conf.add_filter_param("RASERVER", ra_server)

    if allow_same_net:
        if ipv4_cidr:
            net, mask = netutils.get_net_and_mask(ipv4_cidr)
            conf.add_filter_param("PROJNET", net)
            conf.add_filter_param("PROJMASK", mask)

        if ipv6_cidr:
            net, prefix = netutils.get_net_and_prefixlen(ipv6_cidr)
            conf.add_filter_param("PROJNET6", net)
            conf.add_filter_param("PROJMASK6", prefix)
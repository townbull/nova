{
    "server": {
        "os-extended-server-attributes:host": "%(compute_host)s",
        "os-extended-server-attributes:hypervisor_hostname": "%(hypervisor_hostname)s",
        "os-extended-server-attributes:instance_name": "%(instance_name)s",
        "updated": "%(timestamp)s",
        "created": "%(timestamp)s",
        "access_ip_v4": "",
        "access_ip_v6": "",
        "addresses": {
            "private": [
                {
                    "addr": "%(ip)s",
                    "version": 4,
                    "mac_addr": "aa:bb:cc:dd:ee:ff",
                    "type": "fixed"
                }
            ]
        },
        "flavor": {
            "id": "1",
            "links": [
                {
                    "href": "%(host)s/flavors/1",
                    "rel": "bookmark"
                }
            ]
        },
        "host_id": "%(hostid)s",
        "id": "%(uuid)s",
        "image": {
            "id": "%(uuid)s",
            "links": [
                {
                    "href": "%(glance_host)s/images/%(uuid)s",
                    "rel": "bookmark"
                }
            ]
        },
        "links": [
            {
                "href": "%(host)s/v3/servers/%(uuid)s",
                "rel": "self"
            },
            {
                "href": "%(host)s/servers/%(uuid)s",
                "rel": "bookmark"
            }
        ],
        "metadata": {
            "My Server Name": "Apache1"
        },
        "name": "new-server-test",
        "progress": 0,
        "status": "ACTIVE",
        "tenant_id": "openstack",
        "user_id": "fake",
        "key_name": null
    }
}
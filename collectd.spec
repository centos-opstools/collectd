%global __provides_exclude_from ^%{_libdir}/collectd/.*\\.so$

Summary: Statistics collection daemon for filling RRD files
Name: collectd
Version: 5.5.1
Release: 8%{?dist}
License: GPLv2
Group: System Environment/Daemons
URL: http://collectd.org/

Source: http://collectd.org/files/%{name}-%{version}.tar.bz2
Source1: collectd-httpd.conf
Source2: collectd.service
Source91: apache.conf
Source92: email.conf
Source93: mysql.conf
Source94: nginx.conf
Source95: sensors.conf
Source96: snmp.conf
Source97: rrdtool.conf
Source98: onewire.conf

Patch0: %{name}-include-collectd.d.patch
Patch1: vserver-ignore-deprecation-warnings.patch
Patch2: modbus-avoid-enabling-libmodbus-s-debug-flag-by-defa.patch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: python-devel
BuildRequires: libgcrypt-devel
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
collectd is a small daemon written in C for performance.  It reads various
system  statistics  and updates  RRD files,  creating  them if necessary.
Since the daemon doesn't need to startup every time it wants to update the
files it's very fast and easy on the system. Also, the statistics are very
fine grained since the files are updated every 10 seconds.


%package amqp
Summary:       AMQP plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librabbitmq-devel
%description amqp
This plugin can be used to communicate with other instances of collectd
or third party applications using an AMQP message broker.


%package apache
Summary:       Apache plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description apache
This plugin collects data provided by Apache's 'mod_status'.


%package ascent
Summary:       Ascent plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
BuildRequires: libxml2-devel
%description ascent
This plugin collects data about an Ascent server,
a free server for the "World of Warcraft" game.


%package bind
Summary:       Bind plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
BuildRequires: libxml2-devel
%description bind
This plugin retrieves statistics from the BIND dns server.


%package ceph
Summary:       Ceph plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: yajl-devel
%description ceph
This plugin collects data from Ceph.


%package -n collectd-utils
Summary:       Collectd utilities
Group:         System Environment/Daemons
Requires:      libcollectdclient%{?_isa} = %{version}-%{release}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description -n collectd-utils
Collectd utilities


%package curl
Summary:       Curl plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
%description curl
This plugin reads webpages with curl


%package curl_json
Summary:       Curl JSON plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
BuildRequires: yajl-devel
%description curl_json
This plugin retrieves JSON data via curl.


%package curl_xml
Summary:       Curl XML plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
BuildRequires: libxml2-devel
%description curl_xml
This plugin retrieves XML data via curl.


%package dbi
Summary:       DBI plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libdbi-devel
%description dbi
This plugin uses the dbi library to connect to various databases,
execute SQL statements and read back the results.


%package disk
Summary:       Disk plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: systemd-devel
%description disk
This plugin collects statistics of harddisk and, where supported, partitions.


%package dns
Summary:       DNS traffic analysis plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libpcap-devel
%description dns
This plugin collects DNS traffic data.


%package drbd
Summary:       DRBD plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description drbd
This plugin collects data from DRBD.


%package email
Summary:       Email plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description email
This plugin collects data provided by spamassassin.


%package generic-jmx
Summary:       Generic JMX plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description generic-jmx
This plugin collects data provided by JMX.


%package gmond
Summary:       Gmond plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: ganglia-devel
%description gmond
This plugin receives multicast traffic sent by gmond,
the statistics collection daemon of Ganglia.


%package ipmi
Summary:       IPMI plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: OpenIPMI-devel
%description ipmi
This plugin for collectd provides IPMI support.


%package ipvs
Summary:       IPVS plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description ipvs
This plugin collects data from IPVS.


%package java
Summary:       Java bindings for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: java-devel
BuildRequires: jpackage-utils
%description java
These are the Java bindings for collectd.


%package -n libcollectdclient
Summary:       Collectd client library
Group:         System Environment/Daemons
%description -n libcollectdclient
Collectd client library.


%package -n libcollectdclient-devel
Summary:       Development files for libcollectdclient
Group:         System Environment/Daemons
Requires:      libcollectdclient%{?_isa} = %{version}-%{release}
%description -n libcollectdclient-devel
Development files for libcollectdclient.


%package log_logstash
Summary:       Logstash plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: yajl-devel
%description log_logstash
This plugin formats messages as JSON events for Logstash


%package lvm
Summary:       LVM plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: lvm2-devel
%description lvm
This plugin collects information from lvm


%package memcachec
Summary:       Memcachec plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libmemcached-devel
%description memcachec
This plugin connects to a memcached server, queries one or more
given pages and parses the returned data according to user specification.


%package modbus
Summary:       Modbus plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libmodbus-devel
%description modbus
This plugin connects to a Modbus "slave" via Modbus/TCP
and reads register values.


%package mysql
Summary:       MySQL plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: mysql-devel
%description mysql
MySQL querying plugin. This plugin provides data of issued commands,
called handlers and database traffic.


%package netlink
Summary:       Netlink plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: iproute-static, libmnl-devel
%description netlink
This plugin uses a netlink socket to query the Linux kernel
about statistics of various interface and routing aspects.


%package nginx
Summary:       Nginx plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description nginx
This plugin collects data provided by Nginx.


%package notify_desktop
Summary:       Notify desktop plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libnotify-devel
%description notify_desktop
This plugin sends a desktop notification to a notification daemon,
as defined in the Desktop Notification Specification.


%package notify_email
Summary:       Notify email plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libesmtp-devel
%description notify_email
This plugin uses the ESMTP library to send
notifications to a configured email address.


%ifnarch s390 s390x
%package nut
Summary:       Network UPS Tools plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: nut-devel
%description nut
This plugin for collectd provides Network UPS Tools support.
%endif


%package onewire
Summary:       OneWire bus plugin for collectd
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: owfs-devel
%description onewire
The experimental OneWire plugin collects temperature information
from sensors connected to the computer over the OneWire bus.


%package openldap
Summary:       OpenLDAP plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: openldap-devel
%description openldap
This plugin for collectd reads monitoring information
from OpenLDAP's cn=Monitor subtree.


%package -n perl-Collectd
Summary:       Perl bindings for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%description -n perl-Collectd
This package contains the Perl bindings and plugin for collectd.


%package pinba
Summary:       Pinba plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: protobuf-c-devel
%description pinba
This plugin receives profiling information from Pinba,
an extension for the PHP interpreter.


%package ping
Summary:       Ping plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: liboping-devel
%description ping
This plugin for collectd provides network latency statistics.


%package postgresql
Summary:       PostgreSQL plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: postgresql-devel
%description postgresql
PostgreSQL querying plugin. This plugins provides data of issued commands,
called handlers and database traffic.


%package redis
Summary:       Redis plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: hiredis-devel
%description redis
The Redis plugin connects to one or more instances of Redis, a key-value store,
and collects usage information using the hiredis library.


%package rrdcached
Summary:       RRDCacheD plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: rrdtool-devel
%description rrdcached
This plugin uses the RRDtool accelerator daemon, rrdcached(1),
to store values to RRD files in an efficient manner.


%package rrdtool
Summary:       RRDTool plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: rrdtool-devel
%description rrdtool
This plugin for collectd provides rrdtool support.


%ifnarch ppc sparc sparc64
%package sensors
Summary:       Libsensors module for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: lm_sensors-devel
%description sensors
This plugin for collectd provides querying of sensors supported by
lm_sensors.
%endif


%package smart
Summary:       SMART plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libatasmart-devel
%description smart
This plugin for collectd collects SMART statistics,
notably load cycle count, temperature and bad sectors.


%package snmp
Summary:       SNMP module for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: net-snmp-devel
%description snmp
This plugin for collectd provides querying of net-snmp.


%ifarch %ix86 x86_64
%package turbostat
Summary:       Turbostat module for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libcap-devel
%description turbostat
This plugin for collectd reads CPU frequency and C-state residency
on modern Intel turbo-capable processors.
%endif


%package varnish
Summary:       Varnish plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: varnish-libs-devel
%description varnish
This plugin collects information about Varnish, an HTTP accelerator.


%ifnarch ppc sparc sparc64
%package virt
Summary:       Libvirt plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libvirt-devel
BuildRequires: libxml2-devel
%description virt
This plugin collects information from virtualized guests.
%endif


%package web
Summary:       Contrib web interface to viewing rrd files
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      collectd-rrdtool = %{version}-%{release}
Requires:      perl-HTML-Parser, perl-Regexp-Common, rrdtool-perl, httpd
%description web
This package will allow for a simple web interface to view rrd files created by
collectd.


%package write_http
Summary:       HTTP output plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
%description write_http
This plugin can send data to Redis.


%package write_redis
Summary:       Redis output plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: hiredis-devel
%description write_redis
This plugin can send data to Redis.


%package write_riemann
Summary:       Riemann output plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: protobuf-c-devel
BuildRequires: libtool-ltdl-devel
%description write_riemann
This plugin can send data to Riemann.


%package write_sensu
Summary:       Sensu output plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description write_sensu
This plugin can send data to Sensu.


%package write_tsdb
Summary:       OpenTSDB output plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description write_tsdb
This plugin can send data to OpenTSDB.


%package xmms
Summary:       XMMS plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
BuildRequires: xmms-devel
%description xmms
This is a collectd plugin for the XMMS music player.
It graphs the bit-rate and sampling rate as you play songs.


%package zookeeper
Summary:       Zookeeper plugin for collectd
Group:         System Environment/Daemons
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description zookeeper
This is a collectd plugin that reads data from Zookeeper's MNTR command.


%prep
%autosetup -v -p1

# recompile generated files
touch src/riemann.proto src/pinba.proto


%build
%configure \
    --disable-dependency-tracking \
    --disable-silent-rules \
    --without-included-ltdl \
    --enable-all-plugins \
    --disable-static \
    --disable-apple_sensors \
    --disable-aquaero \
    --disable-barometer \
    --disable-iptables \
    --disable-lpar \
    --disable-mic \
    --disable-netapp \
%ifarch s390 s390x
    --disable-nut \
%endif
    --disable-oracle \
    --disable-pf \
    --disable-routeros \
%ifarch ppc sparc sparc64
    --disable-sensors \
%endif
    --disable-sigrok \
    --disable-tape \
    --disable-tokyotyrant \
%ifnarch %ix86 x86_64
    --disable-turbostat \
%endif
    --disable-write_kafka \
    --disable-write_mongodb \
    --with-libiptc \
    --with-java=%{java_home}/ \
    --with-python \
    --with-perl-bindings=INSTALLDIRS=vendor \
    AR_FLAGS="-cr" \

make %{?_smp_mflags}


%install
rm -rf contrib/SpamAssassin
make install DESTDIR="%{buildroot}"

install -Dp -m0644 src/collectd.conf %{buildroot}%{_sysconfdir}/collectd.conf
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/collectd.service
install -d -m0755 %{buildroot}%{_localstatedir}/lib/collectd/rrd
install -d -m0755 %{buildroot}%{_datadir}/collectd/collection3/
install -d -m0755 %{buildroot}%{_sysconfdir}/httpd/conf.d/

find contrib/ -type f -exec chmod a-x {} \;

# Remove Perl hidden .packlist files.
find %{buildroot} -name .packlist -delete
# Remove Perl temporary file perllocal.pod
find %{buildroot} -name perllocal.pod -delete

# copy web interface
cp -ad contrib/collection3/* %{buildroot}%{_datadir}/collectd/collection3/
cp -pv %{buildroot}%{_datadir}/collectd/collection3/etc/collection.conf %{buildroot}%{_sysconfdir}/collection.conf
ln -rsf %{_sysconfdir}/collection.conf %{buildroot}%{_datadir}/collectd/collection3/etc/collection.conf
cp -pv %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/collectd.conf
chmod +x %{buildroot}%{_datadir}/collectd/collection3/bin/*.cgi

# Move the Perl examples to a separate directory.
mkdir perl-examples
find contrib -name '*.p[lm]' -exec mv {} perl-examples/ \;

# Move config contribs
mkdir -p %{buildroot}%{_sysconfdir}/collectd.d/
cp %{SOURCE91} %{buildroot}%{_sysconfdir}/collectd.d/apache.conf
cp %{SOURCE92} %{buildroot}%{_sysconfdir}/collectd.d/email.conf
cp %{SOURCE93} %{buildroot}%{_sysconfdir}/collectd.d/mysql.conf
cp %{SOURCE94} %{buildroot}%{_sysconfdir}/collectd.d/nginx.conf
cp %{SOURCE95} %{buildroot}%{_sysconfdir}/collectd.d/sensors.conf
cp %{SOURCE96} %{buildroot}%{_sysconfdir}/collectd.d/snmp.conf
cp %{SOURCE97} %{buildroot}%{_sysconfdir}/collectd.d/rrdtool.conf
cp %{SOURCE98} %{buildroot}%{_sysconfdir}/collectd.d/onewire.conf

# configs for subpackaged plugins
%ifnarch s390 s390x
for p in dns ipmi libvirt nut perl ping postgresql
%else
for p in dns ipmi libvirt perl ping postgresql
%endif
do
cat > %{buildroot}%{_sysconfdir}/collectd.d/$p.conf <<EOF
LoadPlugin $p
EOF
done

# *.la files shouldn't be distributed.
rm -f %{buildroot}/%{_libdir}/{collectd/,}*.la


%check
make check


%post
%systemd_post collectd.service


%preun
%systemd_preun collectd.service


%postun
%systemd_postun_with_restart collectd.service


%post -n libcollectdclient -p /sbin/ldconfig


%postun -n libcollectdclient -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS ChangeLog README
%config(noreplace) %{_sysconfdir}/collectd.conf
%config(noreplace) %{_sysconfdir}/collectd.d/
%exclude %{_sysconfdir}/collectd.d/apache.conf
%exclude %{_sysconfdir}/collectd.d/dns.conf
%exclude %{_sysconfdir}/collectd.d/email.conf
%exclude %{_sysconfdir}/collectd.d/ipmi.conf
%exclude %{_sysconfdir}/collectd.d/libvirt.conf
%exclude %{_sysconfdir}/collectd.d/mysql.conf
%exclude %{_sysconfdir}/collectd.d/nginx.conf
%ifnarch s390 s390x
%exclude %{_sysconfdir}/collectd.d/nut.conf
%endif
%exclude %{_sysconfdir}/collectd.d/onewire.conf
%exclude %{_sysconfdir}/collectd.d/perl.conf
%exclude %{_sysconfdir}/collectd.d/ping.conf
%exclude %{_sysconfdir}/collectd.d/postgresql.conf
%exclude %{_datadir}/collectd/postgresql_default.conf
%exclude %{_sysconfdir}/collectd.d/rrdtool.conf
%exclude %{_sysconfdir}/collectd.d/sensors.conf
%exclude %{_sysconfdir}/collectd.d/snmp.conf

%{_unitdir}/collectd.service
%{_sbindir}/collectd
%{_sbindir}/collectdmon
%dir %{_localstatedir}/lib/collectd/

%dir %{_libdir}/collectd

%{_libdir}/collectd/aggregation.so
%{_libdir}/collectd/apcups.so
%{_libdir}/collectd/battery.so
%{_libdir}/collectd/cgroups.so
%{_libdir}/collectd/conntrack.so
%{_libdir}/collectd/contextswitch.so
%{_libdir}/collectd/cpu.so
%{_libdir}/collectd/cpufreq.so
%{_libdir}/collectd/csv.so
%{_libdir}/collectd/df.so
%{_libdir}/collectd/entropy.so
%{_libdir}/collectd/ethstat.so
%{_libdir}/collectd/exec.so
%{_libdir}/collectd/fhcount.so
%{_libdir}/collectd/filecount.so
%{_libdir}/collectd/fscache.so
%{_libdir}/collectd/hddtemp.so
%{_libdir}/collectd/interface.so
%{_libdir}/collectd/ipc.so
%{_libdir}/collectd/irq.so
%{_libdir}/collectd/load.so
%{_libdir}/collectd/logfile.so
%{_libdir}/collectd/madwifi.so
%{_libdir}/collectd/match_empty_counter.so
%{_libdir}/collectd/match_hashed.so
%{_libdir}/collectd/match_regex.so
%{_libdir}/collectd/match_timediff.so
%{_libdir}/collectd/match_value.so
%{_libdir}/collectd/mbmon.so
%{_libdir}/collectd/md.so
%{_libdir}/collectd/memcached.so
%{_libdir}/collectd/memory.so
%{_libdir}/collectd/multimeter.so
%{_libdir}/collectd/network.so
%{_libdir}/collectd/nfs.so
%{_libdir}/collectd/ntpd.so
%{_libdir}/collectd/numa.so
%{_libdir}/collectd/olsrd.so
%{_libdir}/collectd/openvpn.so
%{_libdir}/collectd/powerdns.so
%{_libdir}/collectd/processes.so
%{_libdir}/collectd/protocols.so
%{_libdir}/collectd/python.so
%{_libdir}/collectd/serial.so
%{_libdir}/collectd/statsd.so
%{_libdir}/collectd/swap.so
%{_libdir}/collectd/syslog.so
%{_libdir}/collectd/table.so
%{_libdir}/collectd/tail.so
%{_libdir}/collectd/tail_csv.so
%{_libdir}/collectd/target_notification.so
%{_libdir}/collectd/target_replace.so
%{_libdir}/collectd/target_scale.so
%{_libdir}/collectd/target_set.so
%{_libdir}/collectd/target_v5upgrade.so
%{_libdir}/collectd/tcpconns.so
%{_libdir}/collectd/teamspeak2.so
%{_libdir}/collectd/ted.so
%{_libdir}/collectd/thermal.so
%{_libdir}/collectd/threshold.so
%{_libdir}/collectd/unixsock.so
%{_libdir}/collectd/uptime.so
%{_libdir}/collectd/users.so
%{_libdir}/collectd/uuid.so
%{_libdir}/collectd/vmem.so
%{_libdir}/collectd/vserver.so
%{_libdir}/collectd/wireless.so
%{_libdir}/collectd/write_graphite.so
%{_libdir}/collectd/write_log.so
%{_libdir}/collectd/zfs_arc.so

%{_datadir}/collectd/types.db

%doc %{_mandir}/man1/collectd.1*
%doc %{_mandir}/man1/collectdmon.1*
%doc %{_mandir}/man5/collectd.conf.5*
%doc %{_mandir}/man5/collectd-exec.5*
%doc %{_mandir}/man5/collectd-python.5*
%doc %{_mandir}/man5/collectd-threshold.5*
%doc %{_mandir}/man5/collectd-unixsock.5*
%doc %{_mandir}/man5/types.db.5*


%files -n libcollectdclient-devel
%{_includedir}/collectd/client.h
%{_includedir}/collectd/network.h
%{_includedir}/collectd/network_buffer.h
%{_includedir}/collectd/lcc_features.h
%{_libdir}/pkgconfig/libcollectdclient.pc
%{_libdir}/libcollectdclient.so


%files -n libcollectdclient
%{_libdir}/libcollectdclient.so.1
%{_libdir}/libcollectdclient.so.1.0.0


%files -n collectd-utils
%{_bindir}/collectd-nagios
%{_bindir}/collectd-tg
%{_bindir}/collectdctl
%{_mandir}/man1/collectdctl.1*
%{_mandir}/man1/collectd-nagios.1*
%{_mandir}/man1/collectd-tg.1*

%files amqp
%{_libdir}/collectd/amqp.so


%files apache
%{_libdir}/collectd/apache.so
%config(noreplace) %{_sysconfdir}/collectd.d/apache.conf


%files ascent
%{_libdir}/collectd/ascent.so


%files bind
%{_libdir}/collectd/bind.so


%files ceph
%{_libdir}/collectd/ceph.so


%files curl
%{_libdir}/collectd/curl.so


%files curl_json
%{_libdir}/collectd/curl_json.so


%files curl_xml
%{_libdir}/collectd/curl_xml.so


%files disk
%{_libdir}/collectd/disk.so


%files dbi
%{_libdir}/collectd/dbi.so


%files dns
%{_libdir}/collectd/dns.so
%config(noreplace) %{_sysconfdir}/collectd.d/dns.conf


%files drbd
%{_libdir}/collectd/drbd.so


%files email
%{_libdir}/collectd/email.so
%config(noreplace) %{_sysconfdir}/collectd.d/email.conf
%doc %{_mandir}/man5/collectd-email.5*


%files generic-jmx
%{_datadir}/collectd/java/generic-jmx.jar


%files gmond
%{_libdir}/collectd/gmond.so


%files ipmi
%{_libdir}/collectd/ipmi.so
%config(noreplace) %{_sysconfdir}/collectd.d/ipmi.conf


%files ipvs
%{_libdir}/collectd/ipvs.so


%files java
%{_libdir}/collectd/java.so
%dir %{_datadir}/collectd/java/
%{_datadir}/collectd/java/collectd-api.jar
%doc %{_mandir}/man5/collectd-java.5*

%files log_logstash
%{_libdir}/collectd/log_logstash.so


%files lvm
%{_libdir}/collectd/lvm.so


%files memcachec
%{_libdir}/collectd/memcachec.so


%files modbus
%{_libdir}/collectd/modbus.so


%files mysql
%{_libdir}/collectd/mysql.so
%config(noreplace) %{_sysconfdir}/collectd.d/mysql.conf


%files netlink
%{_libdir}/collectd/netlink.so


%files nginx
%{_libdir}/collectd/nginx.so
%config(noreplace) %{_sysconfdir}/collectd.d/nginx.conf


%files notify_desktop
%{_libdir}/collectd/notify_desktop.so


%files notify_email
%{_libdir}/collectd/notify_email.so


%ifnarch s390 s390x
%files nut
%{_libdir}/collectd/nut.so
%config(noreplace) %{_sysconfdir}/collectd.d/nut.conf
%endif


%files onewire
%{_libdir}/collectd/onewire.so
%config(noreplace) %{_sysconfdir}/collectd.d/onewire.conf


%files openldap
%{_libdir}/collectd/openldap.so


%files -n perl-Collectd
%doc perl-examples/*
%{_libdir}/collectd/perl.so
%{perl_vendorlib}/Collectd.pm
%{perl_vendorlib}/Collectd/
%config(noreplace) %{_sysconfdir}/collectd.d/perl.conf
%doc %{_mandir}/man5/collectd-perl.5*
%doc %{_mandir}/man3/Collectd::Unixsock.3pm*


%files pinba
%{_libdir}/collectd/pinba.so


%files ping
%{_libdir}/collectd/ping.so
%config(noreplace) %{_sysconfdir}/collectd.d/ping.conf


%files postgresql
%{_libdir}/collectd/postgresql.so
%config(noreplace) %{_sysconfdir}/collectd.d/postgresql.conf
%{_datadir}/collectd/postgresql_default.conf


%files redis
%{_libdir}/collectd/redis.so


%files rrdcached
%{_libdir}/collectd/rrdcached.so


%files rrdtool
%{_libdir}/collectd/rrdtool.so
%config(noreplace) %{_sysconfdir}/collectd.d/rrdtool.conf


%ifnarch ppc sparc sparc64
%files sensors
%{_libdir}/collectd/sensors.so
%config(noreplace) %{_sysconfdir}/collectd.d/sensors.conf
%endif


%files smart
%{_libdir}/collectd/smart.so


%files snmp
%{_libdir}/collectd/snmp.so
%config(noreplace) %{_sysconfdir}/collectd.d/snmp.conf
%doc %{_mandir}/man5/collectd-snmp.5*


%ifarch %ix86 x86_64
%files turbostat
%{_libdir}/collectd/turbostat.so
%endif


%files varnish
%{_libdir}/collectd/varnish.so


%ifnarch ppc sparc sparc64
%files virt
%{_libdir}/collectd/virt.so
%config(noreplace) %{_sysconfdir}/collectd.d/libvirt.conf
%endif


%files web
%{_datadir}/collectd/collection3/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/collectd.conf
%config(noreplace) %{_sysconfdir}/collection.conf


%files write_http
%{_libdir}/collectd/write_http.so


%files write_redis
%{_libdir}/collectd/write_redis.so


%files write_riemann
%{_libdir}/collectd/write_riemann.so


%files write_sensu
%{_libdir}/collectd/write_sensu.so


%files write_tsdb
%{_libdir}/collectd/write_tsdb.so


%files xmms
%{_libdir}/collectd/xmms.so


%files zookeeper
%{_libdir}/collectd/zookeeper.so



%changelog
* Sat Apr 30 2016 Kevin Fenzi <kevin@scrye.com> - 5.5.1-8
- Rebuild for librrd

* Fri Apr 15 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> - 5.5.1-7
- Rebase modbus patch

* Fri Apr 15 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> - 5.5.1-6
- Use Type=notify in systemd unit now that collectd support it.
- Uncomment accidentally commented Requires for collectd-utils

* Sat Feb 27 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> - 5.5.1-5
- Enable zfs_arc plugin now that it supports ZoL.
- Move disk plugin to subpackage.
- Move log_logstash plugin to subpackage.
- Move write_http plugin to subpackage.
- Move utils to subpackage.
- Finally create subpackage for libcollectdclient.
- Modbus: avoid enabling libmodbus's debug flag by default

* Sat Feb 27 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> - 5.5.1-4
- Disable deprecation warnings in vserver plugin for now.
  The upcoming glibc 2.24 deprecates readdir_r.
  Reported upstream in #1566

* Fri Feb 26 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> - 5.5.1-3
- Disable -Werror
  Fixes build failures due to deprecation warnings turned into errors.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.1-1
- Rediff patch
- Use fully versioned dependencies on main package

* Sat Jan 30 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.1-0
- Upstream released new version

* Sun Dec 06 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.0-11
- Fix regression in swap plugin (#1261237)
- Replace my patch for Varnish 4.1 with upstream patches

* Sat Oct 31 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.0-10
- Fix build against Varnish 4.1 (#1275413)

* Sun Oct 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 5.5.0-9
- Use %%license
- Fix build on PPC64 and PPC64LE
- Minor spec cleanups

* Tue Sep 08 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.0-8
- Rebuild for hiredis soname bump
- Drop hardened_build macro, it's the default now

* Sat Jul 25 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.0-7
- Silence build noise by setting AR_FLAGS:
  ar: `u' modifier ignored since `D' is the default (see `U')

* Sun Jul 05 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.0-6
- Disable iptables plugin, libiptc is broken (#1239213)

* Sun Jul 05 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.0-5
- Turbostat plugin doesn't need net-snmp

* Mon Jun 22 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.0-4
- Enable Redis plugin
- Reduce diff with EPEL spec
- Remove unused collection.conf

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.0-2
- Rebuild for new OneWire version

* Fri Jun 05 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.5.0-1
- Upstream released new version
- New plugins for Ceph, DRBD, SMART, turbostat, Redis and more

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 5.4.2-5
- Perl 5.22 rebuild

* Tue Apr 21 2015 Remi Collet <remi@fedoraproject.org> 5.4.2-4
- rebuild for new librabbitmq

* Sun Apr 12 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.2-3
- Rebuilt for new Ganglia version

* Sun Mar 01 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.2-2
- Remove workaround for perl / python module loading
  This was fixed by upstream commit f131f0347f58 in 2009

* Fri Feb 27 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.2-1
- Upstream released new version
- Drop BuildRequires on owfs-capi, fixed in owfs
- Drop collectd-fix-colors-in-collection.conf.patch, fixed upstream
- Drop collectd-lvm-do-not-segfault-when-there-are-no-vgs.patch, fixed upstream

* Tue Feb 10 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.1-15
- OneWire libraries are in owfs-capi package

* Tue Feb 10 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.1-14
- Rebuilt for new OneWire version

* Wed Feb 04 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.1-13
- Exclude onewire.conf from main collectd package

* Tue Dec 09 2014 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.1-12
- Improve the systemd unit a bit

* Thu Nov 06 2014 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.1-11
- Fix building with varnish 4

* Thu Oct 16 2014 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.1-10
- Rebuilt for new OneWire version

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 5.4.1-9
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.1-7
- Rebuild for new protobuf-c again

* Wed Jul 23 2014 Ruben Kerkhof <ruben@rubenkerkhof.com> - 5.4.1-6
- Enable onewire plugin (patch from Tomasz Torcz)
- Rebuild for new protobuf-c (#1126752)

* Sat Jun 07 2014 Ruben Kerkhof <ruben@rubenkerkhof.com> - 5.4.1-5
- Fix 404 while loading stylesheet in collection3
- Restore symlink to /etc/collection.conf

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 04 2014 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.1-3
- Enable nut plugin again
- Disable varnish plugin (#1099363)
- Don't build libcollectd client with -Werror for now
  (https://github.com/collectd/collectd/issues/632)
- LVM plugin: don't segfault when there are no vgs

* Mon Mar 03 2014 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.1-2
- Disable nut plugin (#1071919)

* Tue Jan 28 2014 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.1-1
- Upstream released new version: http://collectd.org/news.shtml#news95

* Thu Jan 23 2014 Kevin Fenzi <kevin@scrye.com> 5.4.0-3
- Rebuild for new libdbi

* Sat Dec 14 2013 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.0-2
- Enable memcached plugin (#1036422)
- Stop running autoreconf

* Sun Sep 15 2013 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.4.0-1
- Update to 5.4.0
  http://mailman.verplant.org/pipermail/collectd/2013-August/005906.html
- Enable new cgroups, statsd and lvm plugins

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 5.3.0-4
- Perl 5.18 rebuild

* Mon Jun 03 2013 Kevin Fenzi <kevin@scrye.com> 5.3.0-3
- Rebuild for new ganglia

* Mon May 27 2013 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.3.0-2
- BuildRequire static version of iproute (#967214)

* Sat Apr 27 2013 Ruben Kerkhof <ruben@rubenkerkhof.com> 5.3.0-1
- update to 5.3.0
  http://mailman.verplant.org/pipermail/collectd/2013-April/005749.html
- enable all plugins we can enable
- filter plugins from Provides
- use new systemd macros (#850062)
- modernize specfile

* Mon Apr 22 2013 Alan Pevec <apevec@redhat.com> 5.2.2-1
- update to 5.2.2
  http://mailman.verplant.org/pipermail/collectd/2013-April/005749.html
- build with PIE flags rhbz#954322

* Mon Feb 04 2013 Alan Pevec <apevec@redhat.com> 5.2.1-1
- update to 5.2.1
  http://mailman.verplant.org/pipermail/collectd/2013-January/005577.html

* Mon Nov 26 2012 Alan Pevec <apevec@redhat.com> 5.2.0-1
- update to 5.2.0 from Steve Traylen rhbz#877721

* Wed Nov 21 2012 Alan Pevec <apevec@redhat.com> 5.1.1-1
- update to 5.1.1
- spec cleanups from Ruben Kerkhof
- fix postgresql_default.conf location rhbz#681615
- fix broken configuration for httpd 2.4 rhbz#871385

* Mon Nov 19 2012 Alan Pevec <apevec@redhat.com> 5.0.5-1
- new upstream version 5.0.5
  http://mailman.verplant.org/pipermail/collectd/2012-November/005465.html

* Mon Sep 17 2012 Alan Pevec <apevec@redhat.com> 5.0.4-1
- New upstream release, version bump to 5 (#743894) from Andrew Elwell

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 4.10.7-2
- Perl 5.16 rebuild

* Tue Apr 03 2012 Alan Pevec <apevec@redhat.com> 4.10.7-1
- new upstream release 4.10.7
  http://mailman.verplant.org/pipermail/collectd/2012-April/005045.html

* Wed Feb 29 2012 Alan Pevec <apevec@redhat.com> 4.10.6-1
- new upstream release 4.10.6
  http://mailman.verplant.org/pipermail/collectd/2012-February/004932.html

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Alan Pevec <apevec@redhat.com> 4.10.4-1
- new upstream version 4.10.4
  http://mailman.verplant.org/pipermail/collectd/2011-October/004777.html
- collectd-web config file DataDir value wrong rhbz#719809
- Python plugin doesn't work rhbz#739593
- Add systemd service file. (thanks Paul P. Komkoff Jr) rhbz#754460

* Fri Jul 29 2011 Kevin Fenzi <kevin@scrye.com> - 4.10.3-8
- Rebuild for new snmp again.

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 4.10.3-7
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 4.10.3-6
- Perl mass rebuild

* Fri Jul 08 2011 Kevin Fenzi <kevin@scrye.com> - 4.10.3-5
- Rebuild for new snmp

* Thu Jun 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 4.10.3-4
- Perl mass rebuild

* Tue May 03 2011 Dan Horák <dan@danny.cz> - 4.10.3-3
- fix build on s390(x)

* Tue Apr 19 2011 Alan Pevec <apevec@redhat.com> 4.10.3-2
- re-enable nut plugin rhbz#465729 rhbz#691380

* Tue Mar 29 2011 Alan Pevec <apevec@redhat.com> 4.10.3-1
- new upstream version 4.10.3
  http://collectd.org/news.shtml#news87
- disable nut 2.6 which fails collectd check:
  libupsclient  . . . . no (symbol upscli_connect not found)

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 4.10.2-4
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 07 2011 Dan Horák <dan[at]danny.cz> 4.10.2-2
- no nut on s390(x)

* Thu Dec 16 2010 Alan Pevec <apevec@redhat.com> 4.10.2-1
- New upstream version 4.10.2
- http://collectd.org/news.shtml#news86
- explicitly disable/enable all plugins, fixes FTBFS bz#660936

* Thu Nov 04 2010 Alan Pevec <apevec@redhat.com> 4.10.1-1
- New upstream version 4.10.1
  http://collectd.org/news.shtml#news85

* Sat Oct 30 2010 Richard W.M. Jones <rjones@redhat.com> 4.10.0-3
- Bump and rebuild for updated libnetsnmp.so.

* Wed Sep 29 2010 jkeating - 4.10.0-2
- Rebuilt for gcc bug 634757

* Sun Sep 19 2010 Robert Scheck <robert@fedoraproject.org> 4.10.0-1
- New upstream version 4.10.0 (thanks to Mike McGrath)

* Tue Jun 08 2010 Alan Pevec <apevec@redhat.com> 4.9.2-1
- New upstream version 4.9.2
  http://collectd.org/news.shtml#news83

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 4.9.1-3
- Mass rebuild with perl-5.12.0

* Fri Mar 26 2010 Alan Pevec <apevec@redhat.com> 4.9.1-2
- enable ping plugin bz#541744

* Mon Mar 08 2010 Lubomir Rintel <lkundrak@v3.sl> 4.9.1-1
- New upstream version 4.9.1
  http://collectd.org/news.shtml#news81

* Tue Feb 16 2010 Alan Pevec <apevec@redhat.com> 4.8.3-1
- New upstream version 4.8.3
  http://collectd.org/news.shtml#news81
- FTBFS bz#564943 - system libiptc is not usable and owniptc fails to compile:
  add a patch from upstream iptables.git to fix owniptc compilation

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 4.8.1-3
- rebuild against perl 5.10.1

* Fri Nov 27 2009 Alan Pevec <apevec@redhat.com> 4.8.1-2
- use Fedora libiptc, owniptc in collectd sources fails to compile

* Wed Nov 25 2009 Alan Pevec <apevec@redhat.com> 4.8.1-1
- update to 4.8.1 (Florian La Roche) bz# 516276
- disable ping plugin until liboping is packaged bz# 541744

* Fri Sep 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.6.5-1
- update to 4.6.5
- disable ppc/ppc64 due to compile error

* Wed Sep 02 2009 Alan Pevec <apevec@redhat.com> 4.6.4-1
- fix condrestart: on upgrade collectd is not restarted, bz# 516273
- collectd does not re-connect to libvirtd, bz# 480997
- fix unpackaged files https://bugzilla.redhat.com/show_bug.cgi?id=516276#c4
- New upstream version 4.6.4
  http://collectd.org/news.shtml#news69

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 4.6.2-5
- rebuilt with new openssl

* Thu Aug  6 2009 Richard W.M. Jones <rjones@redhat.com> - 4.6.2-4
- Force rebuild to test FTBFS issue.
- lib/collectd/types.db seems to have moved to share/collectd/types.db

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 Alan Pevec <apevec@redhat.com> 4.6.2-1
- New upstream version 4.6.2
  http://collectd.org/news.shtml#news64

* Tue Mar 03 2009 Alan Pevec <apevec@redhat.com> 4.5.3-2
- patch for strict-aliasing issue in liboping.c

* Mon Mar 02 2009 Alan Pevec <apevec@redhat.com> 4.5.3-1
- New upstream version 4.5.3
- fixes collectd is built without iptables plugin, bz# 479208
- list all expected plugins explicitly to avoid such bugs

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 4.5.1-3
- Rebuild against new mysql client.

* Sun Dec 07 2008 Alan Pevec <apevec@redhat.com> 4.5.1-2.1
- fix subpackages, bz# 475093

* Sun Nov 30 2008 Alan Pevec <apevec@redhat.com> 4.5.1-2
- workaround for https://bugzilla.redhat.com/show_bug.cgi?id=468067

* Wed Oct 22 2008 Alan Pevec <apevec@redhat.com> 4.5.1-1
- New upstream version 4.5.1, bz# 470943
  http://collectd.org/news.shtml#news59
- enable Network UPS Tools (nut) plugin, bz# 465729
- enable postgresql plugin
- spec cleanup, bz# 473641

* Fri Aug 01 2008 Alan Pevec <apevec@redhat.com> 4.4.2-1
- New upstream version 4.4.2.

* Thu Jul 03 2008 Lubomir Rintel <lkundrak@v3.sk> 4.4.1-4
- Fix a typo introduced by previous change that prevented building in el5

* Thu Jul 03 2008 Lubomir Rintel <lkundrak@v3.sk> 4.4.1-3
- Make this compile with older perl package
- Turn dependencies on packages to dependencies on Perl modules
- Add default attributes for files

* Thu Jun 12 2008 Alan Pevec <apevec@redhat.com> 4.4.1-2
- Split rrdtool into a subpackage (Chris Lalancette)
- cleanup subpackages, split dns plugin, enable ipmi
- include /etc/collectd.d (bz#443942)

* Mon Jun 09 2008 Alan Pevec <apevec@redhat.com> 4.4.1-1
- New upstream version 4.4.1.
- plugin changes: reenable iptables, disable ascent

* Tue May 27 2008 Alan Pevec <apevec@redhat.com> 4.4.0-2
- disable iptables/libiptc

* Mon May 26 2008 Alan Pevec <apevec@redhat.com> 4.4.0-1
- New upstream version 4.4.0.

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-9
- Added {?dist} to release number (thanks Alan Pevec).

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-8
- Bump release number so we can tag this in Rawhide.

* Thu Apr 17 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-6
- Exclude perl.so from the main package.

* Thu Apr 17 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-5
- Put the perl bindings and plugin into a separate perl-Collectd
  package.  Note AFAICT from the manpage, the plugin and Collectd::*
  perl modules must all be packaged together.

* Wed Apr 16 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-4
- Remove -devel subpackage.
- Add subpackages for apache, email, mysql, nginx, sensors,
  snmp (thanks Richard Shade).
- Add subpackages for perl, libvirt.

* Tue Apr 15 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-2
- Install Perl bindings in vendor dir not site dir.

* Tue Apr 15 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-1
- New upstream version 4.3.2.
- Create a -devel subpackage for development stuff, examples, etc.
- Use .bz2 package instead of .gz.
- Remove fix-hostname patch, now upstream.
- Don't mark collectd init script as config.
- Enable MySQL, sensors, email, apache, Perl, unixsock support.
- Don't remove example Perl scripts.
- Package types.db(5) manpage.
- Fix defattr.
- Build in koji to find the full build-requires list.

* Mon Apr 14 2008 Richard W.M. Jones <rjones@redhat.com> - 4.2.3.100.g79b0797-2
- Prepare for Fedora package review:
- Clarify license is GPLv2 (only).
- Setup should be quiet.
- Spelling mistake in original description fixed.
- Don't include NEWS in doc - it's an empty file.
- Convert some other doc files to UTF-8.
- config(noreplace) on init file.

* Thu Jan 10 2008 Chris Lalancette <clalance@redhat.com> - 4.2.3.100.g79b0797.1.ovirt
- Update to git version 79b0797
- Remove *.pm files so we don't get a bogus dependency
- Re-enable rrdtool; we will need it on the WUI side anyway

* Mon Oct 29 2007 Dag Wieers <dag@wieers.com> - 4.2.0-1 - 5946+/dag
- Updated to release 4.2.0.

* Mon Oct 29 2007 Dag Wieers <dag@wieers.com> - 3.11.5-1
- Initial package. (using DAR)

Использованы образы L2 и L3 Cisco IOL. В качестве клиентов - стандартные VPC из EVE-NG.

(L3-коммутатор использует образ L2 для упрощения и ускорения, маршрутизатор использует образ L3)

Не изменились конфигурации L2 и L3, клиенты могут получать адреса по DHCP, NAT функционирует, проброс порта настроен для клиента 10.0.10.3 (см. RouterFirst.cfg)
(Клиенты всё ещё могут пинговать друг друга и находятся в своих VLAN'ах и подсетях)


**VPC #1:**

VPCS> dhcp -r
DORA IP 10.0.10.11/24 GW 10.0.10.1

VPCS> ping 128.1.1.100

84 bytes from 128.1.1.100 icmp_seq=1 ttl=254 time=4.359 ms
84 bytes from 128.1.1.100 icmp_seq=2 ttl=254 time=4.114 ms
84 bytes from 128.1.1.100 icmp_seq=3 ttl=254 time=3.859 ms
84 bytes from 128.1.1.100 icmp_seq=4 ttl=254 time=2.832 ms
84 bytes from 128.1.1.100 icmp_seq=5 ttl=254 time=3.454 ms

**VPC #2**

VPCS> dhcp -r
DORA IP 10.0.20.11/24 GW 10.0.20.1

VPCS> ping 128.1.1.100

84 bytes from 128.1.1.100 icmp_seq=1 ttl=254 time=1.526 ms
84 bytes from 128.1.1.100 icmp_seq=2 ttl=254 time=3.320 ms
84 bytes from 128.1.1.100 icmp_seq=3 ttl=254 time=2.331 ms
84 bytes from 128.1.1.100 icmp_seq=4 ttl=254 time=6.803 ms
84 bytes from 128.1.1.100 icmp_seq=5 ttl=254 time=2.119 ms

VPCS> ping 10.0.10.11

84 bytes from 10.0.10.11 icmp_seq=1 ttl=63 time=2.516 ms
84 bytes from 10.0.10.11 icmp_seq=2 ttl=63 time=6.044 ms
84 bytes from 10.0.10.11 icmp_seq=3 ttl=63 time=2.671 ms
84 bytes from 10.0.10.11 icmp_seq=4 ttl=63 time=5.343 ms
84 bytes from 10.0.10.11 icmp_seq=5 ttl=63 time=4.976 ms
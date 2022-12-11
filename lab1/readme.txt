Использованы образы L2 и L3 Cisco IOL. В качестве клиентов - стандартные VPC из EVE-NG.

(L3-коммутатор использует образ L2 дл¤ упрощения и ускорения, маршрутизатор использует образ L3)

Клиенты могут статически получить IP в своей подсети своего VLAN и отвечают друг другу на пинг. STP работает, в качестве корн¤ всех VLAN настроен L3 за счёт предустановки приоритетов.


**VPC #1:**

VPCS> ip 10.0.10.2 10.0.10.1
Checking for duplicate address...
VPCS : 10.0.10.2 255.255.255.0 gateway 10.0.10.1

VPCS> ping 10.0.20.2

84 bytes from 10.0.20.2 icmp_seq=1 ttl=63 time=3.817 ms
84 bytes from 10.0.20.2 icmp_seq=2 ttl=63 time=5.378 ms
84 bytes from 10.0.20.2 icmp_seq=3 ttl=63 time=9.774 ms
84 bytes from 10.0.20.2 icmp_seq=4 ttl=63 time=4.180 ms
84 bytes from 10.0.20.2 icmp_seq=5 ttl=63 time=5.904 ms




**VPC #2:**

VPCS> ip 10.0.20.2 10.0.20.1
Checking for duplicate address...
VPCS : 10.0.20.2 255.255.255.0 gateway 10.0.20.1

VPCS> ping 10.0.10.2

84 bytes from 10.0.10.2 icmp_seq=1 ttl=63 time=9.934 ms
84 bytes from 10.0.10.2 icmp_seq=2 ttl=63 time=7.216 ms
84 bytes from 10.0.10.2 icmp_seq=3 ttl=63 time=14.317 ms
84 bytes from 10.0.10.2 icmp_seq=4 ttl=63 time=4.487 ms
84 bytes from 10.0.10.2 icmp_seq=5 ttl=63 time=4.125 ms


**L3 Switch (корень дерева для всех VLAN):**

L3Switch#sh sp

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    4097
             Address     aabb.cc00.2000
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    4097   (priority 4096 sys-id-ext 1)
             Address     aabb.cc00.2000
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    Shr 
Et0/1               Desg FWD 100       128.2    Shr 
Et0/2               Desg FWD 100       128.3    Shr 
Et0/3               Desg FWD 100       128.4    Shr 
Et1/0               Desg FWD 100       128.5    Shr 
Et1/1               Desg FWD 100       128.6    Shr 
Et1/2               Desg FWD 100       128.7    Shr 
Et1/3               Desg FWD 100       128.8    Shr 



VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    32778
             Address     aabb.cc00.2000
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)
             Address     aabb.cc00.2000
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    Shr 
Et0/1               Desg FWD 100       128.2    Shr 
Et0/2               Desg FWD 100       128.3    Shr 



VLAN0020
  Spanning tree enabled protocol rstp
  Root ID    Priority    32788
             Address     aabb.cc00.2000
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32788  (priority 32768 sys-id-ext 20)
             Address     aabb.cc00.2000
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    Shr 
Et0/1               Desg FWD 100       128.2    Shr 
Et0/2               Desg FWD 100       128.3    Shr



**L2 Switch (Vlan 20) - погашено как альтернативное соединение с другим L2:**
L2Switch20#sh sp

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    4097
             Address     aabb.cc00.2000
             Cost        100
             Port        1 (Ethernet0/0)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    20481  (priority 20480 sys-id-ext 1)
             Address     aabb.cc00.4000
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Root FWD 100       128.1    Shr 
Et0/1               Altn BLK 100       128.2    Shr 
Et0/2               Desg FWD 100       128.3    Shr 

Использованы образы L3 Cisco IOL. В качестве клиентов - стандартные VPC из EVE-NG

- Настроены NAT для "интернета" на каждом маршрутизаторе
- Проброшены тоннели - обычный в подсеть одного маршрутизатора и шифрованный в подсеть другого
- "Интернет" из-за NAT не знает ничего о внутренних подсетях
- Стандартные маршруты направлены в "интернет"

**Маршрутизатор №1 - шифрованный тоннель функционирует**

Router1#show crypto session
Crypto session current status

Interface: Tunnel2
Session status: UP-ACTIVE     
Peer: 150.0.0.1 port 500 
  Session ID: 0  
  IKEv1 SA: local 100.0.0.1/500 remote 150.0.0.1/500 Active 
  Session ID: 0  
  IKEv1 SA: local 100.0.0.1/500 remote 150.0.0.1/500 Active 
  IPSEC FLOW: permit 47 host 100.0.0.1 host 150.0.0.1 
        Active SAs: 2, origin: crypto map


VPC #1 может общаться по тоннелям с VPC #2 и VPC #3.
**VPC #1:**

VPCS> ip 10.0.0.5 10.0.0.1
Checking for duplicate address...
VPCS : 10.0.0.5 255.255.255.0 gateway 10.0.0.1

VPCS> ping 20.0.0.5

84 bytes from 20.0.0.5 icmp_seq=1 ttl=62 time=4.080 ms
84 bytes from 20.0.0.5 icmp_seq=2 ttl=62 time=1.589 ms
84 bytes from 20.0.0.5 icmp_seq=3 ttl=62 time=3.801 ms
84 bytes from 20.0.0.5 icmp_seq=4 ttl=62 time=3.078 ms
84 bytes from 20.0.0.5 icmp_seq=5 ttl=62 time=1.885 ms

VPCS> ping 30.0.0.5 

84 bytes from 30.0.0.5 icmp_seq=1 ttl=62 time=2.482 ms
84 bytes from 30.0.0.5 icmp_seq=2 ttl=62 time=2.077 ms
84 bytes from 30.0.0.5 icmp_seq=3 ttl=62 time=2.834 ms
84 bytes from 30.0.0.5 icmp_seq=4 ttl=62 time=1.769 ms
84 bytes from 30.0.0.5 icmp_seq=5 ttl=62 time=4.413 ms
**VPC #2**

VPCS> ip 20.0.0.5 20.0.0.1
Checking for duplicate address...
VPCS : 20.0.0.5 255.255.255.0 gateway 20.0.0.1

VPCS> ping 10.0.0.5 

84 bytes from 10.0.0.5 icmp_seq=1 ttl=62 time=3.967 ms
84 bytes from 10.0.0.5 icmp_seq=2 ttl=62 time=2.953 ms
84 bytes from 10.0.0.5 icmp_seq=3 ttl=62 time=3.716 ms
84 bytes from 10.0.0.5 icmp_seq=4 ttl=62 time=1.853 ms
84 bytes from 10.0.0.5 icmp_seq=5 ttl=62 time=2.229 ms

**VPC #3**

VPCS> ip 30.0.0.5 30.0.0.1
Checking for duplicate address...
VPCS : 30.0.0.5 255.255.255.0 gateway 30.0.0.1

VPCS> ping 10.0.0.5 

84 bytes from 10.0.0.5 icmp_seq=1 ttl=62 time=3.774 ms
84 bytes from 10.0.0.5 icmp_seq=2 ttl=62 time=2.228 ms
84 bytes from 10.0.0.5 icmp_seq=3 ttl=62 time=2.162 ms
84 bytes from 10.0.0.5 icmp_seq=4 ttl=62 time=5.274 ms
84 bytes from 10.0.0.5 icmp_seq=5 ttl=62 time=7.744 ms
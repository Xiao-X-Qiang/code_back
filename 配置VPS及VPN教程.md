配置VPS及VPN
1.ssr安装
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/ssr.sh && chmod +x ssr.sh && bash ssr.sh

2.bbr加速
wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh && chmod +x bbr.sh && bash bbr.sh

3.修改配置文件
    3.1 ssr配置文件
        {
        "server":"0.0.0.0",
        "server_ipv6":"::",
        "server_port":8686,
        "local_address":"127.0.0.1",
        "local_port":1080,
        "password":"mimamima",
        "timeout":120,
        "method":"chacha20",
        "protocol":"auth_aes128_md5",
        "protocol_param":"",
        "obfs":"http_simple",
        "obfs_param":"",
        "redirect":"",
        "dns_ipv6":false,
        "fast_open":false,
        "workers":1
        }
    3.2 修改
        删除两条(端口及密码);添加一条(端口及密码)
        {
        "server":"0.0.0.0",
        "server_ipv6":"::",
        "local_address":"127.0.0.1",
        "local_port":1080,

        "port_password":{
            "8686":"mimamima1",
            "8787":"mimamima2",
            "8888":"mimamima3"
        },

        "timeout":120,
        "method":"chacha20",
        "protocol":"auth_aes128_md5",
        "protocol_param":"",
        "obfs":"http_simple",
        "obfs_param":"",
        "redirect":"",
        "dns_ipv6":false,
        "fast_open":false,
        "workers":1
        }

4.开放端口
    配置远程连接的使用需要使用iptable(/etc/sysconfig/iptables),设置允许外部访问xxxx端口
    4.1 添加iptables规则
    iptables -I INPUT 1 -p tcp -m state --state NEW -m tcp --dport 2445 -j ACCEPT

    iptables -I INPUT 1 -p udp -m state --state NEW -m udp --dport 2445 -j ACCEPT

    4.2 保存规则
    service iptables save

    4.3 重启服务
    systemctl restart  iptables.service

    4.4 查看端口是否开放
    /sbin/iptables -L -n

5.关闭防火墙或者开放某端口
    5.1 关闭/重启/启动防火墙
    systemctl stop/restart/start firewalld.service
    
    5.2 查看防火墙状态
    firewall-cmd --state

    5.3 检查端口被哪个进程占用
    netstat -lnpt |grep 5672

    5.4 开放/关闭端口
    firewall-cmd --zone=public --add-port=5672/tcp --permanent   # 开放5672端口
    firewall-cmd --zone=public --add-port=5672/udp --permanent   # 开放5672端口
    firewall-cmd --zone=public --remove-port=5672/tcp --permanent  #关闭5672端口
    firewall-cmd --zone=public --remove-port=5672/udp --permanent  #关闭5672端口
    firewall-cmd --reload   # 配置立即生效
    firewall-cmd --zone=public --list-ports 查看防火墙所有开放的端口










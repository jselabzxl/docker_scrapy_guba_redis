#-*-coding=utf-8-*-

proxy_ips = set()
f = open('proxy_ips.txt')
for line in f:
    proxy_ips.add(line.strip())
f.close()

fw = open('proxy_ips_c.txt', 'w')
for ip in proxy_ips:
    fw.write('%s\n' % ip)
fw.close()

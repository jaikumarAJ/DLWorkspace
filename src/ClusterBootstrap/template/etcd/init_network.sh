curl  --cacert /etc/etcd/ssl/ca.pem --cert /etc/etcd/ssl/etcd.pem --key /etc/etcd/ssl/etcd-key.pem -X PUT -d "value={\"Network\":\"{{cnf["pod_ip_range"]}}\",\"Backend\":{\"Type\":\"vxlan\"}}" "https://127.0.0.1:2379/v2/keys/coreos.com/network/config"

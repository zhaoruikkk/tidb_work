# tidb_work

构建镜像：
docker build -t worker:1.0

注入容器：
kubectl patch TidbCluster basic --patch "$(cat add_container.yaml)" 

查看结果：
kubectl get TidbCluster basic --output yaml

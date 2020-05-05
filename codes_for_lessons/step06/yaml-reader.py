import yaml
f = open("nginx-pod.yml", "r+")
data = yaml.load(f)
print data["apiVersion"]
print data["kind"]

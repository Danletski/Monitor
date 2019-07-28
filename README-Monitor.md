# Prometheus & Grafana monitor

A Virtual box host, that deploys a Monitoring stack composed of:
 Grafana
 Prometheus
 Node-Exporter
 Graphite
The components are docker hosts deployed via docker-compose.
As default the dashboard provides the hosts stats.

### Dependencies

* Any Linux/Unix/Win host.
* VirtualBox 
* Vagrant
* Internet connection
* Python

### Installing

* Extract the Zip file
* Follow the Execution steps bellow
* Login to Grafana dashboard: 
	http://localhost:3000
* Select the "Docker monitor" dashboard to view the hosts stats

### Executing program

* Navigate to the "Monitor" Folder
* Make sure VirtualBox & Vagrant are running
* In the command line run "vagrant up -d"
* Or use the attached Jenkins file to run it as a Jenkins pipepline job
```
Thu above will deploy a virtual machine, based on Ubuntu.
Inside it will deploy dockers each docker will run a service:
Prometheus
Grafana
Node-Exporter
Graphite

Login 
Grafana default credentials:
username - admin
password - foobar (Password is stored in the `/grafana/config.monitoring` env file)

Dockers inside the VM are deployed using the docker-compose.yml file and their configurations files that are saved respectivly under the service folders.
```

## Authors

Contributors names and contact info

Dan Siletski
siletski.dan@gmail.com

## Acknowledgments

Inspiration, code snippets, etc.
* [Stack suggestions](https://github.com/vegasbrianc/prometheus)
* [Overops blog](https://blog.overops.com/graphite-vs-grafana-build-the-best-monitoring-architecture-for-your-application/)
* 
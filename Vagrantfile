Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.synced_folder "./", "/etc/ansible"
config.vm.network "public_network", 
    use_dhcp_assigned_default_route: true
  config.vm.network "forwarded_port", guest: 9090, host: 9090
  config.vm.network "forwarded_port", guest: 3000, host: 3000
  config.vagrant.plugins = "vagrant-docker-compose"
  config.vm.provision :docker
  config.vm.provision :docker_compose, yml: "/etc/ansible/docker-compose.yml"
  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 2
    v.name = "Monitor"
  end
   config.vm.provision "shell", inline: <<-SHELL
     apt-get install -y software-properties-common
     apt-add-repository ppa:ansible/ansible
     apt-get update
     apt-get install -y ansible
   SHELL
  end
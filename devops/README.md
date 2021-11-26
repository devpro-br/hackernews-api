## Setup a new droplet

```
# 1 - cria usuário ubunut (não usar root)
ssh root@137.184.32.249 < devops/bootstrap.sh

# 2 - Instalar docker engine
ansible-playbook -i hosts/production --tags docker playbook.yml

# 3 - Instalar nginx
ansible-playbook -i hosts/production --tags nginx playbook.yml

# 4 - Instalar backend
ansible-playbook -i hosts/production --tags backend playbook.yml

# 5 - Instalar configurar nginx para redicionar /api para o backend
ansible-playbook -i hosts/production --tags nginxenable playbook.yml

```

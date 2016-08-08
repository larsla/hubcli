# hubcli - CLI tool for Docker Hub

## installation
```
pip install hubcli
```

## login
You can either provide environment variables or use the cli options.
```
export DOCKERHUB_USER=my_user
export DOCKERHUB_PASSWORD=topsecret
```

```
hubcli --user my_user --password topsecret
```

## create repository
hubcli myorganization --repo myrepo --create

## delete repository
hubcli myorganization --repo myrepo --delete

## list repositories
hubcli myorganization --list

## get permissions from repository
hubcli myorganization --repo myrepo --permissions

## set permissions for repository
hubcli myorganization --repo myrepo  --set-permissions permissions.yml

## create repo and copy permissions from an existing repo (recommended way of handling permissions)
hubcli myorganization --repo existingrepo --permissions >permissions.yml  
hubcli myorganization --repo newrepo --create --set-permissions permissions.yml

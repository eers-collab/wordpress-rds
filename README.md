# wordpress-rds

How it works GitOps/Kustomization/ArgoCD

1. Uses  Kubernetes native configuration management topology
2. Kustomization.yaml ( Key configuration file with dependent manifests )
    - wordpress-Deployment

Flow
1. Make changes to versions or secrets and push to repository main branch
2. ArgoCD will sync the state and match the configurations

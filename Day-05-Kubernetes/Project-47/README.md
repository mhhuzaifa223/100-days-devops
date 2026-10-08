# Project 47 — Kubernetes RBAC Project

## Objective

Implement Kubernetes Role-Based Access Control (RBAC) to control what a Kubernetes identity is allowed to access.

This project demonstrates ServiceAccounts, Roles, RoleBindings, permission verification, least privilege, failure scenarios, and RBAC recovery.

## Technologies

- Kubernetes
- Kind
- kubectl
- YAML
- Kubernetes RBAC

## How It Works

Kubernetes RBAC controls access using three main components:

    ServiceAccount → RoleBinding → Role → Permissions

The ServiceAccount represents the identity.

The Role defines which resources and actions are allowed.

The RoleBinding connects the ServiceAccount to the Role.

## Project Structure

    Project-47/
    ├── k8s/
    │   ├── role.yaml
    │   └── rolebinding.yaml
    └── README.md

## ServiceAccount

A dedicated ServiceAccount was created:

    kubectl create serviceaccount project-47-reader

The ServiceAccount represents a Kubernetes identity that can be assigned specific permissions.

Creating a ServiceAccount does not automatically provide access to Kubernetes resources.

## RBAC Role

The Role allows the identity to access Pods with the following permissions:

    get
    list
    watch

The Role does not allow:

    delete
    create
    update
    patch

The Role definition is stored in:

    k8s/role.yaml

## RoleBinding

The RoleBinding connects:

    project-47-reader

to:

    project-47-pod-reader

The binding is stored in:

    k8s/rolebinding.yaml

Without the RoleBinding, the Role does not grant permissions to the ServiceAccount.

## Permission Testing

Permissions were tested using:

    kubectl auth can-i list pods --as=system:serviceaccount:default:project-47-reader

The result was:

    yes

Additional permission checks demonstrated least privilege:

    get pods              → yes
    list pods             → yes
    delete pods           → no
    get services          → no
    create deployments    → no

This confirmed that the ServiceAccount could only perform the actions explicitly granted by the Role.

## Failure Scenario

The RoleBinding was intentionally deleted:

    kubectl delete rolebinding project-47-pod-reader-binding

After removing the binding, the same permission test returned:

    no

This demonstrated that the Role and ServiceAccount alone do not establish access.

The RoleBinding is the connection between the identity and the permissions.

## Recovery

The RoleBinding was restored using:

    kubectl apply -f k8s/rolebinding.yaml

Permission was verified again:

    kubectl auth can-i list pods --as=system:serviceaccount:default:project-47-reader

The result returned:

    yes

## Troubleshooting

### ServiceAccount has no permissions

Check:

    kubectl auth can-i list pods --as=system:serviceaccount:default:project-47-reader

If the result is `no`, verify the RoleBinding:

    kubectl get rolebinding project-47-pod-reader-binding

Then inspect it:

    kubectl describe rolebinding project-47-pod-reader-binding

### Role exists but access is denied

A Role does not grant permissions by itself.

Verify that the RoleBinding references the correct:

- ServiceAccount
- Role
- Namespace

### Verify the Role

    kubectl get role project-47-pod-reader

Inspect the rules:

    kubectl describe role project-47-pod-reader

## Key Concepts Learned

- Kubernetes RBAC
- ServiceAccounts
- Roles
- RoleBindings
- Resource permissions
- Kubernetes verbs
- `kubectl auth can-i`
- Least privilege
- Namespace-scoped permissions
- Permission boundaries
- RBAC troubleshooting
- RBAC failure recovery

## Result

Successfully implemented Kubernetes RBAC with a dedicated ServiceAccount that can read Pods but cannot access unrelated resources or perform unauthorized actions.

The project demonstrated:

Identity → Permission Definition → Binding → Verification → Failure → Recovery

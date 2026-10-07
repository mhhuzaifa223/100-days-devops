# Project 43 — Persistent Application Using PV / PVC

## Objective

Demonstrate Kubernetes persistent storage using a PersistentVolumeClaim (PVC) and dynamically provisioned PersistentVolume (PV), and verify that application data survives Pod deletion and recreation.

## Technologies

- Kubernetes
- Kind
- PersistentVolume (PV)
- PersistentVolumeClaim (PVC)
- StorageClass
- BusyBox
- kubectl

## How It Works

The application uses a PVC to request persistent storage.

The Kind cluster provides a default `standard` StorageClass using the `rancher.io/local-path` provisioner.

The storage flow is:

    Pod
      ↓
    PVC
      ↓
    StorageClass
      ↓
    Dynamically Provisioned PV
      ↓
    Persistent Storage

The PVC uses:

    accessModes:
      - ReadWriteOnce

and requests:

    storage: 1Gi

## Project Structure

    Project-43/
    ├── k8s/
    │   ├── pvc.yaml
    │   └── app.yaml
    └── README.md

## StorageClass

The cluster uses:

    standard (default)

with:

    PROVISIONER: rancher.io/local-path
    VOLUMEBINDINGMODE: WaitForFirstConsumer
    RECLAIMPOLICY: Delete

Because the StorageClass uses `WaitForFirstConsumer`, the PVC initially remained Pending until a Pod consumed it.

Once the Pod was scheduled, Kubernetes dynamically provisioned and bound the PV.

## PersistentVolumeClaim

The PVC requests 1Gi of persistent storage:

    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: project-43-pvc
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi

## Application

The BusyBox Pod mounts the PVC at:

    /data

The container writes:

    /data/message.txt

with the content:

    Project 43 persistent data

## Verification

The PVC initially showed:

    STATUS: Pending

After the Pod consumed the PVC:

    STATUS: Bound

A dynamically provisioned PV was created and bound to the PVC.

The application successfully wrote and read:

    Project 43 persistent data

## Persistence Test

The application Pod was deleted:

    kubectl delete pod project-43-app

After deletion:

- Pod was removed.
- PVC remained Bound.
- PV remained Bound.
- Persistent data remained available.

The Pod was then recreated using the same PVC.

The original data was successfully read:

    Project 43 persistent data

This confirmed that the data was not stored only inside the Pod's temporary filesystem.

## Important Kubernetes Behavior

Deleting a Pod does not delete the PVC.

The PVC continues to reference the persistent storage.

However, deleting the PVC can cause the dynamically provisioned PV and its underlying storage to be deleted when the StorageClass uses:

    reclaimPolicy: Delete

This project therefore demonstrates the difference between Pod lifecycle and persistent storage lifecycle.

## Troubleshooting

During deployment, the Pod initially showed:

    ContainerCreating

`kubectl describe pod project-43-app` was used to inspect the Pod lifecycle and Events.

The Events showed:

    Scheduled
    Pulled
    Created
    Started

The Pod then reached:

    Running

This confirmed that the storage was successfully mounted and the application started normally.

## Key Concepts Learned

- PersistentVolume
- PersistentVolumeClaim
- StorageClass
- Dynamic provisioning
- WaitForFirstConsumer
- ReadWriteOnce
- Persistent storage
- Pod lifecycle
- PVC lifecycle
- PV lifecycle
- Reclaim policies
- Kubernetes storage troubleshooting

## Result

Successfully deployed a Kubernetes application using persistent storage and demonstrated that application data survives Pod deletion and recreation through a PersistentVolumeClaim and dynamically provisioned PersistentVolume.

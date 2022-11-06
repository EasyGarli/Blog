#!/bin/bash

VM_RUN_RESULT=$( virsh start Docker-debian11 )

if [[ "$VM_RUN_RESULT" == "Domain 'Docker-debian11' started" ]]; then
        echo $VM_RUN_RESULT
        sleep 20
        source ../../../../envs/RemComEnv/bin/activate
        python run_container.py

        bash start_backend.sh
    else
        echo "VM DIDN'T START"
fi
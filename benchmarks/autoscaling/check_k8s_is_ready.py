# from kubernetes import client, config
# import time
# import sys

# def wait_for_pods_ready(target_deployment):
#     v1 = client.CoreV1Api()
#     while True:
#         pods = v1.list_pod_for_all_namespaces().items
#         all_pods_ready = True
#         for pod in pods:
#             if target_deployment in pod.metadata.name:
#                 container_statuses = pod.status.container_statuses or []
#                 total_containers = len(container_statuses)
#                 ready_containers = sum(1 for c in container_statuses if c.ready)
                
#                 if ready_containers != total_containers:
#                     all_pods_ready = False
#                     print(f"Pod {pod.metadata.name}: {ready_containers}/{total_containers} containers ready")
#                     break

#         if all_pods_ready:
#             print("All pods have all containers ready")
#             return
#         time.sleep(5)

# def wait_for_all_pa_ready(namespace="default"):
#     custom_api = client.CustomObjectsApi()
#     while True:
#         try:
#             pas = custom_api.list_namespaced_custom_object(
#                 group="autoscaling.aibrix.ai",
#                 version="v1alpha1",
#                 namespace=namespace,
#                 plural="podautoscalers"
#             )
#             all_ready = True
#             for pa in pas['items']:
#                 conditions = pa.get('status', {}).get('conditions', [])
#                 if not any(c['type'] == 'AbleToScale' and c['status'] == 'True' for c in conditions):
#                     all_ready = False
#                     name = pa['metadata']['name']
#                     print(f"PA {name} conditions:")
#                     for c in conditions:
#                         print(f"- Type: {c['type']}, Status: {c['status']}, Reason: {c.get('reason', 'N/A')}")
#                     break
#             if all_ready:
#                 print("All podautoscaler are ready")
#                 return True
#             time.sleep(5)
#         except Exception as e:
#             print(f"Error checking PAs: {e}")
#             time.sleep(5)

# if __name__ == "__main__":
#     target_deployment = sys.argv[1]
#     config.load_kube_config(context="ccr3aths9g2gqedu8asdg@41073177-kcu0mslcp5mhjsva38rpg")
#     wait_for_all_pa_ready()
#     wait_for_pods_ready(target_deployment)
#     print("All pods are ready")



##################################################################



from kubernetes import client, config
import time
import sys


def wait_for_pods_ready(target_deployment):
    v1 = client.CoreV1Api()
    while True:
        pods = v1.list_pod_for_all_namespaces().items
        all_pods_ready = True
        for pod in pods:
            if target_deployment in pod.metadata.name:
                if pod.status.phase != 'Running':
                    all_pods_ready = False
                    print(f"Pod {pod.metadata.name} is not running (Phase: {pod.status.phase})")
                    break
                container_statuses = pod.status.container_statuses or []
                for container in container_statuses:
                    if not container.ready:
                        all_pods_ready = False
                        print(f"Container {container.name} in pod {pod.metadata.name} is not ready")
                        break
                if not all_pods_ready:
                    break
        if all_pods_ready:
            print("All pods and their containers are ready")
            return
        # time.sleep(5)


def wait_for_all_pa_ready(namespace="default"):
    custom_api = client.CustomObjectsApi()
    while True:
        try:
            pas = custom_api.list_namespaced_custom_object(
                group="autoscaling.aibrix.ai",
                version="v1alpha1",
                namespace=namespace,
                plural="podautoscalers"
            )
            all_ready = True
            for pa in pas['items']:
                conditions = pa.get('status', {}).get('conditions', [])
                if not any(c['type'] == 'AbleToScale' and c['status'] == 'True' for c in conditions):
                        all_ready = False
                        name = pa['metadata']['name']
                        print(f"PA {name} conditions:")
                        for c in conditions:
                            print(f"- Type: {c['type']}, Status: {c['status']}, Reason: {c.get('reason', 'N/A')}")
                        break
            if all_ready:
                print("All podautoscaler are ready")
                return True
        except Exception as e:
            print(f"Error checking PAs: {e}")


if __name__ == "__main__":
    target_deployment = sys.argv[1]
    config.load_kube_config(context="ccr3aths9g2gqedu8asdg@41073177-kcu0mslcp5mhjsva38rpg")
    wait_for_all_pa_ready()
    wait_for_pods_ready(target_deployment)
    print("All pods are ready")
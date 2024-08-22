import os

def generate_kustomization_file(directory):
    # List of YAML files to include in the kustomization.yaml
    resources = []
    
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            resources.append(filename)
    
    # Create kustomization.yaml content
    kustomization_content = "resources:\n"
    for resource in resources:
        kustomization_content += f"  - {resource}\n"
    
    # Write the kustomization.yaml file
    kustomization_file_path = os.path.join(directory, "kustomization.yaml")
    with open(kustomization_file_path, "w") as kustomization_file:
        kustomization_file.write(kustomization_content)

    print(f"Generated kustomization.yaml in {directory}")

def generate_kustomization_files_recursively(base_directory):
    # Walk through each directory in the base directory
    for root, dirs, files in os.walk(base_directory):
        generate_kustomization_file(root)

# Specify the base directory containing your Kubernetes YAML files
base_directory = "Prod/Files/deployment"

generate_kustomization_files_recursively(base_directory)
import os

def generate_kustomization_file(directory):
    # List of YAML files to include in the kustomization.yaml
    resources = []
    
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            resources.append(filename)
    
    # Create kustomization.yaml content
    kustomization_content = "resources:\n"
    for resource in resources:
        kustomization_content += f"  - {resource}\n"
    
    # Write the kustomization.yaml file
    kustomization_file_path = os.path.join(directory, "kustomization.yaml")
    with open(kustomization_file_path, "w") as kustomization_file:
        kustomization_file.write(kustomization_content)

    print(f"Generated kustomization.yaml in {directory}")

def generate_kustomization_files_recursively(base_directory):
    # Walk through each directory in the base directory
    for root, dirs, files in os.walk(base_directory):
        generate_kustomization_file(root)

# Specify the base directory containing your Kubernetes YAML files
base_directory = "/path/to/your/kubernetes/files"

generate_kustomization_files_recursively(base_directory)

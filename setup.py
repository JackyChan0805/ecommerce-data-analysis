import kagglehub
import os
import shutil

def setup_project():
    """Download dataset and prepare project structure"""
    
    # Create data folder
    os.makedirs("data", exist_ok=True)
    
    # Download dataset
    print("Downloading dataset...")
    path = kagglehub.dataset_download("carrie1/ecommerce-data")
    
    # Find and move CSV
    for file in os.listdir(path):
        if file.endswith(".csv"):
            src = os.path.join(path, file)
            dst = os.path.join("data", "ecommerce_data.csv")
            shutil.move(src, dst)
            print(f"Dataset saved to: {dst}")
            break

if __name__ == "__main__":
    setup_project()

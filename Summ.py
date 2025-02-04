import os
import matplotlib.pyplot as plt
import pandas as pd

def get_module_paths(module_name):
    base_dir = os.path.join('/home/hgc-qc-web/Wirebond/', 'Modules')
    images_dir = os.path.join(base_dir, module_name, 'Resultswirebond')
    labels_dir = os.path.join(base_dir, module_name, 'Resultswirebond', 'labels')
    return images_dir , labels_dir

def process_labels(label_path):
    category_data = {
        'Glue': [],
        'Broken': [],
        'Anomaly': [],
        'One Wire': [],
        'Two Wire': [],
        'All Wires': [],
        'Good': []
    }

    for file_name in os.listdir(label_path):
        if not file_name.endswith('.txt'):
            continue
        image_name = file_name.replace(".txt", ".jpg")
        file_path = os.path.join(label_path, file_name)
        with open(file_path, 'r') as file:
            lines = file.readlines()
            categories = [int(line.strip()[0]) for line in lines]

            # Append image to appropriate categories
            if 1 not in categories and 2 not in categories and 3 not in categories:
                category_data['Good'].append(image_name)
            else:
                if 1 in categories:
                    category_data['Broken'].append(image_name)
                if 2 in categories:
                    category_data['Glue'].append(image_name)
                if 3 in categories:
                    category_data['Anomaly'].append(image_name)

            if categories.count(0) == 1:
                category_data['One Wire'].append(image_name)
            elif categories.count(0) == 2:
                category_data['Two Wire'].append(image_name)
            elif categories.count(0) == 3:
                category_data['All Wires'].append(image_name)

    return category_data

def create_histogram(category_data, images_path):
    counts = [len(images) for images in category_data.values()]
    plt.figure(figsize=(12, 6))
    categories = list(category_data.keys())

    plt.bar(categories, counts, color='skyblue')
    plt.title("Class Distribution Histogram")
    plt.xlabel("Class")
    plt.ylabel("Number of Images")
    save_path = os.path.join(images_path, 'Histogram.jpg')
    plt.savefig(save_path, dpi=100)
    plt.close()
    print(f"Histogram saved at {save_path}")

def create_summary_table(category_data, images_path):
    data_summary = {
        "Class": list(category_data.keys()),
        "Image Count": [len(images) for images in category_data.values()],
        "Image Names": [', '.join(images[:5]) + ('...' if len(images) > 5 else '') for images in category_data.values()]
    }
    summary_df = pd.DataFrame(data_summary)
    summary_file_path = os.path.join(images_path, 'Summary_Table.csv')
    summary_df.to_csv(summary_file_path, index=False)
    print(f"Summary table saved at: {summary_file_path}")

def main():
    module_name = input("Enter the module name (e.g., 'M35'): ")
    images_path, labels_path = get_module_paths(module_name)
    category_data = process_labels(labels_path)
    create_histogram(category_data, images_path)
    create_summary_table(category_data, images_path)
    print("Histogram and Summary Table generated successfully.")

if __name__ == "__main__":
    main()

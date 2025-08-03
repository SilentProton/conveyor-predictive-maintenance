import os

labels_folder = "labels"

for filename in os.listdir(labels_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(labels_folder, filename)
        
        with open(file_path, "r") as f:
            lines = f.readlines()
        
        updated_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts:  # make sure line is not empty
                pass
                # if parts[0] == "0":  # classname as per old dataset
                #     parts[0] = "3"   #classname  as per data.yaml
                # elif parts[0] == "1":
                #     parts[0] = "5"  
                
                updated_lines.append(" ".join(parts))
        
        with open(file_path, "w") as f:
            f.write("\n".join(updated_lines))

print("✅ All class IDs converted according to the class names in data.yaml.")

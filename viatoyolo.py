## Iban Berganzo-Besga ## 
### Post-doctoral Fellow
#### Ramsey Laboratory for Environmental Archaeology (RLEA)​
#### University of Toronto Mississauga (UTM)​
### Associate Researcher​
#### Landscape Archaeology Research Group (GIAP)​
#### Catalan Institute of Classical Archaeology (ICAC)​

import os
import json
import argparse

def via_to_yolo(folder_path, outFolder, xSize, ySize):
    for filename in os.listdir(folder_path):
        if filename.endswith(('.json', '.JSON')):
            json_file = os.path.join(folder_path, filename)
            with open(json_file) as f:
                data = json.load(f)

            all_points_x = None
            all_points_y = None 
            filenames = []
            for filename, image_data in data.items():
                filename2, _ = os.path.splitext(filename)
                print("Processed image: ", filename2)
                regions = image_data.get('regions', [])

                for region in regions:
                    shape_attributes = region.get('shape_attributes', {})
                    if shape_attributes.get('name') == 'polygon':
                        x_values = shape_attributes.get('all_points_x', [])
                        y_values = shape_attributes.get('all_points_y', [])
                        all_points_x = x_values
                        all_points_y = y_values
                        
                        values = []
                        values.append(0) # only one class
                        for i in range(len(all_points_x)):
                            values.append(round(all_points_x[i]/xSize, 4))
                            values.append(round(all_points_y[i]/ySize, 4))
                        
                        outpath = os.path.join(outFolder, filename2)

                        result = ' '.join(map(str, values))
                        if not outpath.endswith('.txt'):
                            outpath += '.txt'
                        with open(outpath, 'a' if os.path.exists(outpath) else 'w') as file1:
                            file1.write(result + '\n')

def main():
    parser = argparse.ArgumentParser(description='VIA to YOLO Format')
    parser.add_argument('--img', nargs=2, metavar=('xSize', 'ySize'), type=int, required=True, help='Image size in pixels horizontally and vertically')   
    args = parser.parse_args()
    xSize, ySize = args.img
    
    folder = 'via'
    outFolder = "yolo"
    via_to_yolo(folder, outFolder, xSize, ySize)

if __name__ == "__main__":
    main()


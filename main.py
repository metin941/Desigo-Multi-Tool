import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from PIL import Image as PILImage
from PIL import Image, ImageTk
from datetime import datetime
import re
import xml.etree.ElementTree as ET
import configparser
import os
import sys
import csv



#Configuration files==============================================
config = configparser.ConfigParser()

# Check if the config file exists, if not create one
CONFIG_FILE = 'config.ini'
if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'w') as f:
        config.write(f)

#Save path for Uplad svg
def save_upload_svg_path(uploaded_svg_file_path):
    config.read(CONFIG_FILE)
    if 'Path_upload_svg' not in config:
        config['Path_upload_svg'] = {}
    config['Path_upload_svg']['uploaded_svg_file_path'] = uploaded_svg_file_path
    with open(CONFIG_FILE, 'w') as f:
        config.write(f)

def save_upload_debug_path(upload_debug_file_path):
    config.read(CONFIG_FILE)
    if 'Path_upload_debug_file' not in config:
        config['Path_upload_debug_file'] = {}
    config['Path_upload_debug_file']['upload_debug_file_path'] = upload_debug_file_path
    with open(CONFIG_FILE, 'w') as f:
        config.write(f)

def save_export_all_path(export_all_file_path):
    config.read(CONFIG_FILE)
    if 'Export_all_file_path' not in config:
        config['Export_all_file_path'] = {}
    config['Export_all_file_path']['export_all_file_path'] = export_all_file_path
    with open(CONFIG_FILE, 'w') as f:
        config.write(f)

def save_upload_combine_svg_path(upload_combine_svg_paths):
    config.read(CONFIG_FILE)
    if 'Path_upload_combine_svg' not in config:
        config['Path_upload_combine_svg'] = {}
    for idx, path in enumerate(upload_combine_svg_paths):
        config['Path_upload_combine_svg'][f'upload_combine_svg_path_{idx}'] = path
    with open(CONFIG_FILE, 'w') as f:
        config.write(f)

def save_upload_combine_xml_path(upload_combine_xml_path):
    config.read(CONFIG_FILE)
    if 'Path_upload_combine_xml' not in config:
        config['Path_upload_combine_xml'] = {}
    for idx, path in enumerate(upload_combine_xml_path):
        config['Path_upload_combine_xml'][f'upload_combine_xml_path_{idx}'] = path
    with open(CONFIG_FILE, 'w') as f:
        config.write(f)

def save_ready_graphic_file_path(ready_graphic_file_path):
    config.read(CONFIG_FILE)
    if 'Path_ready_graphic_file' not in config:
        config['Path_ready_graphic_file'] = {}
    for idx, path in enumerate(ready_graphic_file_path):
        config['Path_ready_graphic_file'][f'ready_graphic_file_path_{idx}'] = path
    with open(CONFIG_FILE, 'w') as f:
        config.write(f)

def save_ready_as_file_path(ready_as_file_path):
    config.read(CONFIG_FILE)
    if 'Path_ready_as_file' not in config:
        config['Path_ready_as_file'] = {}
    for idx, path in enumerate(ready_as_file_path):
        config['Path_ready_as_file'][f'ready_as_file_path_{idx}'] = path
    with open(CONFIG_FILE, 'w') as f:
        config.write(f)



def read_upload_svg(key='Path_upload_svg', subkey='uploaded_svg_file_path'):
    if key in config:
        if subkey in config[key]:
            return config[key][subkey]
    return ''

def read_upload_debug(key='Path_upload_debug_file', subkey='upload_debug_file_path'):
    if key in config:
        if subkey in config[key]:
            return config[key][subkey]
    return ''

def read_export_all(key='Export_all_file_path', subkey='export_all_file_path'):
    if key in config:
        if subkey in config[key]:
            return config[key][subkey]
    return ''

def read_upload_combine_svg(key='Path_upload_combine_svg', subkey='upload_combine_svg_path'):
    paths = []
    if key in config:
        for config_key in config[key]:
            paths.append(config[key][config_key])
    return paths

def read_upload_combine_xml(key='Path_upload_combine_xml', subkey='upload_combine_xml_path'):  
    if key in config:  
        paths = []  
        i = 0  
        while True:  
            path_key = f"{subkey}_{i}"  
            if path_key in config[key]:  
                paths.append(config[key][path_key])  
                i += 1  
            else:  
                break  
        return paths  
    return []  

def read_ready_graphic_file_path(key='Path_ready_graphic_file', subkey='ready_graphic_file_path'):  
    if key in config:  
        paths = []  
        i = 0  
        while True:  
            path_key = f"{subkey}_{i}"  
            if path_key in config[key]:  
                paths.append(config[key][path_key])  
                i += 1  
            else:  
                break  
        return paths  
    return []  

def read_ready_as_file_path(key='Path_ready_as_file', subkey='ready_as_file_path'):  
    if key in config:  
        paths = []  
        i = 0  
        while True:  
            path_key = f"{subkey}_{i}"  
            if path_key in config[key]:  
                paths.append(config[key][path_key])  
                i += 1  
            else:  
                break  
        return paths  
    return []  

#BACKEND AND FUNCTIONS=============================================

def upload_svg():
    file_path = filedialog.askopenfilename(filetypes=[("SVG files", "*.svg")])
    if file_path:
        # Save the selected file path to the config file for uploading SVG files
        save_upload_svg_path(file_path)

def upload_debug():
    file_path = filedialog.askopenfilename(filetypes=[("debug files", "*.debug")])
    if file_path:
        # Save the selected file path to the config file for uploading SVG files
        save_upload_debug_path(file_path)

def export_all():
    folder_path = filedialog.askdirectory()
    if folder_path:
        # Save the selected folder path to the config file for saving report files
        save_export_all_path(folder_path)

def upload_combine_svg():
    file_paths = filedialog.askopenfilenames(filetypes=[("SVG files", "*.svg")])
    if file_paths:
        # Save the selected file paths to the config file for uploading SVG files
        save_upload_combine_svg_path(list(file_paths))  # Convert file_paths tuple to list

def upload_combine_xml():
    file_paths = filedialog.askopenfilenames(filetypes=[("xml files", "*.xml")])
    if file_paths:
        # Save the selected file paths to the config file for uploading SVG files
        save_upload_combine_xml_path(list(file_paths))  # Convert file_paths tuple to list

def upload_ready_graphic_file():
    file_paths = filedialog.askopenfilenames(filetypes=[("xml files", "*.xml")])
    if file_paths:
        # Save the selected file paths to the config file for uploading SVG files
        save_ready_graphic_file_path(list(file_paths))  # Convert file_paths tuple to list

def upload_ready_as_file():
    file_paths = filedialog.askopenfilenames(filetypes=[("xml files", "*.xml")])
    if file_paths:
        # Save the selected file paths to the config file for uploading SVG files
        save_ready_as_file_path(list(file_paths))  # Convert file_paths tuple to list

#LOGS ===========================================================
class PrintLogger:
    def __init__(self, text_widget, label_widget):
        self.text_widget = text_widget
        self.label_widget = label_widget

    def write(self, message):
        self.text_widget.configure(state='normal')
        self.text_widget.insert(tk.END, message)
        self.text_widget.configure(state='disabled')
        self.text_widget.see(tk.END)

    def flush(self):
        pass

def clear_logs():
    text_widget.configure(state='normal')
    text_widget.delete(1.0, tk.END)
    text_widget.configure(state='disabled')

#INPUTS FUNCTIONS ===============================================
def on_entry_click(event):
    if regex_input.get() == "Enter your text here... example (B'A , B'Ahu , ect.)":
        regex_input.delete(0, "end")  # delete all the text in the entry
        regex_input.insert(0, '')  # insert blank for user input
        regex_input.config(foreground='black')

def on_focusout(event):
    if regex_input.get() == '':
        regex_input.insert(0, "Enter your text here... example (B'A , B'Ahu , ect.)")
        regex_input.config(foreground='grey')

#MAIN Functions===================================================

def extract_program_signals():
    try:
        # Define the input and output file paths
        input_file_path = read_upload_debug()
        output_file_path = read_export_all()+"/"+f"{str(regex_input.get())}.xml"

        # Read the content of the input file
        with open(input_file_path, 'rb') as file:
            content = file.read()

        # Remove BOM if present
        if content.startswith(b'\xef\xbb\xbf'):
            content = content[3:]

        # Decode content to string
        content = content.decode('utf-8')

        # Parse the XML content
        tree = ET.ElementTree(ET.fromstring(content))
        root = tree.getroot()

        # Initialize a list to hold extracted sections
        extracted_sections = []

        # Traverse the XML tree to find elements with attributes starting with "B01"
        found = False
        for elem in root.iter():
            # Check all attributes of the element
            for attr, value in elem.attrib.items():
                regex_string = str(regex_input.get())
                if value.startswith(regex_string):
                    found = True
                    extracted_sections.append(ET.tostring(elem, encoding='unicode'))
                    break  # No need to check other attributes once a match is found

        if not found:
            #print(f"No elements with attributes starting with '<input string>' found.")
            print(f"No elements with attributes starting with 'searched input' found.")
        else:
            #print(f"Found {len(extracted_sections)} elements with attributes starting with 'B01'.")
            print(f"Found {len(extracted_sections)} elements.")

        # Join the extracted sections into a single string
        extracted_content = "\n".join(extracted_sections)

        # Write the extracted content to a new text file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_content)

        print(f'Extracted sections saved to: {output_file_path}')

    except ET.ParseError as e:
        print(f'Error parsing XML: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not subelem.tail or not subelem.tail.strip():
            subelem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def extract_and_combine_svg():
    try:
        # Define the input and output file paths for SVG processing
        input_file_paths = read_upload_combine_svg()
        output_directory = read_export_all()
        output_file_path = os.path.join(output_directory, "combined_svg_output.svg")
        designations_file_path = os.path.join(output_directory, "Structured_Graphic_Datapoints.xml")

        # Initialize an empty string to store combined content
        combined_content = ""

        # Initialize a list to store extracted designations
        designations = []

        # Initialize a flag to check if any Datapoint elements were found
        found_datapoints = False

        # Loop through each input file path
        for file_path in input_file_paths:
            # Read the content of each input file
            with open(file_path, 'rb') as file:
                content = file.read()

            # Remove BOM if present
            if content.startswith(b'\xef\xbb\xbf'):
                content = content[3:]

            # Decode content to string
            content = content.decode('utf-8')

            # Parse the SVG content
            tree = ET.ElementTree(ET.fromstring(content))
            root = tree.getroot()

            # Traverse the SVG tree to find Datapoint elements
            for elem in root.iter():
                if elem.tag.endswith('}Datapoint'):  # Check if the element is a Datapoint
                    found_datapoints = True
                    combined_content += f"<Graphic.Point>{ET.tostring(elem, encoding='unicode')}</Graphic.Point>"

                    # Extract Designation attribute
                    designation = elem.get('Designation')
                    if designation:
                        designations.append(designation)

        if not found_datapoints:
            print("No Datapoint elements found in the input files.")
        else:
            print("Combined Datapoint elements from all input SVG files.")

        # Wrap the combined content in the root SVG element
        svg_header = '<svg xmlns="http://www.w3.org/2000/svg">'
        svg_footer = '</svg>'
        final_combined_content = f"{svg_header}\n{combined_content}\n{svg_footer}"

        # Write the combined content to a new SVG file
        os.makedirs(output_directory, exist_ok=True)
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(final_combined_content)

        print(f'Combined SVG elements saved to: {output_file_path}')

        # Write the extracted designations to a text file wrapped in <Graphic.Datapoints> tags
        with open(designations_file_path, 'w', encoding='utf-8') as designations_file:
            designations_file.write('<Graphic.Datapoints>\n')
            for designation in designations:
                designations_file.write(f"<Graphic.Point>{designation}</Graphic.Point>\n")
            designations_file.write('</Graphic.Datapoints>\n')

        print(f'Extracted designations saved to: {designations_file_path}')

        # Process Graphic_Datapoints.xml and extract parts
        final_output_file_path = os.path.join(output_directory, "Graphic_Datapoints.xml")
        with open(designations_file_path, 'r', encoding='utf-8') as file:
            xml_content = file.read()

        # Extract <Graphic.Point> elements within <Graphic.Datapoints>
        graphic_points = re.findall(r'<Graphic\.Point>(.*?)</Graphic\.Point>', xml_content)

        # Extract the part after 'BACx01.' and remove everything after the first semicolon or at symbol
        extracted_parts = []
        for point in graphic_points:
            match = re.search(r'BACx01\.(.*)', point)
            if match:
                part = match.group(1).split(';')[0].split('@')[0].replace('.', "'")
                extracted_parts.append(part)

        # Remove duplicates and entries ending with a period ('.')
        extracted_parts = list(set(extracted_parts))
        extracted_parts = [part for part in extracted_parts if not part.endswith('.')]

        # Write the extracted parts to an output file
        with open(final_output_file_path, 'w', encoding='utf-8') as output_file:
            for part in extracted_parts:
                output_file.write(part + '\n')

        print(f'Extracted parts saved to: {final_output_file_path}')

        # Delete the combined SVG file
        os.remove(output_file_path)

        # Delete the structured Graphic Datapoints XML file
        os.remove(designations_file_path)

    except ET.ParseError as e:
        print(f'Error parsing SVG: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

def combine_xml_values():
    try:
        import re  # Importing the 're' module for regular expressions
    except ImportError:
        print("Failed to import the 're' module. Please ensure it is installed.")

    xml_paths = read_upload_combine_xml()  # Assuming this function reads and returns the paths of XML files
    combined_values = []

    for path in xml_paths:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Use regular expression to find values
            values = re.findall(r'Value="([^"]*)"', content)
            print(f"Found {len(values)} values in file: {path}")

            combined_values.extend(values)

        except Exception as e:
            print(f'An error occurred while processing {path}: {e}')

    if combined_values:
        print(f"Combined values: {combined_values}")
    else:
        print("No values found to combine.")

    # Write the combined values to a file
    export_path = read_export_all()  # Assuming this function reads and returns the export path
    if not export_path:
        print("Export path not found in configuration.")
        return

    output_file_path = os.path.join(export_path, 'AS_Datapoints.xml')
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for value in combined_values:
            output_file.write(f"{value}\n")

    print(f'Combined values saved to {output_file_path}')

def compare_lines_and_write_to_csv():
    try:
        input_file_paths_graphic = read_ready_graphic_file_path()
        input_file_paths_as = read_ready_as_file_path()
        output_directory = read_export_all()

        total_lines_file1 = 0
        matching_lines_count = 0

        output_file_path = os.path.join(output_directory, "comparison_report.csv")

        with open(output_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Graphic_Datapoints', 'AS_Datapoints', 'Match Status'])

            for graphic_file_path, as_file_path in zip(input_file_paths_graphic, input_file_paths_as):
                with open(graphic_file_path, 'r') as f1, open(as_file_path, 'r') as f2:
                    for line_number_file1, line_file1 in enumerate(f1, start=1):
                        total_lines_file1 += 1
                        line_file1 = line_file1.strip()  # Remove leading and trailing whitespace
                        f2.seek(0)  # Reset the file pointer for file2 to the beginning
                        found_match = False
                        for line_number_file2, line_file2 in enumerate(f2, start=1):
                            line_file2 = line_file2.strip()  # Remove leading and trailing whitespace
                            if line_file1 == line_file2:
                                matching_lines_count += 1
                                writer.writerow([line_file1, line_file2, 'Match'])
                                found_match = True
                                break
                        if not found_match:
                            writer.writerow([line_file1, '', 'No Match'])

        # Calculate percentage of matching lines
        percentage_matching = (matching_lines_count / total_lines_file1) * 100

        # Append percentage matching to the CSV file
        with open(output_file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['', '', f'Percentage of lines matching: {percentage_matching:.2f}%'])

        print(f'Comparison report saved to: {output_file_path}')

    except Exception as e:
        print(f'An error occurred: {e}')

def create_image_from_svg():
    current_date = datetime.now().strftime("%Y-%m-%d")
    output_file_path = read_export_all()+"/"+f"Output_Image_{current_date}.png"

        # Open a file dialog to select the SVG file
    file_path = filedialog.askopenfilename(filetypes=[("SVG files", "*.svg")])
    if not file_path:
        return

    with open(file_path, 'r') as file:
        svg_content = file.read()

    def extract_symbol_refs_with_coordinates(svg_content):
        symbol_refs_with_coordinates = []
        lines = svg_content.split('\n')

        viewbox_width = None
        viewbox_height = None

        # Search for viewBox attribute using regex
        viewbox_match = re.search(r'viewBox="(\d+)\s+(\d+)\s+(\d+)\s+(\d+)"', svg_content)
        if viewbox_match:
            viewbox_width = float(viewbox_match.group(3))
            viewbox_height = float(viewbox_match.group(4))

        for line in lines:
            if 'SymbolRef="' in line:
                start_index = line.find('SymbolRef="') + len('SymbolRef="')
                end_index = line.find('"', start_index)
                symbol_ref = line[start_index:end_index]
                symbol_ref = symbol_ref[8:]  # Remove the first backslash
                symbol_ref = symbol_ref.replace("\\", "\\Symbols\\", 1)  # Add 'Symbols\\' after the second '\\'
                symbol_ref = "Database\\" + symbol_ref.replace("/", "\\")  # Replace forward slashes with backslashes
                symbol_ref += ".png"  # Append ".png"
                
                # Extract x and y coordinates if available
                x = None
                y = None
                if 'X="' in line:
                    x_index = line.find('X="') + len('X="')
                    x_end_index = line.find('"', x_index)
                    x_str = line[x_index:x_end_index]
                    if x_str.isdigit():
                        x = float(x_str)

                if 'Y="' in line:
                    y_index = line.find('Y="') + len('Y="')
                    y_end_index = line.find('"', y_index)
                    y_str = line[y_index:y_end_index]
                    if y_str.isdigit():
                        y = float(y_str)

                # Get width and height from the SVG element
                width = 0
                height = 0
                if 'width="' in line:
                    width_start_index = line.find('width="') + len('width="')
                    width_end_index = line.find('"', width_start_index)
                    width_str = line[width_start_index:width_end_index]
                    if width_str.isdigit():
                        width = float(width_str)

                if 'height="' in line:
                    height_start_index = line.find('height="') + len('height="')
                    height_end_index = line.find('"', height_start_index)
                    height_str = line[height_start_index:height_end_index]
                    if height_str.isdigit():
                        height = float(height_str)

                symbol_refs_with_coordinates.append((symbol_ref, x, y, width, height))
        return symbol_refs_with_coordinates, viewbox_width, viewbox_height

    def create_image(symbol_refs, viewbox_width, viewbox_height):
        # Create a blank image with white background
        background = PILImage.new('RGBA', (int(viewbox_width), int(viewbox_height)), (255, 255, 255, 255))

        # Paste each PNG onto the blank image at its coordinates
        for symbol_ref, x, y, width, height in symbol_refs:
            # Open the PNG image
            image = PILImage.open(symbol_ref).convert("RGBA")

            # If x and y coordinates are not None, paste the image onto the blank image
            if x is not None and y is not None:
                background.paste(image, (int(x), int(y)), mask=image)

        # Convert the image to RGB and save it
        background = background.convert('RGB')
        background.save(output_file_path)

    try:
        print(f"Image saved to: {output_file_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

    # Extract symbol references and coordinates
    symbol_refs, viewbox_width, viewbox_height = extract_symbol_refs_with_coordinates(svg_content)
    
    # Create the image
    create_image(symbol_refs, viewbox_width, viewbox_height)

#INFORMATION WINDOW===============================================
def info():
    root_info = tk.Tk()
    root_info.geometry("300x300")
    root_info.title("Information")
    root_info.iconbitmap(r"Visuals\main_window_icon.ico")
    root_info.resizable(False, False)

    #Information Labels
    label_info = tk.Label(root_info, text="Version 2.01\r Team memebers:\r\r -Metin Hasanov (GBS CEE ENG IMP)\r\r -Velina Ilieva (GBS CEE ENG IMP)\r\r -Petar Marchev(GBS CEE ENG PEX2)")
    label_info.place(x=50,y=15)

    root_info.mainloop()

#FRONTEND=======================================================

# Create the main window
root = tk.Tk()
root.geometry("590x500")
root.title("Siemens - Desigo Engineering Multi Tool")
root.iconbitmap("Visuals\main_window_icon.ico")
root.resizable(False, False)
# Set background color
background_color = "#F9F9F9"  # Light gray

#Menu bar
menu_bar = tk.Menu(root)

import_menu = tk.Menu(menu_bar, tearoff=0)
import_menu.add_command(label="Upload AS program file (.debug)",command=upload_debug)
import_menu.add_command(label="Combine Graphic files (.svg)",command=upload_combine_svg)
import_menu.add_command(label="Combine AS program files (.xml)",command=upload_combine_xml)
import_menu.add_command(label="Graphic files for comparing(.xml)",command=upload_ready_graphic_file)
import_menu.add_command(label="Upload AS file fir comparing(.xml)",command=upload_ready_as_file)

menu_bar.add_cascade(label="Upload",menu=import_menu)

menu_bar.add_cascade(label="Export", command=export_all)

menu_bar.add_cascade(label="Info",command=info)

menu_bar.add_cascade(label="Help")

root.config(menu=menu_bar)

#Draw canvas separator lines 
def draw_separator(canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill="gray", width=1)

canvas = tk.Canvas(root, background=background_color)
canvas.pack(fill=tk.BOTH, expand=True)

# Draw separator lines
draw_separator(canvas, 10, 100, 580, 100)
draw_separator(canvas, 10, 260, 580, 260)
draw_separator(canvas, 10, 350, 580, 350)

#VISUALS====================================================
# Add Siemens logo
image_siemens_logo = Image.open("Visuals\Siemens_logo.png")  # Replace "image_path.png" with the path to your image
image_siemens_logo = image_siemens_logo.resize((270, 70))  # Resize the image if necessary
photo_siemens_logo = ImageTk.PhotoImage(image_siemens_logo)
image_label_siemens_logo = tk.Label(root, image=photo_siemens_logo,background=background_color)
image_label_siemens_logo.image = photo_siemens_logo  # To prevent garbage collection
image_label_siemens_logo.place(x=125, y=270)

# Add AI logo
image = Image.open("Visuals\logo.png")  # Replace "image_path.png" with the path to your image
image = image.resize((60, 60))  # Resize the image if necessary
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo,background=background_color)
image_label.image = photo  # To prevent garbage collection
image_label.place(x=395, y=275)

#LABELS=====================================================

# Set Accuracy label
regex_label = tk.Label(root, text="Search and extraxt datapoints from AS (.debug) file:",background=background_color)
regex_label.place(x=10,y=60)

#INPUT FIELDS================================================
# Regex input
regex_input = ttk.Entry(root)
regex_input.place(x=290,y=60,width=280)

regex_input.insert(0, "Enter your text here... example (B'A , B'Ahu , ect.)")
regex_input.config(foreground='grey')

regex_input.bind('<FocusIn>', on_entry_click)
regex_input.bind('<FocusOut>', on_focusout)

#BUTTONS=====================================================
# Button Check
check_file = ttk.Button(root,text="Extract AS signals",command=extract_program_signals)
check_file.place(x=10,y=360,width=190)

# Button auto correct
combine_xml = ttk.Button(root,text="Combine AS signals",command=combine_xml_values)
combine_xml.place(x=10,y=390,width=190)

# Button Check
combine_svg = ttk.Button(root,text="Extract & Combine Graphic signals",command=extract_and_combine_svg)
combine_svg.place(x=200,y=360,width=190)

# Button auto correct
combine_signals = ttk.Button(root,text="Compare Datapoints & print report",command=compare_lines_and_write_to_csv)
combine_signals.place(x=200,y=390,width=190)

clear_log_button = ttk.Button(root, text="Clear Logs", command=clear_logs)
clear_log_button.place(x=390, y=390,width=190)

clear_log_button = ttk.Button(root, text="Create image from svg", command=create_image_from_svg)
clear_log_button.place(x=390, y=360,width=190)

frame = ttk.Frame(root)
frame.place(x=10,y=105,width=570,height=150)

text_widget = ScrolledText(frame, wrap=tk.WORD, height=10)
text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
text_widget.configure(state='disabled')  # Make the ScrolledText widget read-only

# Create the label widget
label_widget = tk.Label(root, text="", fg="red")
label_widget.pack(side=tk.BOTTOM, fill=tk.X)

# Instantiate PrintLogger and redirect stdout
print_logger = PrintLogger(text_widget, label_widget)
sys.stdout = print_logger

root.mainloop() 
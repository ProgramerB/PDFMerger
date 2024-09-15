from pypdf import PdfWriter
import argparse
import os
from pathlib import Path
parser=argparse.ArgumentParser(description='''
                               Script to append pdf files, \n\t 
                               
                               To run: python script.py --file file1.pdf file2.pdf --name <name_of_file> --title <title_of_file>''',
                               epilog='by Bhavish Nadar')


parser.add_argument('--files', help='List of files', required=True, metavar='Files', nargs='+')
parser.add_argument('--name', help='Name of merged file', required=True, metavar='Name', type=str)
parser.add_argument('--title', help='Title of merged the file', metavar='Title',  required=True, type=str) 
parser.add_argument('-c', '--current_path',help='Use saved path var -> default_path', action='store_true')

args=parser.parse_args()

print (os.getcwd())
print(str(Path.home() / "Downloads"))
print(Path(os.environ['USERPROFILE']) / 'Downloads')
print(args.current_path)


default_path = 'D:\\Users\\Bhavish\\Downloads\\'

try:
    writer = PdfWriter()
    for pdf in args.files:
        writer.append(pdf)

    writer.add_metadata(
        {
            # "/Author": "Martin",
            # "/Producer": "Libre Writer",
            "/Title": args.title
            # "/Subject": "Subject",
            # "/Keywords": "Keywords",
            # "/CreationDate": time,
            # "/ModDate": time,
            # "/Creator": "Creator",
            # "/CustomField": "CustomField",
        }
    )

    file_name = args.name+".pdf"

    if args.current_path:
        saved_path = os.getcwd()
    else:
        file_name = default_path+file_name
        saved_path = default_path
           
    writer.write(file_name)
    print("File saved as "+file_name+" in "+saved_path)
    
except Exception as e:
    print(e)

finally:
    writer.close()


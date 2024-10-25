import os
import img2pdf

# def main():
dir_jpg = 'jpg'
print("Booting up JPG CONVERTER 9000...")
for filename in os.listdir("jpg"):
    # macOS creates temporary files in directories, avoid these
    if(filename != ".DS_Store"):
        # Check for folder input
        if(os.path.isdir("jpg/" + filename)):
            print("Found folder input: /jpg" + filename)
            for file in os.listdir("jpg/" + filename):
                # check for temporary file again when traversing the new directory
                if(file != ".DS_Store"):
                    input = "jpg/"+ filename + "/" + file
                    print(input)
                    if "jpg" in file:
                        output = "pdf/" + file.replace("jpg", "pdf")
                    elif "jpeg" in file: 
                        output = "pdf/" + file.replace("jpeg", "pdf")
                    else:
                        output = "pdf/" + file
                        break
                    with open(input, "rb") as f:
                        pdf_bytes = img2pdf.convert(f.read())
                    with open(output, "wb") as f:
                        f.write(pdf_bytes) 
                    # os.remove(input)
                    print(file + "processed...")
        else:
            input = "jpg/" + filename
            if "jpg" in filename:
                output = "pdf/" + filename.replace("jpg", "pdf")
            elif "jpeg" in filename: 
                output = "pdf/" + filename.replace("jpeg", "pdf")
            else :
                output = "pdf/" + filename
                break
            with open(input, "rb") as f:
                pdf_bytes = img2pdf.convert(f.read())
            with open(output, "wb") as f:
                f.write(pdf_bytes) 
            # os.remove(input)
            print(filename + "processed...")
print("JPG CONVERTER 9000 done. .../jpg folder cleaned")


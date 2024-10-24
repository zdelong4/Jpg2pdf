import os
import img2pdf

def main():
    dir_jpg = 'jpg'
    print("Booting up JPG CONVERTER 9000...")
    for filename in os.listdir("jpg"):
        # macOS creates temporary files in directories, avoid these
        if(filename != ".DS_Store"):
            # Check for folder input
            print(filename + " " + str(os.path.isdir(filename)))
            # print(os.path.isdir(filename))
            if(os.path.isdir(filename)):
                print("here")
                for file in os.listdir(filename):
                    # check for temporary file again when traversing the new directory
                    if(filename != ".DS_Store"):
                        input = "jpg/" + filename
                        if "jpg" in filename:
                            output = "pdf/" + filename.replace("jpg", "pdf")
                        elif "jpeg" in filename: 
                            output = "pdf/" + filename.replace("jpeg", "pdf")
                        else:
                            output = "pdf/" + filename
                            break
                        with open(input, "rb") as f:
                            pdf_bytes = img2pdf.convert(f.read())
                        with open(output, "wb") as f:
                            f.write(pdf_bytes) 
                        # os.remove(input)
                        print(filename + "processed...")
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
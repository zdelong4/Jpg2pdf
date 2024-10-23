import os
import img2pdf

dir_jpg = 'jpg'
print("Booting up JPG CONVERTER 9000...")
for filename in os.listdir("jpg"):
    if(filename != ".DS_Store"):
        print("jpg/" + filename)
        input = "jpg/" + filename
        if "jpg" in filename:
            output = "pdf/" + filename.replace("jpg", "pdf")
        elif "jpeg" in filename: 
            output = "pdf/" + filename.replace("jpeg", "pdf")
        else :
            output = "pdf/" + filename
        with open(input, "rb") as f:
            pdf_bytes = img2pdf.convert(f.read())
        with open(output, "wb") as f:
            f.write(pdf_bytes) 
        # os.remove(input)
        print(filename + " processed...")
# print("JPG CONVERTER 9000 done. .../jpg folder cleaned")

    
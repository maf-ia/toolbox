import zipfile as zip
 
with zip.ZipFile(name+".zip","r") as zf:
    namelist = zf.namelist()[0][:-4]
    zf.extractall(pwd="mypassword") 

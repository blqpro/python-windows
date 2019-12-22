import os
import shutil

def copydir(src, dst):
  h = os.getcwd()
  src = r"{}".format(src)
  if not os.path.isdir(dst):
     print("\n[!] No Such directory: ["+dst+"] !!!")
     exit(1)

  if not os.path.isdir(src):
     print("\n[!] No Such directory: ["+src+"] !!!")
     exit(1)
  if "\\" in src:
     c = "\\"
     tsrc = src.split("\\")[-1:][0]
  else:
    c = "/"
    tsrc = src.split("/")[-1:][0]

  os.chdir(dst)
  if os.path.isdir(tsrc):
    print("\n[!] The Directory Is already exists !!!")
    exit(1)
  try:
    os.mkdir(tsrc)
  except WindowsError:
    print("\n[!] Error: In[ {} ]\nPlease Check Your Dirctory Path !!!".format(src))
    exit(1)
  os.chdir(h)
  files = []
  for i in os.listdir(src):
    files.append(src+c+i)
  if len(files) > 0:
    for i in files:
        if not os.path.isdir(i):
            shutil.copy2(i, dst+c+tsrc)

  print("\n[*] Done ! :)")

src_dir = os.path.join('A:/', 'dossier', 'source', )
dest_dir = os.path.join('A:/', 'dossier', 'destination',)

copydir(src_dir, dest_dir)
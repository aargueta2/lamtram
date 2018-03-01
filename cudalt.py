#!/usr/bin/python
# libtoolish hack: compile a .cu file like libtool does
import sys
import os

lo_filepath = sys.argv[1]
o_filepath = lo_filepath.replace(".lo", ".o")

try:
   i = o_filepath.rindex("/")
   lo_dir = o_filepath[0:i+1]
   o_filename = o_filepath[i+1:]

except ValueError:
   lo_dir = ""
   o_filename = o_filepath

local_pic_dir = ".libs/"
local_npic_dir = ""
pic_dir = lo_dir + local_pic_dir
npic_dir = lo_dir + local_npic_dir

pic_filepath = pic_dir + o_filename
npic_filepath = npic_dir + o_filename
local_pic_filepath = local_pic_dir + o_filename
local_npic_filepath = local_npic_dir + o_filename

# Make lib dir
try:
   os.mkdir(pic_dir)
except OSError:
   pass

# generate the command to compile the .cu for shared library
args = sys.argv[2:]
args.extend(["-Xcompiler","-fPIC"]) # position indep code
args.append("-o")
args.append(pic_filepath)
command = " ".join(args)
print command

# compile the .cu
rv = os.system(command)
if rv != 0:
    sys.exit(1)

# generate the command to compile the .cu for static library
args = sys.argv[2:]
args.append("-o")
args.append(npic_filepath)
command = " ".join(args)
print command

# compile the .cu
rv = os.system(command)
if rv != 0:
    sys.exit(1)

# get libtool version
fd = os.popen("libtool --version")
libtool_version = fd.readline()
# this loop supresses the broken pipe errors
# you get by not reading all the data
for dog in fd.readlines():
    noop = 1;
fd.close()

# generate the .lo file
f = open(lo_filepath, "w")
f.write("# " +  lo_filepath + " - a libtool object file\n")
f.write("# Generated by " + libtool_version + "\n")
f.write("#\n")
f.write("# Please DO NOT delete this file!\n")
f.write("# It is necessary for linking the library.\n\n")

f.write("# Name of the PIC object.\n")
f.write("pic_object='" + local_pic_filepath + "'\n\n")

f.write("# Name of the non-PIC object.\n")
f.write("non_pic_object='" + local_npic_filepath + "'\n")
f.close()

sys.exit(0)

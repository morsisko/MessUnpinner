import re
import sys

X86 = 0x3
X86_64 = 0x3E
ARM_V7A = 0x28
ARM64_V8A = 0xB7

patches = {}

#patches[architecture] = (pattern, offset, patch)
patches[X86] = (re.compile(b"\x83\xFE\x01\x0F\x85....\x8D\x84\\x24\x90\x00\x00\x00\x89\x04\\x24"), 3, bytearray(b"\x90\x90\x90\x90\x90\x90"))
patches[X86_64] = (re.compile(b"\x83\xFD\x01\x0F\x85....\x48\x8D\xBC\\x24.\x00\x00\x00"), 3, bytearray(b"\x90\x90\x90\x90\x90\x90"))
patches[ARM_V7A] = (re.compile(b"\x01\x2e.\xf0..\x04\xf1\x20\x00....\x25\xa8....\x26\xa8....\x27\xa8"), 2, bytearray(b"\x00\xBF\x00\xBF"))
patches[ARM64_V8A] = (re.compile(b"\x9f\x06\x00\x71...\x54....\xe0\x23\x03\x91"), 4, bytearray(b"\x1F\x20\x03\xD5"))

if len(sys.argv) != 2:
    print("Usage: patch.py <binary>")
    sys.exit(-1)
    
data = bytearray(open(sys.argv[1], mode="rb").read())
e_machine = int(data[0x12])

if e_machine not in patches:
    print("Unsupported architecture: supported architectures x86, x86_64, arm-v7a, arm64-v8a")
    sys.exit(-2)
    
pattern, offset, patch = patches[e_machine]
results = pattern.search(data)

if not results:
    print("Sorry, couldn't find any matching pattern. Is your application already patched? Try to reinstall the application. Please file new issue in the repository. Architecture:", e_machine)
    sys.exit(-3)
    
data_start = results.start() + offset
print("Found match at: ", data_start, "patching...")

i = 0
for b in patch:
    data[data_start + i] = b
    i += 1
    
print("OK! Writing")
open("patch_" + sys.argv[1], mode="wb").write(data)
print("OK!")
sys.exit(0)
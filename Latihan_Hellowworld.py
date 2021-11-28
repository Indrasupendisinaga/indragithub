x = True
y = False
z = False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)
    

#cara mengompile python ke yang namanya bytecode
#caranya adalah
# - buka terminal dan tuliskan
# - python -m py__compile main.py (main.py adalah nama folder yang akan di compile atau bisa diartikan
# (compile dokumen adalah memasukkan ke dalama sebuah folder)

"""
untuk membuat sebuah keterangan tanpa menampilkan pada saat di run bisa menggunakan tanda kutip tiga kali  atau """
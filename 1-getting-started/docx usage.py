Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getwd()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    os.getwd()
AttributeError: module 'os' has no attribute 'getwd'
>>> os.getcwd()
'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> import docx
>>> d = doc.Document('c:\\Users\\User\\Decktop\\demo.docx')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d = doc.Document('c:\\Users\\User\\Decktop\\demo.docx')
NameError: name 'doc' is not defined
>>> d = docx.Document('c:\\Users\\User\\Decktop\\demo.docx')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d = docx.Document('c:\\Users\\User\\Decktop\\demo.docx')
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\api.py", line 25, in Document
    document_part = Package.open(docx).main_document_part
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\package.py", line 116, in open
    pkg_reader = PackageReader.from_file(pkg_file)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\pkgreader.py", line 32, in from_file
    phys_reader = PhysPkgReader(pkg_file)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\phys_pkg.py", line 31, in __new__
    "Package not found at '%s'" % pkg_file
docx.opc.exceptions.PackageNotFoundError: Package not found at 'c:\Users\User\Decktop\demo.docx'
>>> d = docx.Document('c:\\Users\\User\\Decktop\\demo.docx')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d = docx.Document('c:\\Users\\User\\Decktop\\demo.docx')
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\api.py", line 25, in Document
    document_part = Package.open(docx).main_document_part
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\package.py", line 116, in open
    pkg_reader = PackageReader.from_file(pkg_file)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\pkgreader.py", line 32, in from_file
    phys_reader = PhysPkgReader(pkg_file)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\phys_pkg.py", line 31, in __new__
    "Package not found at '%s'" % pkg_file
docx.opc.exceptions.PackageNotFoundError: Package not found at 'c:\Users\User\Decktop\demo.docx'
>>> d = docx.Document('c:\\Users\\User\\Desktop\\demo.docx')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d = docx.Document('c:\\Users\\User\\Desktop\\demo.docx')
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\api.py", line 25, in Document
    document_part = Package.open(docx).main_document_part
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\package.py", line 116, in open
    pkg_reader = PackageReader.from_file(pkg_file)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\pkgreader.py", line 32, in from_file
    phys_reader = PhysPkgReader(pkg_file)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\phys_pkg.py", line 31, in __new__
    "Package not found at '%s'" % pkg_file
docx.opc.exceptions.PackageNotFoundError: Package not found at 'c:\Users\User\Desktop\demo.docx'
>>> d = docx.Document('c:\\Users\\User\\Desktop\\demo.docx')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d = docx.Document('c:\\Users\\User\\Desktop\\demo.docx')
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\api.py", line 25, in Document
    document_part = Package.open(docx).main_document_part
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\package.py", line 116, in open
    pkg_reader = PackageReader.from_file(pkg_file)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\pkgreader.py", line 32, in from_file
    phys_reader = PhysPkgReader(pkg_file)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\phys_pkg.py", line 31, in __new__
    "Package not found at '%s'" % pkg_file
docx.opc.exceptions.PackageNotFoundError: Package not found at 'c:\Users\User\Desktop\demo.docx'
>>> d = docx.Document('c:\\Users\\User\\Desktop\\demo.docx')
>>> d.paragraphs
[<docx.text.paragraph.Paragraph object at 0x01F5A630>, <docx.text.paragraph.Paragraph object at 0x01F5AB70>, <docx.text.paragraph.Paragraph object at 0x01F5A250>]
>>> d.paragraph[0].text
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d.paragraph[0].text
AttributeError: 'Document' object has no attribute 'paragraph'
>>> d.paragraphs[0].text
'1Paragraph'
>>> d.paragraphs[1].text
''
>>> p = d.paragraphs[2]
>>> p.runs
[<docx.text.run.Run object at 0x00E3FF70>]
>>> p.runs[0].text
'2Paragraph'
>>> p.runs[1].text
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    p.runs[1].text
IndexError: list index out of range
>>> p.runs[2].text
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    p.runs[2].text
IndexError: list index out of range
>>> p.runs[0].underline = True
>>> p.runs[0].text = 'Lets make this text Underlineed text
SyntaxError: EOL while scanning string literal
>>> p.runs[0].text = 'Lets make this text Underlineed text'
>>> d.save
<bound method Document.save of <docx.document.Document object at 0x00E60E68>>
>>> 
KeyboardInterrupt
>>> d.save('c:\\demo.docx')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d.save('c:\\demo.docx')
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\document.py", line 142, in save
    self._part.save(path_or_stream)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\parts\document.py", line 129, in save
    self.package.save(path_or_stream)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\package.py", line 160, in save
    PackageWriter.write(pkg_file, self.rels, self.parts)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\pkgwriter.py", line 32, in write
    phys_writer = PhysPkgWriter(pkg_file)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\site-packages\docx\opc\phys_pkg.py", line 141, in __init__
    self._zipf = ZipFile(pkg_file, 'w', compression=ZIP_DEFLATED)
  File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\zipfile.py", line 1090, in __init__
    self.fp = io.open(file, filemode)
PermissionError: [Errno 13] Permission denied: 'c:\\demo.docx'
>>> d.save('c:\\users\\user\desktop\\demo2.docx')
>>> 

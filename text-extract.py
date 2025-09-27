import pymupdf
doc = pymupdf.open("sample_pdf.pdf") # opening the pdf file

#get the input from user for search for a particular word
search_string = input("what word do you want to search for: ")

#iterate through each page of the document
for page_num in range(len(doc)):
    page = doc[page_num]   # get the current page number
    matches = page.search_for(search_string) # search for the particular word
    if matches:
        print(f"found '{search_string}' on page {page_num + 1} at location: {matches}")
        
    else:
        print(f"'{search_string}' was not found on {page_num + 1}")

doc.close()


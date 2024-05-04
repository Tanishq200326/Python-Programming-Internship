from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(pdf_files, output_file):
    writer = PdfWriter()
    for pdf_file in pdf_files:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            writer.add_page(page)
          
    with open(output_file, "wb") as out_pdf:
        writer.write(out_pdf)
    print("PDFs merged successfully!")

def split_pdf(input_file, output_folder, chunk_size=1):
    reader = PdfReader(input_file)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_filename = f"{output_folder}/page_{i+1}.pdf"
        with open(output_filename, "wb") as out_pdf:
            writer.write(out_pdf)
        print(f"Page {i+1} split successfully to {output_filename}")
    

# Example usage
if __name__ == "__main__":
    # Merge PDFs
    pdf_files_to_merge = ["file1.pdf", "file2.pdf", "file3.pdf"]  # List of PDF files to merge
    output_merged_pdf = "merged.pdf"  # Output merged PDF file name
    merge_pdfs(pdf_files_to_merge, output_merged_pdf)

    # Split PDF
    input_pdf_to_split = "input.pdf"  # PDF file to split
    output_folder_for_split = "split_pages"  # Folder where split PDF pages will be saved
    split_pdf(input_pdf_to_split, output_folder_for_split)

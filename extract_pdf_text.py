import PyPDF2
import sys

def extract_text_from_pdf(pdf_path, output_txt_path):
    """
    Extracts text from a PDF file and saves it to a text file.

    Args:
        pdf_path (str): The path to the input PDF file.
        output_txt_path (str): The path to save the extracted text.
    """
    try:
        with open(pdf_path, 'rb') as pdf_file_obj:
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
            raw_text = ""
            for page_num in range(len(pdf_reader.pages)):
                page_obj = pdf_reader.pages[page_num]
                try:
                    raw_text += page_obj.extract_text()
                except Exception as e:
                    print(f"Warning: Could not extract text from page {page_num + 1}. Error: {e}")
                    raw_text += "[UNABLE_TO_EXTRACT_PAGE_CONTENT]\n"
            
            # Attempt to clean and encode the text properly
            # Ignore non-UTF-8 characters
            cleaned_text = raw_text.encode('utf-8', 'ignore').decode('utf-8')

            with open(output_txt_path, 'w', encoding='utf-8') as text_file:
                text_file.write(cleaned_text)
            print(f"Successfully extracted and cleaned text from '{pdf_path}' to '{output_txt_path}'")

    except FileNotFoundError:
        print(f"Error: The file '{pdf_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_pdf_text.py <input_pdf_filename> <output_txt_filename>")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_txt = sys.argv[2]
    extract_text_from_pdf(input_pdf, output_txt)
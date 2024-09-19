import pikepdf
import sys

def remove_pdf_password(input_pdf, output_pdf, password):
    try:
        # Open the password-protected PDF
        with pikepdf.open(input_pdf, password=password) as pdf:
            # Save the PDF without the password
            pdf.save(output_pdf)
        print(f"Password removed successfully. Output saved to {output_pdf}.")
    except pikepdf._qpdf.PasswordError:
        print("Incorrect password!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python remove_pdf_password.py input.pdf output.pdf password")
    else:
        input_pdf = sys.argv[1]
        output_pdf = sys.argv[2]
        password = sys.argv[3]
        remove_pdf_password(input_pdf, output_pdf, password)

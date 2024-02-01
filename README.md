
# PDF Encryption using PyPDF2 in Bulk

![pypdf-home](https://github.com/mohammedbilalkhan/pypdf2-pdf-encryption/assets/156965348/9b0b8635-ab90-46da-928b-d649f824a3f7)

## Overview

This Python script allows you to bulk encrypt PDF files using the PyPDF2 library. The input is a CSV file (`creds.csv`) containing user information, and the script generates encrypted PDFs with unique passwords for each user. Additionally, a CSV file is generated, which includes the passwords and corresponding file names for easy reference.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python (version 3.x)
- PyPDF2 library (install using `pip install PyPDF2`)
- Tkinter library (install using `pip install tkinter`)

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mohammedbilalkhan/pypdf2-pdf-encryption.git
   cd pypdf2-pdf-encryption
   ```

2. **Prepare the CSV file (`creds.csv`):**

   The CSV file should have the following columns: `name`, `numbers`.

   ```csv
   name,numbers
   John Doe,9999999999
   Jane Smith,88888888888
   ```

3. **Run the script:**

   ```bash
   python pypdf2-encrypt-pdf.pyw
   ```

4. **Generated Files:**

   - Encrypted PDFs: `encypted logs/user_123_encrypted.pdf`, `encrypted logs/user_456_encrypted.pdf`
   - Password Details: `passwords.csv`

## Script Details

The script reads the CSV file, generates unique passwords for each user, encrypts the PDF files, and creates a CSV file with the password and corresponding file names.

### File Structure

- `pypdf2-encrypt-pdf.pyw`: The main Python script for bulk PDF encryption.
- `creds.csv`: Input CSV file containing user information.
- `encrypt logs/`: Directory to store the encrypted PDFs.
- `passwords.csv`: Output CSV file with passwords and file names.

## Example Output

After running the script, the `encrypt logs` directory will contain encrypted PDFs:

- `user_123_encrypted.pdf`
- `user_456_encrypted.pdf`

The `passwords.csv` file will have the following format:

```csv
name, numbers,password,pdffile_name
```

Feel free to customize the script or provide additional features as needed.

Happy encrypting! 📄🔒


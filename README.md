# PDF Password Remover

A simple Flask-based web application to remove passwords from PDF files. Users can upload a password-protected PDF, provide the password, and download an unlocked version. This project is open-source and intended for legal use only.

## Features

- Upload a password-protected PDF and enter its password
- Removes both user and owner passwords using the `pikepdf` library
- Clean, black-and-white UI with a legal disclaimer and ownership confirmation checkbox
- Secure in-memory processing (no files saved on disk)
- Download the unlocked PDF directly

## Legal Disclaimer

**Important:** This tool is for removing passwords from PDFs you own or have explicit permission to modify. Unauthorized use of others' PDFs is illegal and violates copyright laws. By using this tool, you confirm the PDF is yours and not used for illegal purposes.

## Prerequisites

- Python 3.8+
- Git (to clone the repository)

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/suneel-DK/pdf-unlocker.git
cd pdf-unlocker
```

### 2. Create a Virtual Environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

The `requirements.txt` includes:
- `flask` (web framework)
- `pikepdf` (PDF decryption)
- `gunicorn` (production server)

### 4. Run the Application
```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

For production, use:
```bash
gunicorn app:app
```

## Usage

1. Access the web app in your browser
2. Upload a password-protected PDF file
3. Enter the PDF's password
4. Check the box confirming you own the PDF and are using it legally
5. Click "Unlock and Download" to receive the unlocked PDF
6. If the password is incorrect, an error will display

## Project Structure

```
pdf-unlocker/
├── app.py              # Flask backend
├── templates/
│   └── index.html      # Frontend with UI and legal disclaimer
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add your feature"`
4. Push to your fork: `git push origin feature/your-feature`
5. Open a Pull Request

Please ensure your code follows the existing style and includes tests if applicable.


## Contact

For issues or suggestions, open an issue on GitHub or contact [suneel-DK] via GitHub.

---

**⚠️ Reminder:** Use this tool responsibly and only on PDFs you own or have permission to modify.
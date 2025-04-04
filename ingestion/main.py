import os
from pathlib import Path
from ingest_pipeline import ingest_document 

FOLDER_PATH = Path("/app/ingestion/docs")

VALID_EXTENSIONS = [".pdf",".docx",".txt"]

def main():
    print(f" Ingesting documents from {FOLDER_PATH.resolve()}...")

    if not FOLDER_PATH.exists():
        print(f"Folder {FOLDER_PATH} does not exist.")
        return

    for file in FOLDER_PATH.iterdir():
        if file.suffix.lower() in VALID_EXTENSIONS:
            print(f"Processing {file.name}...")
            ingest_document(str(file))

        else:
            print(f"Skipping {file.name}... Unsupported file type.")
    
    print("Ingestion complete.")

if __name__ == "__main__":
    main()
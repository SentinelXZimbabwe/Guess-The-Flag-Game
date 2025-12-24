import os
import zipfile

ZIP_NAME = "sentinelx-guess-the-flag-v1.0.0.zip"

def zip_game_folder():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    zip_path = os.path.join(base_dir, ZIP_NAME)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for foldername, subfolders, filenames in os.walk(base_dir):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)

                # Skip the zip file itself
                if filename == ZIP_NAME:
                    continue

                # Create relative path inside zip
                arcname = os.path.relpath(file_path, base_dir)
                zipf.write(file_path, arcname)

    print(f"ZIP package created successfully: {ZIP_NAME}")

if __name__ == "__main__":
    zip_game_folder()

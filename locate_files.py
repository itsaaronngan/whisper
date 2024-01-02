import os
import subprocess
import sys

def find_m4a_files(directory):
    # Find all .m4a files in the specified directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".m4a"):
                file_path = os.path.join(root, file)
                # Filters to exclude files:
                # Uncomment and modify these lines as needed
                # if os.path.getsize(file_path) < 1000000:  # Exclude files smaller than 1MB
                #     continue
                if "Record_audio" in file:  # Exclude files with "exclude_keyword" in the name
                     continue
                # if os.path.getmtime(file_path) < time.time() - 7 * 86400:  # Exclude files modified more than 7 days ago
                #     continue
                yield file_path

def process_audio_files(directory, limit, log_file_path="/Users/aaronnganm1/Documents/Coding/Whisper Transcription/output/log.txt"):
    # Process up to 'limit' .m4a files in the specified directory
    with open(log_file_path, 'a+') as log_file:  # Open the log file in append mode
        files = list(find_m4a_files(directory))  # Convert the generator to a list
        total_files = len(files)
        for i, file_path in enumerate(files):
            if limit is not None and i >= limit:
                break
            log_file.seek(0)  # Go to the start of the file
            if file_path in log_file.read():
                print(f"Skipping already transcribed file: {file_path}")
                continue  # Skip this file if it's already been transcribed
            remaining_files = total_files - i
            print(f"File: {file_path}")
            proceed = input(f"Do you want to continue? (y/n/s/l). Remaining files: {remaining_files} ")
            if proceed.lower() == 'y':
                print("Transcribing...")
                subprocess.run(["python3", "Whisper Transcription/1transcribe.py", file_path])
                log_file.write(file_path + '\n')  # Write the file path to the log file
            elif proceed.lower() == 's':
                print("Skipping this file...")
                continue  # Skip the current file and continue with the next one
            elif proceed.lower() == 'l':
                print("Logging this file without transcribing...")
                log_file.write(file_path + '\n')  # Write the file path to the log file
                continue  # Skip the current file and continue with the next one
            else:
                print("Thank you!")
                sys.exit(0)  # Exit the program

# Specify the directory to scan for .m4a files and the limit
directory = "/Users/aaronnganm1/Documents/Zoom/"
limit = None
process_audio_files(directory, limit)
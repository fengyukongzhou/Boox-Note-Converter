import os
import re

def parse_and_convert(input_file, output_folder):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract book title from the first line
    title_match = re.search(r'<<(.+?)>>', content)
    book_title = title_match.group(1) if title_match else os.path.splitext(os.path.basename(input_file))[0]
    
    output_filename = os.path.join(output_folder, f'{book_title}.md')

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(f'# {book_title}\n\n')

        # Remove the header lines more robustly
        lines = content.split('\n')
        processed_lines = []
        skip_lines = 0

        # Skip the initial "读书笔记 | <<...>>" line
        if lines and re.match(r'^读书笔记\s*\|\s*<<.+>>', lines[0]):
            skip_lines += 1
        
        # Skip the book/author line if it follows the pattern
        if len(lines) > skip_lines and re.match(r'^\s*\|\s*<<.+>>', lines[skip_lines]):
            skip_lines += 1

        processed_content = '\n'.join(lines[skip_lines:]).strip()

        notes = processed_content.split('-------------------')

        for note_text in notes:
            note_text = note_text.strip()
            if not note_text:
                continue

            lines = note_text.split('\n')
            
            chapter_title = None
            # The first line is a chapter if it doesn't contain metadata markers
            if lines and '|' not in lines[0] and '页码' not in lines[0]:
                chapter_title = lines.pop(0).strip()
                f.write('**' + chapter_title + '**\n\n')

            # Check for metadata on the (new) first line
            if lines:
                metadata_line = lines[0]
                time_page_match = re.match(r'(.+?)\s*\|\s*页码：(\d+)', metadata_line)
                if time_page_match:
                    lines.pop(0) # Consume the metadata line
                    time = time_page_match.group(1).strip()
                    page = time_page_match.group(2).strip()
                    f.write(f'**时间：** {time} | **页码：** {page}\n\n')

            # The rest is the note content
            text_content = '\n'.join(lines).strip()
            
            # Extract annotation from the content
            annotation = None
            annotation_match = re.search(r'【批注】(.+)', text_content, re.DOTALL)
            if annotation_match:
                annotation = annotation_match.group(1).strip()
                text_content = re.sub(r'【批注】.+', '', text_content, flags=re.DOTALL).strip()

            # Write the content as a blockquote
            if text_content:
                quoted_text = '\n'.join([f'> {line}' for line in text_content.split('\n')])
                f.write(f'{quoted_text}\n\n')

            # Write the annotation
            if annotation:
                f.write(f'**批注：** {annotation}\n\n')

def main():
    input_folder = 'Boox-Note-Converter'
    output_folder = os.path.join(input_folder, 'output')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.txt') and filename != 'conversion_log.txt': # Exclude the log file
            input_file = os.path.join(input_folder, filename)
            try:
                parse_and_convert(input_file, output_folder)
                print(f'Successfully converted {filename}')
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == '__main__':
    main()
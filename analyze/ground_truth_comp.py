#You can write another script to compare the OCR output with the ground truth:


import difflib

# Function to compare OCR output with ground truth
def compare_text(ocr_text, ground_truth):
    diff = difflib.ndiff(ocr_text.splitlines(), ground_truth.splitlines())
    return '\n'.join(diff)

# Example usage:
ocr_text = open('/path/to/output.txt').read()
ground_truth = open('/path/to/ground_truth.txt').read()

diff = compare_text(ocr_text, ground_truth)
print(diff)

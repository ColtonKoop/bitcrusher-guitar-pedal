"""Minimal helper to export a PDF to Markdown and plain text via pymupdf4llm.

Requirements:
- pip install pymupdf4llm
- pip install pymupdf-layout
- pip install opencv-python      # optional, only if you want OCR
- sudo apt install tesseract-ocr # optional, only if you want OCR
"""

from pathlib import Path
import pymupdf.layout  # required by pymupdf4llm for layout-aware parsing
import pymupdf4llm

# Point this at the PDF you want to convert.
PDF_PATH = Path("/home/c0lt0n/Projects/bitcrusher-guitar-pedal/docs/teensy/IMXRT1060RM_rev3_annotations.pdf")
md = pymupdf4llm.to_markdown(str(PDF_PATH))
PDF_PATH.with_suffix(".md").write_bytes(md.encode("utf-8"))

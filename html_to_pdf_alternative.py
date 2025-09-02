#!/usr/bin/env python3
"""
Alternative HTML to Single-Page PDF Converter using pdfkit

This script provides an alternative method to convert the cannabis sales sheet HTML 
document into a single-page PDF file using pdfkit and wkhtmltopdf.

Requirements:
- pdfkit: pip install pdfkit
- wkhtmltopdf: Download from https://wkhtmltopdf.org/downloads.html

Usage:
    python html_to_pdf_alternative.py
"""

import os
import sys
import tempfile
from pathlib import Path

try:
    import pdfkit
except ImportError:
    print("Error: pdfkit is not installed.")
    print("Please install it using: pip install pdfkit")
    sys.exit(1)

def create_single_page_html_content(original_html_path):
    """
    Read the original HTML and inject additional CSS for single-page layout
    
    Args:
        original_html_path (str): Path to the original HTML file
        
    Returns:
        str: Modified HTML content with single-page CSS
    """
    try:
        with open(original_html_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Additional CSS for single-page layout
        single_page_css = """
        <style>
        @page {
            size: A4;
            margin: 0.2in;
        }
        
        body {
            font-size: 6px !important;
            line-height: 1.1 !important;
            margin: 0 !important;
            padding: 0 !important;
            transform: scale(0.85);
            transform-origin: top left;
            width: 117.6% !important;
        }
        
        .container {
            max-width: none !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        
        .header {
            margin-bottom: 0.3rem !important;
            padding: 0.1rem 0 !important;
        }
        
        .logo {
            max-width: 100px !important;
            height: auto !important;
            margin: 0 auto 0.2rem !important;
            padding: 3px !important;
        }
        
        .header-subtitle {
            font-size: 7px !important;
            margin: 0 !important;
        }
        
        .promo-section {
            padding: 0.4rem !important;
            margin-bottom: 0.4rem !important;
            border-radius: 3px !important;
        }
        
        .promo-title {
            font-size: 11px !important;
            margin-bottom: 0.15rem !important;
        }
        
        .promo-subtitle {
            font-size: 8px !important;
            margin-bottom: 0.1rem !important;
        }
        
        .promo-details {
            font-size: 6px !important;
        }
        
        .product-grid {
            display: grid !important;
            grid-template-columns: repeat(4, 1fr) !important;
            gap: 0.25rem !important;
            margin-bottom: 0.4rem !important;
        }
        
        .product-card {
            padding: 0.25rem !important;
            font-size: 5px !important;
            break-inside: avoid !important;
        }
        
        .product-header {
            margin-bottom: 0.15rem !important;
            gap: 0.1rem !important;
        }
        
        .product-image,
        .flower-image {
            height: 55px !important;
            margin-bottom: 0.15rem !important;
            object-fit: contain !important;
        }
        
        .product-title {
            font-size: 6px !important;
            margin-bottom: 0.1rem !important;
            line-height: 1.0 !important;
        }
        
        .product-description {
            font-size: 4.5px !important;
            margin-bottom: 0.15rem !important;
            line-height: 1.0 !important;
        }
        
        .strain-tag,
        .thc-tag,
        .price-tag {
            font-size: 4px !important;
            padding: 0.03rem 0.08rem !important;
            margin-bottom: 0.08rem !important;
        }
        
        .quantities-title {
            font-size: 4px !important;
            margin-bottom: 0.08rem !important;
        }
        
        .quantity-tag {
            font-size: 3.5px !important;
            padding: 0.03rem 0.08rem !important;
            margin: 0.01rem !important;
        }
        
        .quantities {
            gap: 0.08rem !important;
        }
        
        .order-connect-section {
            padding: 0.4rem !important;
            margin-top: 0.4rem !important;
        }
        
        .order-connect-section h2 {
            font-size: 9px !important;
            margin-bottom: 0.15rem !important;
        }
        
        .order-connect-section p {
            font-size: 5px !important;
            margin-bottom: 0.15rem !important;
        }
        
        .order-connect-section img {
            max-width: 70px !important;
            height: auto !important;
        }
        
        .footer {
            padding: 0.25rem 0 !important;
            margin-top: 0.25rem !important;
            font-size: 4px !important;
        }
        
        .footer p {
            margin: 0.08rem 0 !important;
            font-size: 4px !important;
        }
        
        /* Special handling for dual product card */
        .product-card div[style*="display: flex"] {
            margin-bottom: 0.15rem !important;
        }
        
        .product-card div[style*="display: flex"] .product-image {
            height: 35px !important;
            width: 35px !important;
        }
        
        .product-card div[style*="display: flex"] .product-title {
            font-size: 4px !important;
        }
        </style>
        """
        
        # Insert the CSS before the closing </head> tag
        if '</head>' in html_content:
            html_content = html_content.replace('</head>', single_page_css + '\n</head>')
        else:
            # If no </head> tag found, insert after <head>
            html_content = html_content.replace('<head>', '<head>' + single_page_css)
        
        return html_content
        
    except Exception as e:
        print(f"Error reading HTML file: {str(e)}")
        return None

def convert_html_to_pdf_pdfkit(html_file_path, output_pdf_path):
    """
    Convert HTML file to single-page PDF using pdfkit
    
    Args:
        html_file_path (str): Path to the input HTML file
        output_pdf_path (str): Path for the output PDF file
    """
    try:
        # Check if HTML file exists
        if not os.path.exists(html_file_path):
            raise FileNotFoundError(f"HTML file not found: {html_file_path}")
        
        print(f"Converting {html_file_path} to PDF using pdfkit...")
        
        # Get modified HTML content
        modified_html = create_single_page_html_content(html_file_path)
        if modified_html is None:
            return False
        
        # Configure pdfkit options for single-page layout
        options = {
            'page-size': 'A4',
            'margin-top': '0.2in',
            'margin-right': '0.2in',
            'margin-bottom': '0.2in',
            'margin-left': '0.2in',
            'encoding': "UTF-8",
            'no-outline': None,
            'enable-local-file-access': None,
            'print-media-type': None,
            'disable-smart-shrinking': None,
            'zoom': 0.8
        }
        
        # Create temporary HTML file with modifications
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as temp_file:
            temp_file.write(modified_html)
            temp_html_path = temp_file.name
        
        try:
            # Convert to PDF
            pdfkit.from_file(temp_html_path, output_pdf_path, options=options)
            print(f"✅ PDF successfully created: {output_pdf_path}")
            return True
            
        finally:
            # Clean up temporary file
            try:
                os.unlink(temp_html_path)
            except:
                pass
        
    except Exception as e:
        print(f"❌ Error converting HTML to PDF: {str(e)}")
        if "wkhtmltopdf" in str(e).lower():
            print("\n💡 Tip: Make sure wkhtmltopdf is installed and in your PATH.")
            print("   Download from: https://wkhtmltopdf.org/downloads.html")
        return False

def main():
    """
    Main function to execute the conversion
    """
    # Get the directory of this script
    script_dir = Path(__file__).parent
    
    # Define file paths
    html_file = script_dir / "sales_sheetv1.html"
    output_pdf = script_dir / "cannabis_sales_sheet_single_page_alt.pdf"
    
    print("🔄 Alternative HTML to Single-Page PDF Converter (pdfkit)")
    print("=" * 55)
    print(f"Input HTML: {html_file}")
    print(f"Output PDF: {output_pdf}")
    print("=" * 55)
    
    # Convert HTML to PDF
    success = convert_html_to_pdf_pdfkit(str(html_file), str(output_pdf))
    
    if success:
        print("\n✅ Conversion completed successfully!")
        print(f"📄 Single-page PDF saved as: {output_pdf}")
        print("\n📋 Features:")
        print("   • All content scaled to fit on one page")
        print("   • Maintains visual hierarchy and readability")
        print("   • Preserves all product information")
        print("   • Optimized for printing on standard A4 paper")
        print("   • Uses pdfkit/wkhtmltopdf engine")
    else:
        print("\n❌ Conversion failed. Please check the error messages above.")
        print("\n💡 Try the main converter script (html_to_pdf_converter.py) if this doesn't work.")
        sys.exit(1)

if __name__ == "__main__":
    main()
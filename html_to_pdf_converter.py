#!/usr/bin/env python3
"""
HTML to Single-Page PDF Converter

This script converts the cannabis sales sheet HTML document into a single-page PDF file,
ensuring all content is properly scaled and formatted to fit within one page without
any overflow or loss of information.

Requirements:
- weasyprint: pip install weasyprint
- Pillow: pip install Pillow

Usage:
    python html_to_pdf_converter.py
"""

import os
import sys
from pathlib import Path
try:
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration
except ImportError:
    print("Error: weasyprint is not installed.")
    print("Please install it using: pip install weasyprint")
    sys.exit(1)

def create_single_page_css():
    """
    Create CSS rules to ensure all content fits on a single page
    """
    return CSS(string="""
        @page {
            size: A4;
            margin: 0.3in;
        }
        
        body {
            font-size: 7px !important;
            line-height: 1.2 !important;
            margin: 0;
            padding: 0;
        }
        
        .container {
            max-width: none !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        
        .header {
            margin-bottom: 0.5rem !important;
            padding: 0.2rem 0 !important;
        }
        
        .logo {
            max-width: 120px !important;
            height: auto !important;
            margin: 0 auto 0.3rem !important;
            padding: 5px !important;
        }
        
        .header-subtitle {
            font-size: 8px !important;
            margin: 0 !important;
        }
        
        .promo-section {
            padding: 0.5rem !important;
            margin-bottom: 0.5rem !important;
            border-radius: 4px !important;
        }
        
        .promo-title {
            font-size: 12px !important;
            margin-bottom: 0.2rem !important;
        }
        
        .promo-subtitle {
            font-size: 9px !important;
            margin-bottom: 0.1rem !important;
        }
        
        .promo-details {
            font-size: 7px !important;
        }
        
        .product-grid {
            display: grid !important;
            grid-template-columns: repeat(4, 1fr) !important;
            gap: 0.3rem !important;
            margin-bottom: 0.5rem !important;
        }
        
        .product-card {
            padding: 0.3rem !important;
            font-size: 6px !important;
            break-inside: avoid !important;
            page-break-inside: avoid !important;
        }
        
        .product-header {
            margin-bottom: 0.2rem !important;
            gap: 0.1rem !important;
        }
        
        .product-image,
        .flower-image {
            height: 60px !important;
            margin-bottom: 0.2rem !important;
            object-fit: contain !important;
        }
        
        .product-title {
            font-size: 7px !important;
            margin-bottom: 0.1rem !important;
            line-height: 1.1 !important;
        }
        
        .product-description {
            font-size: 5px !important;
            margin-bottom: 0.2rem !important;
            line-height: 1.1 !important;
        }
        
        .strain-tag,
        .thc-tag,
        .price-tag {
            font-size: 5px !important;
            padding: 0.05rem 0.1rem !important;
            margin-bottom: 0.1rem !important;
        }
        
        .quantities-title {
            font-size: 5px !important;
            margin-bottom: 0.1rem !important;
        }
        
        .quantity-tag {
            font-size: 4px !important;
            padding: 0.05rem 0.1rem !important;
            margin: 0.02rem !important;
        }
        
        .quantities {
            gap: 0.1rem !important;
        }
        
        .order-connect-section {
            padding: 0.5rem !important;
            margin-top: 0.5rem !important;
        }
        
        .order-connect-section h2 {
            font-size: 10px !important;
            margin-bottom: 0.2rem !important;
        }
        
        .order-connect-section p {
            font-size: 6px !important;
            margin-bottom: 0.2rem !important;
        }
        
        .order-connect-section img {
            max-width: 80px !important;
            height: auto !important;
        }
        
        .footer {
            padding: 0.3rem 0 !important;
            margin-top: 0.3rem !important;
            font-size: 5px !important;
        }
        
        .footer p {
            margin: 0.1rem 0 !important;
            font-size: 5px !important;
        }
        
        /* Special handling for dual product card */
        .product-card div[style*="display: flex"] {
            margin-bottom: 0.2rem !important;
        }
        
        .product-card div[style*="display: flex"] .product-image {
            height: 40px !important;
            width: 40px !important;
        }
        
        .product-card div[style*="display: flex"] .product-title {
            font-size: 5px !important;
        }
        
        /* Ensure no page breaks */
        * {
            page-break-inside: avoid !important;
        }
        
        .product-grid {
            page-break-inside: avoid !important;
        }
    """)

def convert_html_to_pdf(html_file_path, output_pdf_path):
    """
    Convert HTML file to single-page PDF
    
    Args:
        html_file_path (str): Path to the input HTML file
        output_pdf_path (str): Path for the output PDF file
    """
    try:
        # Check if HTML file exists
        if not os.path.exists(html_file_path):
            raise FileNotFoundError(f"HTML file not found: {html_file_path}")
        
        print(f"Converting {html_file_path} to PDF...")
        
        # Create font configuration
        font_config = FontConfiguration()
        
        # Load HTML file
        html_doc = HTML(filename=html_file_path)
        
        # Create single-page CSS
        single_page_css = create_single_page_css()
        
        # Generate PDF with custom CSS
        html_doc.write_pdf(
            output_pdf_path,
            stylesheets=[single_page_css],
            font_config=font_config
        )
        
        print(f"✅ PDF successfully created: {output_pdf_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error converting HTML to PDF: {str(e)}")
        return False

def main():
    """
    Main function to execute the conversion
    """
    # Get the directory of this script
    script_dir = Path(__file__).parent
    
    # Define file paths
    html_file = script_dir / "sales_sheetv1.html"
    output_pdf = script_dir / "cannabis_sales_sheet_single_page.pdf"
    
    print("🔄 HTML to Single-Page PDF Converter")
    print("=" * 40)
    print(f"Input HTML: {html_file}")
    print(f"Output PDF: {output_pdf}")
    print("=" * 40)
    
    # Convert HTML to PDF
    success = convert_html_to_pdf(str(html_file), str(output_pdf))
    
    if success:
        print("\n✅ Conversion completed successfully!")
        print(f"📄 Single-page PDF saved as: {output_pdf}")
        print("\n📋 Features:")
        print("   • All content scaled to fit on one page")
        print("   • Maintains visual hierarchy and readability")
        print("   • Preserves all product information")
        print("   • Optimized for printing on standard A4 paper")
    else:
        print("\n❌ Conversion failed. Please check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()